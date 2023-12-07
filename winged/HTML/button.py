from winged.core.tag import Tag

"""
This module defines a class called 'Button' that represents a 'button' HTML-like container element.

The 'Button' class is a specific implementation of the 'Tag' class and is used to create and manipulate 'button' elements within an HTML-like document. It inherits attributes and methods from the 'Tag' class and specializes in handling button elements, which are commonly used in HTML forms.

# Usage Example:

```python
from winged.core.tag import Tag

# Create a 'Button' instance
button_element = Button()

# Add text content or other elements to the 'Button'
button_element.add(Tag("Click me"))

# Get the string representation of the 'Button' element
button_string = button_element.get_string()

# Generate and print the 'Button' element
button_element.generate()
```
# Class Attributes:

- _tag (str): The name of the tag, which is set to "button" for 'Button' elements.
- _container (bool): Indicates that 'Button' elements are container elements.
- _form_element (bool): Indicates that 'Button' elements are form elements, as they are used in HTML forms to trigger actions.

# Methods:

- __init__(): Constructor method to initialize a 'Button' instance.
- add(element: ElementAbstract): Add text content or other elements to the 'Button' container.
- get_tag() -> str: Get the name of the tag ("button").
- is_container() -> bool: Check if the 'Button' element is a container.
- is_form_element() -> bool: Check if the 'Button' element is a form element.
- get_string() -> str: Get the string representation of the 'Button' element, including its nested elements and content.
- generate(): Print the string representation of the 'Button' element to the console.

# Note:

- The 'Button' class is a specialization of the 'Tag' class for representing 'button' elements commonly used in HTML forms to trigger actions.
"""


class Button(Tag):
    _tag = "button"
    _container = True
    _form_element = True
