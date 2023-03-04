from CONST import *
import copy


def get_default_check(text: str) -> bool:
    if len(text) == 0:
        print("You enter empty sentence")
        return False
    elif text[0] in PUNCT_MARKS.keys():
        print("The sentence can't start by punctuation mark")
        return False
    else:
        return True


def get_num_abbr(text: str) -> int:
    res = 0
    for i in ABBR_WORD.keys():
        res += text.count(i)
    return res


def get_num_sent(text: str) -> int:
    res = 0
    if get_default_check(text):
        iterator = 0
        while iterator < len(text):
            if text[iterator] in PUNCT_MARKS:
                while iterator != len(text) - 1 and text[iterator + 1] in PUNCT_MARKS:
                    iterator += 1
                res += 1
            iterator += 1
        return res - get_num_abbr(text.lower())
    else:
        return res


def get_num_non_declarative_sent(text: str) -> int:
    res = 0
    if get_default_check():
        iterator = 0
        while iterator < len(text):
            if text[iterator] == "!" or text[iterator] == "?":
                while iterator != len(text) - 1 and text[iterator + 1] in PUNCT_MARKS:
                    iterator += 1
                res += 1
            iterator += 1
        return res
    else:
        return res


def get_average_sent_len(text: str) -> float:
    if get_default_check():
        txt = copy.copy(text)

        for i in PUNCT_FOR_WORDS.keys():
            txt = txt.replace(i, " ")

        txt = txt.split()
        return len(txt)/get_num_sent(text)

    else:
        return 0


def get_average_len_word(text: str) -> float:
    if get_default_check():
        length = 0
        txt = copy.copy(text)
        lst = txt.split()

        for i in PUNCT_FOR_WORDS.keys():
            txt = txt.replace(i, " ")

        txt = txt.split()

        for i in txt:
            length += len(i)

        return length/len(txt)

    else:
        return 0




