from winged.core.attribute_type import AttributeType
from winged.core.attribute import Attribute
from winged.core.element_abstract import ElementAbstract


class Tag(ElementAbstract):
    _tag: str = ""
    _attributes: Attribute
    _container: bool = False
    _form_element: bool = False
    _elements: [ElementAbstract]

    def __init__(self, *attributes: AttributeType):
        self._attributes = Attribute()
        self._elements = []

        for att in attributes:
            self._attributes.add_attribute(att)

    # This method add a new n attributes
    def add_attributes(self, *attributes: AttributeType):
        for att in attributes:
            self._attributes.add_attribute(att)

    # This method add a new element
    def add(self, element: ElementAbstract):
        self._elements.append(element)

    # This method return open tag and all attributes
    def _get_open_tag(self):
        attr = self._attributes.get_string()

        if len(attr) > 0:
            return f"<{self._tag} {attr}>"
        else:
            return f"<{self._tag}>"

    # This method return close tag
    def _get_close_tag(self):
        return f"</{self._tag}>"

    def get_tag(self):
        return self._tag

    def get_attributes(self):
        return self._attributes

    def is_container(self):
        return self._container

    def is_form_element(self):
        return self._form_element

    # This method return tag and all elements
    def get_string(self):
        string = self._get_open_tag()

        if self._container:
            for element in self._elements:
                string += element.get_string()
            string += self._get_close_tag()
        return string

    # This method print tag and all elements
    def generate(self):
        print(self.get_string())
