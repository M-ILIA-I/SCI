from CONST import *
#from nltk.util import ngrams
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
    if get_default_check(text):
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
    if get_default_check(text):
        txt = copy.copy(text)

        for i in PUNCT_FOR_WORDS.keys():
            txt = txt.replace(i, " ")

        txt = txt.split()
        digit_counter = 0

        for i in txt:
            if i.isdigit():
                digit_counter += 1

        return (len(txt)-digit_counter)/get_num_sent(text)

    else:
        return 0


def get_average_len_word(text: str) -> float:
    if get_default_check(text):
        length = 0
        txt = copy.copy(text)

        for i in PUNCT_FOR_WORDS.keys():
            txt = txt.replace(i, " ")

        txt = txt.split()
        digit_counter = 0

        for i in txt:
            if not i.isdigit():
                length += len(i)
            else:
                digit_counter += 1

        return length/(len(txt) - digit_counter)

    else:
        return 0


def top_n_grams(k: int, n: int, text: str) -> list:
    if get_default_check(text):
        res = []
        txt = copy.copy(text)
        lst = txt.split()

        for i in PUNCT_FOR_WORDS.keys():
            txt = txt.replace(i, " ")

        txt = txt.split()
        n_grams = ngrams(txt, n)

        lst = [" ".join(grams) for grams in n_grams]
        lst = sorted(lst, key=lst.count, reverse=True)

        i = 0
        while i < len(lst):
            res.append(lst[i])
            i += lst.count(lst[i])
            k -= 1
            if k == 0:
                break

        return res
    else:
        return [0]


def menu():
    print("1. The number of sentences in the text")
    print("2. The number of non-declarative sentences in the text")
    print("3. Average length of the sentences")
    print("4. Average length of the words")
    print("5. Top K-repeated N-grams in the text")
