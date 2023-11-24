from winged.core.element_abstract import ElementAbstract

"""
This module defines a class called 'GenericElement' that represents a generic element in a data structure.

The 'GenericElement' class is intended to be used as a part of a more complex data structure. It extends the 'ElementAbstract' class and provides methods for adding elements and generating a string representation of its content.

Usage Example:
```python
from winged.core.element_abstract import ElementAbstract

# Create instances of GenericElement
element1 = GenericElement()
element2 = GenericElement()

# Add elements to the GenericElement instances
element1.add(element2)
element1.add(ElementAbstract())

# Get the string representation of the elements
string_representation = element1.get_string()

# Generate and print the string representation
element1.generate()
```

# Class Attributes:

- _elements (list): A list that stores the elements added to the 'GenericElement' instance.

# Methods:

- __init__(self): Constructor method to initialize the 'GenericElement' instance with an empty list of elements.
- add(element: ElementAbstract): Add a new element to the 'GenericElement' instance.
- get_string(self) -> str: Get a concatenated string representation of all elements within the 'GenericElement' instance.
- generate(self): Print the string representation of the 'GenericElement' instance to the console.

# Note:

- The 'GenericElement' class extends 'ElementAbstract' and inherits the abstract methods 'get_string' and 'generate'. It provides concrete implementations for these methods.
- You can create more specialized subclasses of 'GenericElement' to represent specific elements within your data structure.
"""


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
