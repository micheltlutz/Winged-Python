from winged.core.tag import Tag

"""
This module defines a class called 'Html' that represents an 'html' HTML-like container element.

The 'Html' class is a specific implementation of the 'Tag' class and is used to create and manipulate 'html' container elements within an HTML-like document. It inherits attributes and methods from the 'Tag' class and specializes in handling 'html' elements, which serve as the root element of an HTML document.

# Usage Example:

```python
from winged.core.tag import Tag

# Create an 'Html' instance
html_element = Html()

# Add 'head', 'body', or other elements to the 'Html' container
html_element.add(Head())
html_element.add(Body())

# Get the string representation of the 'Html' element
html_string = html_element.get_string()

# Generate and print the 'Html' element
html_element.generate()
```

# Class Attributes:

- _tag (str): The name of the tag, which is set to "html" for 'Html' elements. - _container (bool): Indicates that 
'Html' elements are container elements. - _form_element (bool): Indicates that 'Html' elements are not form elements, 
as they serve as the root element of an HTML document.

# Methods:

- __init__(): Constructor method to initialize an 'Html' instance.
- add(element: ElementAbstract): Add 'head', 'body', or other elements to the 'Html' container.
- get_tag() -> str: Get the name of the tag ("html").
- is_container() -> bool: Check if the 'Html' element is a container.
- is_form_element() -> bool: Check if the 'Html' element is a form element.
- get_string() -> str: Get the string representation of the 'Html' element, including its nested elements and content.
- generate(): Print the string representation of the 'Html' element to the console.

# Note:

- The 'Html' class is a specialization of the 'Tag' class for representing 'html' container elements, which serve as 
the root element of an HTML document."""


class Html(Tag):
    _tag = "html"
    _container = True
    _form_element = False
