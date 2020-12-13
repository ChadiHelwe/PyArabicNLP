NER_LABEL_TO_ID = {
    "O": 0,
    "B-ORG": 1,
    "I-ORG": 2,
    "B-PER": 3,
    "I-PER": 4,
    "B-LOC": 5,
    "I-LOC": 6,
}

ID_TO_NER_LABEL = {value: key for key, value in NER_LABEL_TO_ID.items()}


def clean_label(ner_label: str) -> str:
    """
    Clean the ner label from whitespaces

    :param ner_label: takes a ner label
    :type ner_label: str
    :return: a cleaned label is returned
    :rtype: str
    """
    if "B-ORG" in ner_label:
        return "B-ORG"
    elif "I-ORG" in ner_label:
        return "I-ORG"
    elif "B-PER" in ner_label:
        return "B-PER"
    elif "I-PER" in ner_label:
        return "I-PER"
    elif "B-LOC" in ner_label:
        return "B-LOC"
    elif "I-LOC" in ner_label:
        return "I-LOC"
    elif "O" in ner_label:
        return "O"


def ner_label_to_id(ner_label: str) -> int:
    """
    return the id of the ner label

    :param ner_label: ner label
    :type ner_label: str
    :return: id of the ner label
    :rtype: int
    """
    return NER_LABEL_TO_ID[ner_label]


def id_to_ner_label(id: int) -> str:
    """
    return the ner label of the id

    :param id: id of the ner label
    :type id: int
    :return: ner label
    :rtype: str
    """
    return ID_TO_NER_LABEL[id]
