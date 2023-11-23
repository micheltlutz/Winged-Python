from winged.core.element_abstract import ElementAbstract


class GenericElement(ElementAbstract):
    _elements: [ElementAbstract]

    def __init__(self):
        self._elements = []

    # This method add a new element
    def add(self, element: ElementAbstract):
        self._elements.append(element)

    # This method return tag and all elements
    def get_string(self):
        string = ""

        for element in self._elements:
            string += element.get_string()

        return string

    # This method print tag and all elements
    def generate(self):
        print(self.get_string())
