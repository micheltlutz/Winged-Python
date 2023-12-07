from winged.core.tag import Tag

"""
This module defines a class called 'Center' that represents a 'center' HTML-like container element.

The 'Center' class is a specific implementation of the 'Tag' class and is used to create and manipulate 'center' container elements within an HTML-like document. It inherits attributes and methods from the 'Tag' class and specializes in handling 'center' elements.

# Usage Example:

```python
from winged.core.tag import Tag

# Create a 'Center' instance
center_element = Center()

# Add elements or text content to the 'Center' container
center_element.add(Tag("This content is centered."))

# Get the string representation of the 'Center' element
center_string = center_element.get_string()

# Generate and print the 'Center' element
center_element.generate()
```
# Class Attributes:

-_tag (str): The name of the tag, which is set to "center" for 'Center' elements.
- _container (bool): Indicates that 'Center' elements are container elements.
- _form_element (bool): Indicates that 'Center' elements are not form elements, as they are used for centering content.

# Methods:

- __init__(): Constructor method to initialize a 'Center' instance.
- add(element: ElementAbstract): Add elements or text content to the 'Center' container.
- get_tag() -> str: Get the name of the tag ("center").
- is_container() -> bool: Check if the 'Center' element is a container.
- is_form_element() -> bool: Check if the 'Center' element is a form element.
- get_string() -> str: Get the string representation of the 'Center' element, including its nested elements and content.
- generate(): Print the string representation of the 'Center' element to the console.

# Note:

- The 'Center' class is a specialization of the 'Tag' class for representing 'center' container elements commonly used in HTML for centering content.
"""


class Center(Tag):
    _tag = "center"
    _container = True
    _form_element = False
