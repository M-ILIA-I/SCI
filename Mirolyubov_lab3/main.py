import inspect
from json_serializer import Json


def summ(a=11, b=23):
    return a+b


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


def main():
    person = Person("jhon", 34)
    ser = Json()
    a = ser.dumps(person)
    b = ser.loads(a)
    print(b.age)


if __name__ == "__main__":
    main()
