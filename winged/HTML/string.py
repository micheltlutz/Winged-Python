from winged.core.generic_element import GenericElement

"""
This module defines a class called 'String' for representing text strings within a document structure.

The 'String' class is a specific implementation of the 'GenericElement' class and is used to create and manipulate text strings as elements within a document. It inherits attributes and methods from the 'GenericElement' class and specializes in handling text content.

# Usage Example:

```python
from winged.core.generic_element import GenericElement

# Create a 'String' instance with text content
text_element = String("Hello, World!")

# Get the text content as a string
text_content = text_element.get_string()

# Generate and print the text content
text_element.generate()
```

# Class Attributes:

- text (str): The text content represented by the 'String' element.

# Methods:

- __init__(self, str): Constructor method to initialize a 'String' instance with the provided text content.
- get_string() -> str: Get the text content as a string.
- generate(): Print the text content to the console.

# Note:

- The 'String' class is a specialization of the 'GenericElement' class designed for representing text content within a document structure.
"""


class String(GenericElement):
    text = ""

    def __init__(self, str):
        super().__init__()
        self.text = str

    def get_string(self):
        return self.text

    def generate(self):
        print(self.get_string())
