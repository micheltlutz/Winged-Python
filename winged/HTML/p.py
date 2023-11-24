from winged.core.tag import Tag

"""
This module defines a class called 'P' that represents a 'p' HTML-like container element.

The 'P' class is a specific implementation of the 'Tag' class and is used to create and manipulate 'p' paragraph elements within an HTML-like document. It inherits the attributes and methods from the 'Tag' class and specializes in handling 'p' elements.

Usage Example:
```python
from winged.core.tag import Tag

# Create a 'P' instance
paragraph_element = P()

# Add elements to the 'P' container
paragraph_element.add(Tag(), Tag(), Tag())

# Get the string representation of the 'P' container
paragraph_string = paragraph_element.get_string()

# Generate and print the 'P' container
paragraph_element.generate()
```

# Class Attributes:

- _tag (str): The name of the tag, which is set to "p" for 'P' elements.
- _container (bool): Indicates that 'P' elements are container elements.
- _form_element (bool): Indicates that 'P' elements are not form elements, as they are used for text content within paragraphs.

# Methods:

- __init__(): Constructor method to initialize a 'P' instance.
- add(element: ElementAbstract): Add elements to the 'P' container.
- get_tag() -> str: Get the name of the tag ("p").
- is_container() -> bool: Check if the 'P' element is a container.
- is_form_element() -> bool: Check if the 'P' element is a form element.
- get_string() -> str: Get the string representation of the 'P' container, including its nested elements.
- generate(): Print the string representation of the 'P' container to the console.

# Note:

- The 'P' class is a specialization of the 'Tag' class for representing 'p' paragraph elements commonly used in HTML for text content.
"""


class P(Tag):
    _tag = "p"
    _container = True
    _form_element = False
