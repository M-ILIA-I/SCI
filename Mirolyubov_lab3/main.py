import inspect
from json_serializer import Json
from xml_serializer import Xml
from test_value import *
from packing import convert

def summ(a=11, b=23):
    return a+b


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


def main():
    ser = Json()
    xm = Xml()
    #print((xm.dumps(lambda_fanc)))
    #a = xm.dumps({"b": {"c": {'d': {}}}, "A": 3})
    #print(a)
    #print(xm.loads(a))
    #print(convert(lambda_fanc))
    a = (xm.loads(xm.dumps(Employee)))("ilya", 300)
    a.display_employee()
     #print(xm._deserialize_from_str(xm.dumps(Counter)))




if __name__ == "__main__":
    main()
