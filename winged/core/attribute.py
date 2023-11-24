from winged.core.attribute_type import AttributeType

"""
This module defines a Python class called 'Attribute' used for managing attributes.

The 'Attribute' class allows you to create and manage a collection of attributes. It is particularly useful for representing and manipulating attribute data within your code.

Usage Example:
```python
from winged.core.attribute_type import AttributeType

# Create an 'Attribute' instance with attributes
attribute1 = ("name", "John")
attribute2 = ("age", 30)
attr = Attribute(attribute1, attribute2)

# Add a new single attribute
attr.add_attribute(("city", "New York"))

# Get all attributes as a list
all_attributes = attr.get_attributes()

# Get attributes as a formatted string
formatted_string = attr.get_string()

# Print all attributes
attr.generate()

Class Attributes:

- _attributes (list): A list that stores the attributes added to the 'Attribute' instance.
Methods:

- __init__(*attributes: AttributeType): Constructor method to initialize the 'Attribute' instance with the provided attributes.
- add_attribute(attribute: AttributeType): Add a new single attribute to the 'Attribute' instance.
- get_attributes() -> list: Get all attributes as a list.
- get_string() -> str: Get a formatted string representation of all attributes.
- generate(): Print all attributes to the console.

# Note:

- The 'Attribute' class uses the 'AttributeType' type from the 'winged.core.attribute_type' module for attribute typing.
- Attributes can be of various types, including strings, integers, or tuples of (key, value) pairs.

Make sure to import the necessary modules and use the 'Attribute' class according to your requirements.
"""


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
