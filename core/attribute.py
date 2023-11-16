# from attribute_type import AttributeType
from core.attribute_type import AttributeType

class Attribute:
    _attributes: [AttributeType]

    def __init__(self, *attributes: AttributeType):
        self._attributes = []
        for att in attributes:
            self._attributes.append(att)
        

    # This method add a new single attribute
    def addAttribute(self, attribute: AttributeType):
        self._attributes.append(attribute) 

    # This function return all attribures
    def getAttributes(self):
        return self._attributes

    # This method return a `String` with all attributes
    def getString(self):
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
        print(self.getString())