from core.attribute_type import AttributeType
from core.attribute import Attribute
from core.element_abstract import ElementAbstract

# from attribute_type import AttributeType
# from attribute import Attribute
# from element_abstract import ElementAbstract

from typing import Tuple

from pprint import pprint

class GenericElement(ElementAbstract):
    _tag: str = ""
    _attributes: Attribute
    _container: bool = False
    _form_element: bool = False
    _elements: [ElementAbstract]

    def __init__(self, *attributes: AttributeType):
        self._attributes = Attribute()
        self._elements = []

        for att in attributes:
            self._attributes.addAttribute(att)

    # This method add a new n attributes
    def addAttributes(self, *attributes: AttributeType):
        for att in attributes:
            self._attributes.addAttribute(att)

    # This method add a new element
    def addElement(self, element: ElementAbstract):
        self._elements.append(element)

    # This method return open tag and all attributes
    def getOpenTag(self):
        attr = self._attributes.getString()

        if len(attr) > 0:
            return f"<{self._tag} {attr}>"
        else:
            return f"<{self._tag}>"

    # This method return close tag
    def getCloseTag(self):
        return f"</{self._tag}>"

    def getTag(self):
        return self._tag

    def getAttributes(self):
        return self._attributes

    # This method return tag and all elements
    def getString(self):
        string = self.getOpenTag()

        if self._container:
            for element in self._elements:
                string += element.getString()
            string += self.getCloseTag()
        return string

    # This method print tag and all elements
    def generate(self):
        print(self.getString())