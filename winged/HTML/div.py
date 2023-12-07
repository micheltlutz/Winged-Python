from winged.core.tag import Tag

"""
This module defines a class called 'Div' that represents a 'div' HTML-like container element.

The 'Div' class is a specific implementation of the 'Tag' class and is used to create and manipulate 'div' container elements within an HTML-like document. It inherits the attributes and methods from the 'Tag' class and specializes in handling 'div' elements.

Usage Example:
```python
from winged.core.tag import Tag

# Create a 'Div' instance
div_element = Div()

# Add elements to the 'Div' container
div_element.add(Tag(), Tag(), Tag())

# Get the string representation of the 'Div' container
div_string = div_element.get_string()

# Generate and print the 'Div' container
div_element.generate()
```

# Class Attributes:

- _tag (str): The name of the tag, which is set to "div" for 'Div' elements.
- _container (bool): Indicates that 'Div' elements are container elements.
- _form_element (bool): Indicates that 'Div' elements are not form elements, as they are used for layout and grouping.

# Methods:

- __init__(): Constructor method to initialize a 'Div' instance.
- add(element: ElementAbstract): Add elements to the 'Div' container.
- get_tag() -> str: Get the name of the tag ("div").
- is_container() -> bool: Check if the 'Div' element is a container.
- is_form_element() -> bool: Check if the 'Div' element is a form element.
- get_string() -> str: Get the string representation of the 'Div' container, including its nested elements.
- generate(): Print the string representation of the 'Div' container to the console.

# Note:

- The 'Div' class is a specialization of the 'Tag' class for representing 'div' container elements commonly used in 
HTML for layout purposes.

"""


class Div(Tag):
    _tag = "div"
    _container = True
    _form_element = False
