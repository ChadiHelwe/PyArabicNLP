class Buckwalter:
    """ 
    Buckwalter transliteration uses ASCII characters to represent
    Arabic Orthography
    """

    ARABIC_TO_BUCKWALTER = {
        "\u0621": "'",
        "\u0623": ">",
        "\u0624": "&",
        "\u0625": "<",
        "\u0626": "}",
        "\u0627": "A",
        "\u0628": "b",
        "\u0629": "p",
        "\u062A": "t",
        "\u062B": "v",
        "\u062C": "j",
        "\u062D": "H",
        "\u062E": "x",
        "\u062F": "d",
        "\u0630": "*",
        "\u0631": "r",
        "\u0632": "z",
        "\u0633": "s",
        "\u0634": "$",
        "\u0635": "S",
        "\u0636": "D",
        "\u0637": "T",
        "\u0638": "Z",
        "\u0639": "E",
        "\u063A": "g",
        "\u0640": "_",
        "\u0641": "f",
        "\u0642": "q",
        "\u0643": "k",
        "\u0644": "l",
        "\u0645": "m",
        "\u0646": "n",
        "\u0647": "h",
        "\u0648": "w",
        "\u0649": "Y",
        "\u064A": "y",
        "\u064B": "F",
        "\u064C": "N",
        "\u064D": "K",
        "\u064E": "a",
        "\u064F": "u",
        "\u0650": "i",
        "\u0651": "~",
        "\u0652": "o",
        "\u0653": "^",
        "\u0654": "#",
        "\u0670": "`",
        "\u0671": "{",
        "\u06DC": ":",
        "\u06DF": "@",
        "\u06E0": '"',
        "\u06E2": "[",
        "\u06E3": ";",
        "\u06E5": ",",
        "\u06E6": ".",
        "\u06E8": "!",
        "\u06EA": "-",
        "\u06EB": "+",
        "\u06EC": "%",
        "\u06ED": "]",
    }

    def __init__(self):

        self.BUCKWALTER_TO_ARABIC = {v: k for k, v in self.ARABIC_TO_BUCKWALTER.items()}

    def transform_to_buckwalter(self, arabic_sentence: str) -> str:
        """
        This method takes a sentence in Arabic and transliterates 
        it to a Buckwalter form

        :param arabic_sentence: a sentence tranformed in Arabic
        :type arabic_sentence: str
        :return:  a sentence transliterated to buckwalter
        :rtype: str
        """
        buckwalter_sentence = ""
        for w in arabic_sentence:
            try:
                buckwalter_sentence += self.ARABIC_TO_BUCKWALTER[w]
            except KeyError:
                buckwalter_sentence += w
        return buckwalter_sentence

    def transform_to_arabic(self, buckwalter_sentence: str) -> str:
        """
        This method takes a sentence in a Buckwalter
        sentence and transliterates to Arabic 

        :param buckwalter_sentence: a sentence in buckwalter
        :type buckwalter_sentence: str
        :return: a sentence transliterated to Arabic
        :rtype: str
        """
        arabic_sentence = ""
        for w in buckwalter_sentence:
            try:
                arabic_sentence += self.BUCKWALTER_TO_ARABIC[w]
            except KeyError:
                arabic_sentence += w
        return arabic_sentence
