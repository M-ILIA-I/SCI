# from CONST import *
from task1.CONST import K, N
from task1.Functions import (menu, get_num_sent, get_num_non_declarative_sent,
                             get_average_sent_len, get_average_len_word, top_n_grams)

# from Functions import *


if __name__ == "__main__":
    text = ""
    print("Press 1 for reading text and any char for input: ", end="")
    var = input()

    match var:
        case '1':
            f = open("My_text", 'r')
            text = f.read()
        case _:
            text = input()

    print(f"\n{text}\n")
    menu()
    print("\n\nChoose operation: ", end="")

    var = input()

    match var:
        case '1':
            print(f"The number of sentences: {get_num_sent(text)}")
        case '2':
            print(f"The number of non-declarative sentences: {get_num_non_declarative_sent(text)}")
        case '3':
            print(f"Average length of the sentences: {get_average_sent_len(text)}")
        case '4':
            print(f"Average length of the words: {get_average_len_word(text)}")
        case '5':
            print("Enter 1 if you want to choose K and N: ", end='')
            if input() == '1':
                print("Enter K value: ", end='')
                P = int(input())
                print("Enter N value: ", end='')
                L = int(input())
                print(f"Top K-repeated N-grams in the text: {top_n_grams(P, L, text)}")
            else:
                print(f"Top K-repeated N-grams in the text: {top_n_grams(K, N, text)}")
        case _:
            print("This operation is not supported")


