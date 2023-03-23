from CONST import *
from Functions import *


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
            print(f"Top K-repeated N-grams in the text: {top_n_grams(K, N, text)}")
        case _:
            print("This operation is not supported")


