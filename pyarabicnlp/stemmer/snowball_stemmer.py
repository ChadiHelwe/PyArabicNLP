from snowballstemmer import ArabicStemmer
from pyarabicnlp.stemmer.abstract_stemmer import AbstractStemmer


class SnowballStemmer(AbstractStemmer):
    """
    Snowball stemmer for Arabic
    """

    def __init__(self):
        self.stemmer = ArabicStemmer()

    def stem_sentence(self, arabic_sentence: str) -> str:
        """
        This is a method that takes an arabic sentence
        to stem each word of the sentence
        
        :param arabic_sentence: a sentence in arabic
        :type arabic_sentence: str
        :return: a stemmed sentence in arabic
        :rtype: str
        """
        arabic_words = arabic_sentence.split(" ")
        arabic_stem_words = self.stemmer.stemWords(arabic_words)
        return " ".join(arabic_stem_words)

    def stem_word(self, arabic_word: str) -> str:
        """
        This is method that takes an arabic word
        to stem it
        
        :param arabic_word: a word in arabic
        :type arabic_word: str
        :return: a stemmed word in arabic
        :rtype: str
        """
        return self.stemmer.stemWord(arabic_word)
