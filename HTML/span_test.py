import unittest
import io
import sys
from abc import ABC

from HTML.span import Span
from core.element_abstract import ElementAbstract


class MockElement(ElementAbstract, ABC):
    def get_string(self):
        return "mock_element"


class SpanTest(unittest.TestCase):
    def test_tag_attribute(self):
        span = Span()
        self.assertEqual(span.get_tag(), "span")

    def test_container_attribute(self):
        span = Span()
        self.assertTrue(span.is_container())

    def test_form_element_attribute(self):
        span = Span()
        self.assertFalse(span.is_form_element())

    def test_generate(self):
        span = Span()
        mock_element = MockElement()
        span.add(mock_element)

        # Redireciona a saída padrão para um objeto StringIO para testar a saída gerada
        captured_output = io.StringIO()
        sys.stdout = captured_output

        span.generate()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        self.assertEqual(output, '<span>mock_element</span>')

    def test_add_element(self):
        span = Span()
        mock_element = MockElement()
        span.add(mock_element)
        self.assertEqual(span.get_string(), '<span>mock_element</span>')


if __name__ == '__main__':
    unittest.main()
