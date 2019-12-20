from abc import ABCMeta, abstractmethod


class AbstractStemmer(metaclass=ABCMeta):
    """
    This is an abstract class for the stemmers
    
    :param metaclass: [description], defaults to ABCMeta
    :type metaclass: [type], optional
    """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def stem_sentence(self, arabic_sentence: str) -> str:
        """
        This is an abstract method that takes an arabic sentence
        to stem each word of the sentence
        
        :param arabic_sentence: a sentence in arabic
        :type arabic_sentence: str
        :return: a stemmed sentence in arabic
        :rtype: str
        """
        pass

    @abstractmethod
    def stem_word(self, arabic_word: str) -> str:
        """
        This is an abstract method that takes an arabic word
        to stem it
        
        :param arabic_word: a word in arabic
        :type arabic_word: str
        :return: a stemmed word in arabic
        :rtype: str
        """
        pass
