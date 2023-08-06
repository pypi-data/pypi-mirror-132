import json
from json.decoder import JSONDecodeError

from pyonepassword.py_op_exceptions import OPInvalidItemException


class OPUnknownItemType(Exception):
    def __init__(self, msg, item_dict=None):
        super().__init__(msg)
        self.item_dict = item_dict


class OPItemFactory:
    _TYPE_REGISTRY = {}

    @classmethod
    def register_op_item_type(cls, item_type, item_class):
        cls._TYPE_REGISTRY[item_type] = item_class

    @classmethod
    def op_item_from_item_dict(cls, item_dict):
        item_type = item_dict["templateUuid"]
        try:
            item_cls = cls._TYPE_REGISTRY[item_type]
        except KeyError as ke:
            raise OPUnknownItemType(
                "Unknown item type", item_dict=item_dict) from ke

        return item_cls(item_dict)

    @classmethod
    def op_item_from_json(cls, item_json: str):
        try:
            unserialized = json.loads(item_json)
        except JSONDecodeError as jdce:
            raise OPInvalidItemException(
                f"Failed to unserialize item JSON: {jdce}") from jdce
        obj = cls.op_item_from_item_dict(unserialized)
        return obj


def op_register_item_type(item_class):
    item_type = item_class.TEMPLATE_ID
    OPItemFactory.register_op_item_type(item_type, item_class)
    return item_class
