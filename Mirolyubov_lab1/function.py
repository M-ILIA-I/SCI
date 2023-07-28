
def hello_foo():
    print("hello world!!!")


def calculate(num1, num2, op: str) -> float:
    op = op.lower()

    if (type(num1) == float or type(num1) == int) and (type(num2) == float or type(num2) == int):
        match op:
            case "add":
                return num1 + num2
            case "sub":
                return num1 - num2
            case "mult":
                return num1 * num2
            case "div":
                return num1 / num2
            case _:
                print("You operation does not exists")
    else:
        print("The number is not valid")


def get_even_num(lst: list):
    lst1 = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst1.append(lst[i])

    return lst1
