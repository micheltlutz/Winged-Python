from winged.core.attribute_type import AttributeType
from winged.core.attribute import Attribute
from winged.core.element_abstract import ElementAbstract

"""
This module defines a class called 'Tag' that represents an HTML-like tag with attributes and elements.

The 'Tag' class extends the 'ElementAbstract' class and is used to create and manipulate HTML-like tags within a document. It allows you to define attributes, add elements, and generate the string representation of the tag.

Usage Example:
```python
from winged.core.attribute_type import AttributeType
from winged.core.attribute import Attribute
from winged.core.element_abstract import ElementAbstract

# Create a 'Tag' instance with attributes and elements
attributes = (AttributeType("class", "container"), AttributeType("id", "example"))
tag = Tag(*attributes)

# Add elements to the 'Tag' instance
tag.add(ElementAbstract())
tag.add(Tag(AttributeType("src", "image.jpg")))

# Get the string representation of the tag
string_representation = tag.get_string()

# Generate and print the tag
tag.generate()
```
# Class Attributes:

- _tag (str): The name of the tag (e.g., 'div', 'a', 'p').
- _attributes (Attribute): An instance of the 'Attribute' class for managing attributes of the tag.
- _container (bool): Indicates whether the tag is a container for other elements.
- _form_element (bool): Indicates whether the tag is a form element.
- _elements (list): A list that stores elements added to the 'Tag' instance.

# Methods:

- __init__(*attributes: AttributeType): Constructor method to initialize the 'Tag' instance with attributes.
- add_attributes(*attributes: AttributeType): Add new attributes to the 'Tag' instance.
- add(element: ElementAbstract): Add a new element to the 'Tag' instance.
- _get_open_tag(): Get the opening tag string with attributes.
- _get_close_tag(): Get the closing tag string.
- get_tag() -> str: Get the name of the tag.
- get_attributes() -> Attribute: Get the attributes of the tag.
- is_container() -> bool: Check if the tag is a container.
- is_form_element() -> bool: Check if the tag is a form element.
- get_string() -> str: Get the complete string representation of the tag, including attributes and nested elements.
- generate(): Print the string representation of the 'Tag' instance to the console.

# Note:

- The 'Tag' class is designed to represent HTML-like tags and elements within a document.
- It supports attributes, nesting of elements, and differentiating between container and form elements.

Customize and expand this documentation as necessary to align with the specific requirements and structure of your project.
"""


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
