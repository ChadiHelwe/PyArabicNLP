import os
import sys

from pyarabicnlp.transliteration.buckwalter import Buckwalter


def test_transform_to_buckwalter():
    test = "عودة التوتر في لبنان 12345 !!!"
    expected = "Ewdp Altwtr fy lbnAn 12345 !!!"
    buck_transliteration = Buckwalter()
    assert expected == buck_transliteration.transform_to_buckwalter(test)


def test_transform_to_arabic():
    test = "Ewdp Altwtr fy lbnAn"
    expected = "عودة التوتر في لبنان"
    buck_transliteration = Buckwalter()
    assert expected == buck_transliteration.transform_to_arabic(test)
