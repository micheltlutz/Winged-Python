# from attribute_type import AttributeType
from winged.core.attribute_type import AttributeType


class Attribute:
    _attributes: [AttributeType]

    def __init__(self, *attributes: AttributeType):
        self._attributes = []
        for att in attributes:
            self._attributes.append(att)

    # This method add a new single attribute
    def add_attribute(self, attribute: AttributeType):
        self._attributes.append(attribute)

        # This function return all attribures

    def get_attributes(self):
        return self._attributes

    # This method return a `String` with all attributes
    def get_string(self):
        parts = []

        for attribute in self._attributes:
            # Verificar se o attribute é um par
            if isinstance(attribute, tuple) and len(attribute) == 2:
                key, value = attribute
                if value is not None:
                    parts.append(f"{key}=\"{value}\"")
                else:
                    parts.append(f"{key}")
            else:
                parts.append(f"{attribute}")

        return " ".join(parts)

    # This method print all attributes
    def generate(self):
        print(self.get_string())
