import os
import requests
from zipfile import ZipFile

from tqdm import tqdm

PRETRAINED_WORD_EMBEDDINGS = {
    "twitter-cbow-300d": "https://archive.org/download/aravec2.0/tweet_cbow_300.zip",
    "twitter-skipgram-300d": "https://archive.org/download/aravec2.0/tweets_sg_300.zip",
    "twitter-cbow-100d": "https://archive.org/download/aravec2.0/tweet_cbow_100.zip",
    "twitter-skipgram-100d": "https://archive.org/download/aravec2.0/tweets_sg_100.zip",
    "wikipedia-cbow-300d": "https://archive.org/download/aravec2.0/wiki_cbow_300.zip",
    "wikipedia-skipgram-300d": "https://archive.org/download/aravec2.0/wiki_sg_300.zip",
    "wikipedia-cbow-100d": "https://archive.org/download/aravec2.0/wiki_cbow_100.zip",
    "wikipedia-skipgram-100d": "https://archive.org/download/aravec2.0/wiki_sg_100.zip",
    "web-cbow-300d": "https://archive.org/download/aravec2.0/www_cbow_300.zip",
    "web-skipgram-300d": "https://archive.org/download/aravec2.0/www_sg_300.zip",
    "web-cbow-100d": "https://archive.org/download/aravec2.0/www_cbow_100.zip",
    "web-skipgram-100d": "https://archive.org/download/aravec2.0/www_sg_100.zip",
}


class EmbeddingFileNameError(Exception):
    """
    Raised when a pretrained word embedding file name is wrong
    """

    def __init__(self):
        self.message = "EmbeddingFileNameError: Pretrained word embedding file name is wrong"


class FileSizeError(Exception):
    """
    Raised when a downloaded file has a wrong size
    """

    def __init__(self):
        self.message = "FileSizeError: Wrong file size"


def ___download(path: str, folder_name: str, file_name: str) -> None:
    """
    Private helper method to download the pretrained word embeddings
    
    :param path: current path
    :type path: str
    :param folder_name: folder name that contains the pretrained word embeddings
    :type folder_name: str
    :param file_name: file name of the pretrained word embedding
    :type file_name: str
    :raises FileSizeError: raised when the downloaded file has a wrong size
    """

    file_name_on_disk = file_name.replace("-", "_") + ".zip"
    path_folder_name = f"{path}/{folder_name}"
    path_file_name_on_disk = f"{path_folder_name}/{file_name_on_disk}"

    if file_name_on_disk not in os.listdir(path_folder_name):
        url = PRETRAINED_WORD_EMBEDDINGS[file_name]
        req = requests.get(url, stream=True)
        total_size = int(req.headers["content-length"])
        block_size = 1024
        t = tqdm(total=total_size, unit="iB", unit_scale=True)

        with open(path_file_name_on_disk, "wb") as f:
            for data in req.iter_content(block_size):
                t.update(len(data))
                f.write(data)

        t.close()

        try:
            if total_size != 0 and t.n != total_size:
                raise FileSizeError()
            else:
                with ZipFile(path_file_name_on_disk, "r") as zipObj:
                    folder_name_embedding = file_name_on_disk.replace(
                        ".zip", ""
                    )
                    path_embedding_folder = (
                        f"{folder_name}/{folder_name_embedding}"
                    )

                    if not os.path.exists(path_embedding_folder):
                        os.mkdir(path_embedding_folder)

                    zipObj.extractall(f"{folder_name}/{folder_name_embedding}")
        except FileSizeError as e:
            print(e.message)


def download_pretrained_word_embeddings(word_embeddings_name: str) -> None:
    """
    Download pretrained Arabic word embeddings
    
    :param word_embeddings_name: word embedding file name
    :type word_embeddings_name: str
    :raises EmbeddingFileNameError: raised when the pretrained word embedding file name is wrong
    """

    path = os.getcwd()
    folder_name = "pretrained_word_embeddings"

    if folder_name not in os.listdir(path):
        os.mkdir(folder_name)

    try:
        if word_embeddings_name not in PRETRAINED_WORD_EMBEDDINGS.keys():
            raise EmbeddingFileNameError()

        ___download(path, folder_name, word_embeddings_name)

    except EmbeddingFileNameError as e:
        list_pretrained_embeddings = " ".join(
            [file_name for file_name in PRETRAINED_WORD_EMBEDDINGS.keys()]
        )
        print(e.message)
        print(
            f"Pretrained word embeddings available: {list_pretrained_embeddings}"
        )
