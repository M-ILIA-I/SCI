import argparse
from factory import Factory
from json_serializer import Json
from xml_serializer import Xml
import test_value

if __name__ == '__main__':
    # a = Xml()
    # b = Json()
    # with open('my_json_file', 'a') as f:
    #     b.dump(test_value.Counter, f)

    parser = argparse.ArgumentParser(description='Serializer of JSON, XML')
    parser.add_argument('input_dir', type=str, help='Input dir')
    parser.add_argument('source_format', type=str, help='Serialize format(json, xml) of source')
    parser.add_argument('result_format', type=str, help='Serialize format(json, xml) for result')
    parser.add_argument('output_dir', type=str, help='Output dir')
    args = parser.parse_args()

    result_format = args.result_format
    source_format = args.source_format

    if source_format == result_format:
        print("Same type of objects")
        exit()

    source_serializer = Factory.create_serializer(source_format)
    result_serializer = Factory.create_serializer(result_format)

    with open(args.input_dir) as file:
        obj = source_serializer.load(file)
        with open(args.output_dir, "w") as output_file:
            result_serializer.dump(obj, output_file)

    # with open('my_json_file') as file:
    #     obj = b.load(file)
    #     with open('my_xml_file', "w") as output_file:
    #         a.dump(obj, output_file)
