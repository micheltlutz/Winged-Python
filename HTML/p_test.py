import unittest
import io
import sys
from abc import ABC

from HTML.p import P
from core.element_abstract import ElementAbstract


class MockElement(ElementAbstract, ABC):
    def get_string(self):
        return "mock_element"


class PTest(unittest.TestCase):
    def test_tag_attribute(self):
        p = P()
        self.assertEqual(p.get_tag(), "p")

    def test_container_attribute(self):
        p = P()
        self.assertTrue(p.is_container())

    def test_form_element_attribute(self):
        p = P()
        self.assertFalse(p.is_form_element())

    def test_generate(self):
        p = P()
        mock_element = MockElement()
        p.add(mock_element)

        # Redireciona a saída padrão para um objeto StringIO para testar a saída gerada
        captured_output = io.StringIO()
        sys.stdout = captured_output

        p.generate()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        self.assertEqual(output, '<p>mock_element</p>')

    def test_add_element(self):
        p = P()
        mock_element = MockElement()
        p.add(mock_element)
        self.assertEqual(p.get_string(), '<p>mock_element</p>')


if __name__ == '__main__':
    unittest.main()
