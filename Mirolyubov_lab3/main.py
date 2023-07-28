from Mirolyubov_lab3_new_version.factory import Factory
import test_value
import inspect
#
# if __name__ == '__main__':
#     # a = Xml()
#     # b = Json()
#     # with open('my_json_file', 'a') as f:
#     #     b.dump(test_value.Counter, f)
#
#     parser = argparse.ArgumentParser(description='Serializer of JSON, XML')
#     parser.add_argument('input_dir', type=str, help='Input dir')
#     parser.add_argument('source_format', type=str, help='Serialize format(json, xml) of source')
#     parser.add_argument('result_format', type=str, help='Serialize format(json, xml) for result')
#     parser.add_argument('output_dir', type=str, help='Output dir')
#     args = parser.parse_args()
#
#     result_format = args.result_format
#     source_format = args.source_format
#
#     if source_format == result_format:
#         print("Same type of objects")
#         exit()
#
#     source_serializer = Factory.create_serializer(source_format)
#     result_serializer = Factory.create_serializer(result_format)
#
#     with open(args.input_dir) as file:
#         obj = source_serializer.load(file)
#         with open(args.output_dir, "w") as output_file:
#             result_serializer.dump(obj, output_file)

    # with open('my_json_file') as file:
    #     obj = b.load(file)
    #     with open('my_xml_file', "w") as output_file:
    #         a.dump(obj, output_file)

import math
from Mirolyubov_lab3_new_version.factory import Factory

def my_decor(meth):
    def inner(*args, **kwargs):
        print('I am in my_decor')
        return meth(*args, **kwargs)

    return inner


class A:
    x = 10

    @my_decor
    def my_sin(self, c):
        return math.sin(c * self.x)

    @staticmethod
    def stat():
        return 145

    def __str__(self):
        return 'AAAAA'

    def __repr__(self):
        return 'AAAAA'


class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def prop(self):
        return self.a * self.b

    @classmethod
    def class_meth(cls):
        return math.pi


class C(A, B):
    pass


ser = Factory.create_serializer('.xml')
from Mirolyubov_lab3_new_version.json_serializer import Json
from Mirolyubov_lab3_new_version import packing


print(ser.dumps(A))

# var = 15
# var_ser = ser.dumps(var)
# var_des = ser.loads(var_ser)
# print(var_des)
#
# C_ser = ser.dumps(C)
# C_des = ser.loads(C_ser)
#
# c = C(1, 2)
# c_ser = ser.dumps(c)
# c_des = ser.loads(c_ser)
#
# print(c_des)
# print(c_des.x)
# print(c_des.my_sin(10))
# print(c_des.prop)
# print(C_des.stat())
# print(c_des.class_meth())


# def f(a):
#     for i in a:
#         yield i
#
#
# g = f([1, 2, 3])
# print(next(g))
# g_s = ser.dumps(g)
# g_d = ser.loads(g_s)
# print(next(g_d))
#

def a(x):
    yield x[0]
    x[1] += 2
    yield


