from winged.core.tag import Tag

"""
This module defines a class called 'A' that represents an 'a' HTML-like container element for hyperlinks.

The 'A' class is a specific implementation of the 'Tag' class and is used to create and manipulate 'a' hyperlink elements within an HTML-like document. It inherits attributes and methods from the 'Tag' class and specializes in handling hyperlink elements.

# Usage Example:

```python
from winged.core.tag import Tag

# Create an 'A' instance with an 'href' attribute
link_element = A(AttributeType("href", "https://example.com"))

# Add elements or text content to the 'A' hyperlink
link_element.add(Tag("Click me!"))

# Get the string representation of the 'A' hyperlink
link_string = link_element.get_string()

# Generate and print the 'A' hyperlink
link_element.generate()
```

# Class Attributes:

- _tag (str): The name of the tag, which is set to "a" for 'A' elements.
- _container (bool): Indicates that 'A' elements are container elements.
- _form_element (bool): Indicates that 'A' elements are not form elements, as they are used for hyperlinks.

# Methods:

- __init__(): Constructor method to initialize an 'A' instance.
- add(element: ElementAbstract): Add elements or text content to the 'A' hyperlink.
- get_tag() -> str: Get the name of the tag ("a").
- is_container() -> bool: Check if the 'A' element is a container.
- is_form_element() -> bool: Check if the 'A' element is a form element.
- get_string() -> str: Get the string representation of the 'A' hyperlink, including its nested elements and attributes.
- generate(): Print the string representation of the 'A' hyperlink to the console.

# Note:

- The 'A' class is a specialization of the 'Tag' class for representing 'a' hyperlink elements commonly used in HTML for creating hyperlinks to other resources.
"""


class A(Tag):
    _tag = "a"
    _container = True
    _form_element = False
