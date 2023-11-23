import unittest
import io
import sys
from winged.core.attribute import Attribute


class TestAttribute(unittest.TestCase):

    def test_init(self):
        # Testar a inicialização com atributos
        attribute = Attribute(('key1', 'value1'), ('key2', 'value2'))
        self.assertEqual(attribute.get_attributes(), [('key1', 'value1'), ('key2', 'value2')])

    def test_addAttribute(self):
        # Testar a adição de um atributo
        attribute = Attribute()
        attribute.add_attribute(('key', 'value'))
        self.assertIn(('key', 'value'), attribute.get_attributes())

    def test_getAttributes(self):
        # Testar a obtenção dos atributos
        attribute = Attribute(('key1', 'value1'), ('key2', 'value2'))
        self.assertEqual(attribute.get_attributes(), [('key1', 'value1'), ('key2', 'value2')])

    def test_getString(self):
        # Testar a formatação da string dos atributos
        attribute = Attribute(('key1', 'value1'), ('key2', 'value2'))
        expected_string = 'key1="value1" key2="value2"'
        self.assertEqual(attribute.get_string(), expected_string)

    def test_generate(self):
        attr = Attribute(("id", "123"), ("name", "test"))

        # Redireciona a saída padrão para um StringIO
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Chama o método generate
        attr.generate()

        # Redefine a saída padrão para o valor padrão
        sys.stdout = sys.__stdout__

        # Obtém o valor do StringIO
        output = captured_output.getvalue().strip()

        # Verifica se a saída é o que você espera
        self.assertEqual(output, 'id="123" name="test"')


if __name__ == '__main__':
    unittest.main()
