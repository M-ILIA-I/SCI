from MirSerializer.json_serializer import Json
from MirSerializer.xml_serializer import Xml


class Factory:
    @staticmethod
    def create_serializer(format):
        if format == ".json":
            return Json()

        elif format == ".xml":
            return Xml()

        else:
            raise Exception("Unknown type of serialization")
