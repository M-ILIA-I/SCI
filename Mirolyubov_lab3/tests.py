import unittest
from factory import Factory
import test_value


class SerializerTest(unittest.TestCase):
    def test_json_int(self):
        factory = Factory.create_serializer('.json')
        old_obj = test_value.int_test
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_float(self):
        factory = Factory.create_serializer('.json')
        old_obj = test_value.float_test
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_bool(self):
        factory = Factory.create_serializer('.json')
        old_obj = test_value.bool_test
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_none(self):
        factory = Factory.create_serializer('.json')
        old_obj = test_value.none_test
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_str(self):
        factory = Factory.create_serializer('.json')
        old_obj = test_value.str_test
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_list(self):
        factory = Factory.create_serializer('.json')
        old_obj = test_value.list1_test
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_tuple(self):
        factory = Factory.create_serializer('.json')
        old_obj = test_value.tuple1_test
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_set(self):
        factory = Factory.create_serializer('.json')
        old_obj = test_value.set1_test
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_dict(self):
        factory = Factory.create_serializer('.json')
        old_obj = test_value.dict1_test
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_lambda(self):
        factory = Factory.create_serializer('.json')
        old_obj = test_value.lambda_fanc
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj(1), new_obj(1))

    def test_json_simple_func(self):
        factory = Factory.create_serializer('.json')
        old_obj = test_value.simple_func
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj(2), new_obj(2))

    def test_json_complex_func(self):
        factory = Factory.create_serializer('.json')
        old_obj = test_value.complex_func
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj(2), new_obj(2))

    def test_json_lib_func(self):
        factory = Factory.create_serializer('.json')
        old_obj = test_value.math_func
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj(2), new_obj(2))

    def test_json_simple_class_(self):
        factory = Factory.create_serializer('.json')
        old_obj = test_value.Counter
        new_obj = factory.loads(factory.dumps(old_obj))
        a = old_obj()
        b = new_obj()
        a.inc()
        b.inc()
        self.assertEqual(a.value, b.value)

    def test_json_heritage_class_(self):
        factory = Factory.create_serializer('.json')
        old_obj = test_value.DoubleCounter
        new_obj = factory.loads(factory.dumps(old_obj))
        first_object = old_obj()
        second_object = new_obj()
        first_object.inc()
        second_object.inc()
        self.assertEqual(first_object.value, second_object.value)

    def test_json_class_method(self):
        factory = Factory.create_serializer('.json')
        old_obj = test_value.Employee
        new_obj = factory.loads(factory.dumps(old_obj))
        a = old_obj("dd", 2)
        b = new_obj("df", 4)
        self.assertEqual(a.display_count(), b.display_count())

    def test_json_inner_func(self):
        factory = Factory.create_serializer('.json')
        old_obj = test_value.inner_func
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj(2), new_obj(2))

    def test_json_recursive_func(self):
        factory = Factory.create_serializer('.json')
        old_obj = test_value.factorial_recursive
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj(5), new_obj(5))

    def test_json_class_method(self):
        factory = Factory.create_serializer('.json')
        old_obj = test_value.Employee("dd", 2)
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj.name, new_obj.name)

    def test_xml_int(self):
        factory = Factory.create_serializer('.xml')
        old_obj = test_value.int_test
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_xml_float(self):
        factory = Factory.create_serializer('.xml')
        old_obj = test_value.float_test
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_xml_bool(self):
        factory = Factory.create_serializer('.xml')
        old_obj = test_value.bool_test
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_xml_none(self):
        factory = Factory.create_serializer('.xml')
        old_obj = test_value.none_test
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_xml_str(self):
        factory = Factory.create_serializer('.xml')
        old_obj = test_value.str_test
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_xml_list(self):
        factory = Factory.create_serializer('.xml')
        old_obj = test_value.list1_test
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_xml_tuple(self):
        factory = Factory.create_serializer('.xml')
        old_obj = test_value.tuple1_test
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_xml_set(self):
        factory = Factory.create_serializer('.xml')
        old_obj = test_value.set1_test
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_xml_dict(self):
        factory = Factory.create_serializer('.xml')
        old_obj = test_value.dict1_test
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_xml_lambda(self):
        factory = Factory.create_serializer('.xml')
        old_obj = test_value.lambda_fanc
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj(1), new_obj(1))

    def test_xml_simple_func(self):
        factory = Factory.create_serializer('.xml')
        old_obj = test_value.simple_func
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj(2), new_obj(2))

    def test_xml_complex_func(self):
        factory = Factory.create_serializer('.xml')
        old_obj = test_value.complex_func
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj(2), new_obj(2))

    def test_xml_lib_func(self):
        factory = Factory.create_serializer('.xml')
        old_obj = test_value.math_func
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj(2), new_obj(2))

    def test_xml_simple_class_(self):
        factory = Factory.create_serializer('.xml')
        old_obj = test_value.Counter
        new_obj = factory.loads(factory.dumps(old_obj))
        a = old_obj()
        b = new_obj()
        a.inc()
        b.inc()
        self.assertEqual(a.value, b.value)

    def test_xml_heritage_class_(self):
        factory = Factory.create_serializer('.xml')
        old_obj = test_value.DoubleCounter
        new_obj = factory.loads(factory.dumps(old_obj))
        first_object = old_obj()
        second_object = new_obj()
        first_object.inc()
        second_object.inc()
        self.assertEqual(first_object.value, second_object.value)

    def test_xml_class_method(self):
        factory = Factory.create_serializer('.xml')
        old_obj = test_value.Employee
        new_obj = factory.loads(factory.dumps(old_obj))
        a = old_obj("dd", 2)
        b = new_obj("df", 4)
        self.assertEqual(a.display_count(), b.display_count())

    def test_xml_inner_func(self):
        factory = Factory.create_serializer('.xml')
        old_obj = test_value.inner_func
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj(2), new_obj(2))

    def test_xml_recursive_func(self):
        factory = Factory.create_serializer('.xml')
        old_obj = test_value.factorial_recursive
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj(5), new_obj(5))

    def test_xml_class_method(self):
        factory = Factory.create_serializer('.xml')
        old_obj = test_value.Employee("dd", 2)
        new_obj = factory.loads(factory.dumps(old_obj))
        self.assertEqual(old_obj.name, new_obj.name)


