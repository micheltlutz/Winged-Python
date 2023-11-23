from core.generic_element import GenericElement


class String(GenericElement):
    text = ""

    def __init__(self, str):
        super().__init__()
        self.text = str

    def get_string(self):
        return self.text

    def generate(self):
        print(self.get_string())
