from winged.core.tag import Tag

"""
This module defines a class called 'Span' that represents a 'span' HTML-like container element.

The 'Span' class is a specific implementation of the 'Tag' class and is used to create and manipulate 'span' inline container elements within an HTML-like document. It inherits the attributes and methods from the 'Tag' class and specializes in handling 'span' elements.

Usage Example:
```python
from winged.core.tag import Tag

# Create a 'Span' instance
span_element = Span()

# Add elements to the 'Span' container
span_element.add(Tag(), Tag(), Tag())

# Get the string representation of the 'Span' container
span_string = span_element.get_string()

# Generate and print the 'Span' container
span_element.generate()
```

# Class Attributes:

- _tag (str): The name of the tag, which is set to "span" for 'Span' elements.
- _container (bool): Indicates that 'Span' elements are container elements.
- _form_element (bool): Indicates that 'Span' elements are not form elements, as they are used for inline content and styling.

# Methods:

- __init__(): Constructor method to initialize a 'Span' instance.
- add(element: ElementAbstract): Add elements to the 'Span' container.
- get_tag() -> str: Get the name of the tag ("span").
- is_container() -> bool: Check if the 'Span' element is a container.
- is_form_element() -> bool: Check if the 'Span' element is a form element.
- get_string() -> str: Get the string representation of the 'Span' container, including its nested elements.
- generate(): Print the string representation of the 'Span' container to the console.

# Note:

- The 'Span' class is a specialization of the 'Tag' class for representing 'span' inline container elements commonly used in HTML for inline styling and content grouping.
"""


class Span(Tag):
    _tag = "span"
    _container = True
    _form_element = False
