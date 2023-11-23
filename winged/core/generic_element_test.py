import unittest
import io
import sys
from winged.core.generic_element import GenericElement
from winged.core.element_abstract import ElementAbstract


class MockElement(ElementAbstract):
    def get_string(self):
        return "mock_element"


class GenericElementTest(unittest.TestCase):
    def test_add_and_getString(self):
        element = GenericElement()
        mock_element = MockElement()

        element.add(mock_element)

        self.assertEqual(element.get_string(), "mock_element")

    def test_generate(self):
        element = GenericElement()
        mock_element = MockElement()
        element.add(mock_element)

        captured_output = io.StringIO()
        sys.stdout = captured_output

        element.generate()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        self.assertEqual(output, "mock_element")


if __name__ == '__main__':
    unittest.main()
