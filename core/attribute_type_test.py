# Tests for attribute_type.py
import unittest
from typing import Tuple, Optional
from core.attribute_type import AttributeType


# # AttributeType é definido como um alias para um tipo de tupla, e não como uma classe ou uma função que pode ser
# instanciada. Em Python, quando você define um tipo de tupla usando typing.Tuple, está apenas criando um alias para
# anotar tipos, não uma função ou classe construtora.
class AttributeTypeTest(unittest.TestCase):
    def test_attribute_type(self):
        attribute_type: AttributeType = ("id", "id01")
        self.assertEqual(attribute_type[0], "id")
        self.assertEqual(attribute_type[1], "id01")


if __name__ == '__main__':
    unittest.main()
