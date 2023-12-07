from winged.core.tag import Tag

"""
This module defines a class called 'Br' that represents a 'br' HTML-like element for line breaks.

The 'Br' class is a specific implementation of the 'Tag' class and is used to create and manipulate 'br' line break elements within an HTML-like document. It inherits attributes and methods from the 'Tag' class and specializes in handling 'br' elements, which are used to create line breaks in HTML.

# Usage Example:

```python
from winged.core.tag import Tag

# Create a 'Br' instance
br_element = Br()

# Get the string representation of the 'Br' element
br_string = br_element.get_string()

# Generate and print the 'Br' element
br_element.generate()
```
# Class Attributes:

- _tag (str): The name of the tag, which is set to "br" for 'Br' elements.
- _container (bool): Indicates that 'Br' elements are not container elements.
- _form_element (bool): Indicates that 'Br' elements are not form elements.

# Methods:

- __init__(): Constructor method to initialize a 'Br' instance.
- get_tag() -> str: Get the name of the tag ("br").
- is_container() -> bool: Check if the 'Br' element is a container (always returns False).
- is_form_element() -> bool: Check if the 'Br' element is a form element (always returns False).
- get_string() -> str: Get the string representation of the 'Br' element, which is an empty self-closing tag.
- generate(): Print the string representation of the 'Br' element to the console.

# Note:

- The 'Br' class is a specialization of the 'Tag' class for representing 'br' elements commonly used in HTML to create line breaks.
"""


class Br(Tag):
    _tag = "br"
    _container = False
    _form_element = False
