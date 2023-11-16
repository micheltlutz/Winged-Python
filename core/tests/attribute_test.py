import unittest
from attribute import Attribute  # Ajuste o caminho de importação conforme necessário

class TestAttribute(unittest.TestCase):

    def test_init(self):
        # Testar a inicialização com atributos
        attribute = Attribute(('key1', 'value1'), ('key2', 'value2'))
        self.assertEqual(attribute.getAttributes(), (('key1', 'value1'), ('key2', 'value2')))

    def test_addAttribute(self):
        # Testar a adição de um atributo
        attribute = Attribute()
        attribute.addAttribute(('key', 'value'))
        self.assertIn(('key', 'value'), attribute.getAttributes())

    def test_getAttributes(self):
        # Testar a obtenção dos atributos
        attribute = Attribute(('key1', 'value1'), ('key2', 'value2'))
        self.assertEqual(attribute.getAttributes(), (('key1', 'value1'), ('key2', 'value2')))

    def test_getString(self):
        # Testar a formatação da string dos atributos
        attribute = Attribute(('key1', 'value1'), ('key2', 'value2'))
        expected_string = 'key1="value1" key2="value2" '
        self.assertEqual(attribute.getString(), expected_string)

    def test_generate(self):
        # Testar o método generate
        # Este teste é mais complicado pois envolve a captura da saída do console.
        # Pode ser deixado para mais tarde ou implementado usando io.StringIO para capturar saídas do print.

if __name__ == '__main__':
    unittest.main()
