from abc import ABCMeta, abstractmethod


class AbstractWordEmbeddings(metaclass=ABCMeta):
    """
    This is an abstract class for the word embeddings

    :param metaclass: [description], defaults to ABCMeta
    :type metaclass: [type], optional
    """

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def initialize_word_embeddings(self, word_embeddings_file: str) -> None:
        """
        This is an abstract method that takes an word embeddings file
        to initialize the word vectors

        :param word_embeddings_file: a word embeddings file
        :type word_embeddings_file: str
        """
        pass
