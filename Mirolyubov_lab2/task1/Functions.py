import copy
import re
from task1.CONST import PUNCT_MARKS, ABBR_WORD, PUNCT_FOR_WORDS


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
    txt = copy.copy(text)
    txt = txt.lower()
    if get_default_check(text):
        iterator = 0
        num_abbr = get_num_abbr(text)
        for i in ABBR_WORD:
            txt = re.sub(i, "", txt)

        while iterator < len(txt):
            if txt[iterator] in PUNCT_MARKS:
                while iterator != len(txt) - 1 and txt[iterator + 1] in PUNCT_MARKS:
                    iterator += 1
                res += 1
            iterator += 1
        return res
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
        print(txt)
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
    txt = copy.copy(text)
    for i in PUNCT_FOR_WORDS:
        txt = txt.replace(i, "")
    txt = txt.replace(" ", '')
    txt = txt.lower()
    txt = list(txt)
    final_ngrams = {}
    for i in range(len(txt)-n+1):
        ngram = "".join(txt[i:i + n])
        if ngram in final_ngrams:
            final_ngrams[ngram] += 1
        else:
            final_ngrams[ngram] = 0

    lst = sorted(final_ngrams, key=final_ngrams.get, reverse=True)
    return lst[0:k]


def menu():
    print("1. The number of sentences in the text")
    print("2. The number of non-declarative sentences in the text")
    print("3. Average length of the sentences")
    print("4. Average length of the words")
    print("5. Top K-repeated N-grams in the text")
