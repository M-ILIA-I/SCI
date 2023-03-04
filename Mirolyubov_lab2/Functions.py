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


def get_num_non_declarative_sent(text: str) -> int:
    res = 0
    if len(text) == 0:
        print("You enter empty sentence")
        return res
    elif text[0] in PUNCT_MARKS.keys():
        print("The sentence can't start by punctuation mark")
        return res

    iterator = 0
    while iterator < len(text):
        if text[iterator] == "!" or text[iterator] == "?":
            while iterator != len(text) - 1 and text[iterator + 1] in PUNCT_MARKS:
                iterator += 1
            res += 1
        iterator += 1
        return res


def get_average_sent_len(text: str) -> int:
    count = 0
    text.strip(" ")
    i = 0
    while i < (len(text)):
        if ord("a") <= ord(text[i]) <= ord("z") or ord("A") <= ord(text[i]) <= ord("Z"):
            if text[i:len(text)].find(" ") != -1:
                i += text[i:len(text)].find(" ")
            else:
                count += 1
                break
            count += 1
        elif ord("0") <= ord(text[i]) <= ord("9"):
            while i < len(text) and text[i] != " " :
                if ord("a") <= ord(text[i]) <= ord("z") or ord("A") <= ord(text[i]) <= ord("Z"):
                    if text[i:len(text)].find(" ") != -1:
                        i += text[i:len(text)].find(" ")
                    else:
                        break
                    count += 1
                    break
                i += 1
        i += 1

    return count/get_num_sent(text)




