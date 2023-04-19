import unittest
from Functions import (get_num_sent,get_num_non_declarative_sent,get_num_abbr,
                      get_average_sent_len, get_average_len_word, get_default_check, top_n_grams)

class SentenceStatisticCheck(unittest.TestCase):
    def test_dot(self):
        self.assertEqual(get_num_sent("I love you."), 1)
        self.assertEqual(get_num_sent("I love you..."), 1)

    def test_exclMark(self):
        self.assertEqual(get_num_non_declarative_sent("I love you!"), 1)
        self.assertEqual(get_num_non_declarative_sent("I love you!!!"), 1)

    def test_abbreviation(self):
        self.assertEqual(get_num_sent("Mr.Smit try to do something, but there are some problems: wind, sun, etc.."), 1)

    def test_onlyNonDeclarative(self):
        self.assertEqual(get_num_non_declarative_sent("She! Me! Us!"), 3)

    def test_noNonDeclarative(self):
        self.assertEqual(get_num_non_declarative_sent("She..."), 0)


class WordsStatisticCheck(unittest.TestCase):
    def test_wordLen(self):
        self.assertEqual(get_average_len_word("Hi."), 2)
        self.assertEqual(get_average_len_word("aaaaaaaaaaaaaaaaaaaa."), 20)


if __name__ == "main":
    unittest.main()
