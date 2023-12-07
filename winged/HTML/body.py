from winged.core.tag import Tag

"""
This module defines a class called 'Body' that represents a 'body' HTML-like container element.

The 'Body' class is a specific implementation of the 'Tag' class and is used to create and manipulate 'body' container elements within an HTML-like document. It inherits attributes and methods from the 'Tag' class and specializes in handling 'body' elements, which represent the main content of an HTML document.

Usage Example:
```python
from winged.core.tag import Tag

# Create a 'Body' instance
body_element = Body()

# Add elements, text content, or other tags to the 'Body' container
body_element.add(Tag("This is the main content."))

# Get the string representation of the 'Body' element
body_string = body_element.get_string()

# Generate and print the 'Body' element
body_element.generate()
```
# Class Attributes:

- _tag (str): The name of the tag, which is set to "body" for 'Body' elements.
- _container (bool): Indicates that 'Body' elements are container elements.
- _form_element (bool): Indicates that 'Body' elements are not form elements, as they represent the main content of an HTML document.

# Methods:

- __init__(): Constructor method to initialize a 'Body' instance.
- add(element: ElementAbstract): Add elements, text content, or other tags to the 'Body' container.
- get_tag() -> str: Get the name of the tag ("body").
- is_container() -> bool: Check if the 'Body' element is a container.
- is_form_element() -> bool: Check if the 'Body' element is a form element.
- get_string() -> str: Get the string representation of the 'Body' element, including its nested elements and content.
- generate(): Print the string representation of the 'Body' element to the console.

# Note:

- The 'Body' class is a specialization of the 'Tag' class for representing 'body' container elements, which typically contain the main content of an HTML document.
"""


class Body(Tag):
    _tag = "body"
    _container = True
    _form_element = False
