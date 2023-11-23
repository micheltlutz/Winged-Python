import unittest
from abc import ABC

from HTML.div import Div
import io
import sys
from core.element_abstract import ElementAbstract


class MockElement(ElementAbstract, ABC):
    def get_string(self):
        return "mock_element"


class DivTest(unittest.TestCase):
    def test_tag_attribute(self):
        div = Div()
        self.assertEqual(div._tag, "div")

    def test_container_attribute(self):
        div = Div()
        self.assertTrue(div.is_container())

    def test_form_element_attribute(self):
        div = Div()
        self.assertFalse(div.is_form_element())

    def test_add_element(self):
        div = Div()
        mock_element = MockElement()
        div.add(mock_element)
        self.assertEqual(div.get_string(), '<div>mock_element</div>')

    def test_generate(self):
        div = Div()
        mock_element = MockElement()
        div.add(mock_element)

        # Redireciona a saída padrão para um objeto StringIO para testar a saída gerada
        captured_output = io.StringIO()
        sys.stdout = captured_output

        div.generate()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        self.assertEqual(output, '<div>mock_element</div>')


if __name__ == '__main__':
    unittest.main()
