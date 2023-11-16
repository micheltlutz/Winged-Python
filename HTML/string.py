from core.generic_element import GenericElement

class String(GenericElement):
    _tag = ""
    _container = False
    _form_element = False
    text = ""

    def __init__(self, str):
        self.text = str

    def getString(self):
        return self.text

    def generate(self):
        print(self.getString())