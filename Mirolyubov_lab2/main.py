from CONST import *


def get_num_abbr(text: str) -> int:
    res = 0
    for i in ABBR_WORD.keys():
           res += text.count(i)
    return res


def get_num_sent(text: str) -> int:
    res = 0
    if len(text) == 0:
        print("You enter empty sentence")
        return res
    elif text[0] in PUNCT_MARKS.keys():
        print("The sentence can't start by punctuation mark")
        return res

    iterator = 0
    while iterator < len(text):
        if text[iterator] in PUNCT_MARKS:
            while iterator != len(text) - 1 and text[iterator + 1] in PUNCT_MARKS:
                iterator += 1
            res += 1
        iterator += 1

    return res - get_num_abbr(text.lower())


text = input()

print(get_num_sent(text))
