import snowballstemmer


class SnowballStemmer:
    """[summary]
    """

    def __init__(self):
        self.stemmer = snowballstemmer.ArabicStemmer()

    def stem_sentence(self, arabic_sentence: str) -> str:
        """[summary]
        
        :param arabic_sentence: [description]
        :type arabic_sentence: str
        :return: [description]
        :rtype: str
        """
        arabic_words = arabic_sentence.split(" ")
        arabic_stem_words = self.stemmer.stemWords(arabic_words)
        return " ".join(arabic_stem_words)

    def stem_word(self, arabic_word: str) -> str:
        """[summary]
        
        :param arabic_word: [description]
        :type arabic_word: str
        :return: [description]
        :rtype: str
        """
        return self.stemmer.stemWord(arabic_word)
