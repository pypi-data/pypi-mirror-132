import io
import logging
import os
import ssl
import time
from typing import Union, List
from typing.io import BinaryIO, IO

from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from httplib2 import Http
from oauth2client import file, client, tools

from gdrivewrapper.decorator.single import prevent_concurrent_calls

logging.getLogger("googleapiclient").setLevel(logging.FATAL)

DEFAULT_UPLOAD_RETRY_COUNT = 5


def get_service_object(scopes: Union[str, List[str]], creds_path: str, api_name="drive", api_version="v3"):
    """
    Creates a Service object
    :param scopes: scope of the service (ex. "https://www.googleapis.com/auth/drive.file")
    :param creds_path: local path to the credentials file
    :param api_name: name of the api (ex. "gdrive")
    :param api_version:  version of the api (ex. "v3")
    :return: A Service object
    """

    creds_parent = os.path.split(creds_path)[0]
    creds_filename = os.path.split(creds_path)[1]
    creds_basename = os.path.splitext(creds_filename)[0]

    token_path = os.path.join(creds_parent, f"{creds_basename}_store.json")
    store = file.Storage(token_path)
    creds = store.get()

    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(creds_path, scopes)
        creds = tools.run_flow(flow, store)

    return build(api_name, api_version, http=creds.authorize(Http()))


def _download(service, key, fp: Union[IO, BinaryIO]):
    request = service.files().get_media(fileId=key)
    downloader = MediaIoBaseDownload(fp, request)

    done = False
    while not done:
        status, done = downloader.next_chunk()


class GDriveWrapper:
    def __init__(self, scopes: Union[str, List[str]], creds_path: str, allow_concurrent_calls=True):
        self.svc = get_service_object(scopes, creds_path)
        if not allow_concurrent_calls:
            prevent_concurrent_calls(self)

    def upload(self, media, key=None, folder_id=None, thumbnail=None, retry_count=DEFAULT_UPLOAD_RETRY_COUNT, **kwargs):
        """
        Uploads the given data to google drive. This function can create a new file or update an existing file.
        :param media: Data to upload
        :param key: (update-only) FileId of the file to update
        :param folder_id: (Optional) FileId of the containing folder
        :param thumbnail: (Optional) bytearray for the thumbnail image, b64-encoded.
        :param retry_count: number of times to retry upon common errors such as SSLError/BrokenPipeError
        :param kwargs: keyword args
        :return:
        """
        if folder_id:
            kwargs["parents"] = [folder_id]

        if thumbnail:
            content_hints = kwargs.get("contentHints", dict())
            content_hints.update({
                "thumbnail": {
                    "image": thumbnail,
                    "mimeType": "image/png"
                }
            })
            kwargs["contentHints"] = content_hints

        last_exception_msg = None
        for i in range(retry_count):
            try:
                if key:
                    return self.svc.files().update(fileId=key, body=kwargs, media_body=media).execute()
                else:
                    return self.svc.files().create(body=kwargs, media_body=media).execute()
            except (ssl.SSLError, BrokenPipeError) as e:
                last_exception_msg = str(e)
                time.sleep(1)
                continue

        # Stacktrace is lost at this point in time. The next best thing is to create a new exception
        raise RuntimeError(last_exception_msg)

    def download_bytes(self, key: str) -> bytes:
        """
        Downloads a file as bytearray
        :param key: FileId of the file to download
        :return: bytes
        """
        with io.BytesIO() as bytesio:
            _download(self.svc, key, fp=bytesio)
            return bytesio.getvalue()

    def download_file(self, key, local_path):
        """
        Downloads a file as bytearray
        :param key: FileId of the file to download
        :param local_path: Destination path in the local filesystem
        """
        with open(local_path, "wb") as fp:
            _download(self.svc, key, fp)

    def create_folder(self, name, folder_id=None, **kwargs):
        """
        Creates a folder and returns the FileId
        :param name: name of the folder
        :param folder_id: (Optional) FileId of the containing folder
        :return: folder object
        """
        kwargs["name"] = name
        kwargs["mimeType"] = "application/vnd.google-apps.folder"
        if folder_id:
            kwargs["parents"] = [folder_id]
        return self.svc.files().create(body=kwargs).execute()

    def create_comment(self, key, comment):
        """
        Posts a comment to an existing file
        :param key: FileId of the file to post comment to
        :param comment: string
        :return: comment id
        """
        return self.svc.comments().create(fileId=key, body={'content': comment}, fields="id").execute()
