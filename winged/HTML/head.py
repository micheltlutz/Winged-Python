from winged.core.tag import Tag

"""
This module defines a class called 'Head' that represents a 'head' HTML-like container element.

The 'Head' class is a specific implementation of the 'Tag' class and is used to create and manipulate 'head' container elements within an HTML-like document. It inherits attributes and methods from the 'Tag' class and specializes in handling 'head' elements, which typically contain meta-information about the document.

Usage Example:
```python
from winged.core.tag import Tag

# Create a 'Head' instance
head_element = Head()

# Add meta tags, title, or other elements to the 'Head' container
head_element.add(Tag("This is the document's head."))

# Get the string representation of the 'Head' element
head_string = head_element.get_string()

# Generate and print the 'Head' element
head_element.generate()
```

# Class Attributes:

- _tag (str): The name of the tag, which is set to "head" for 'Head' elements. - _container (bool): Indicates that 
'Head' elements are container elements. - _form_element (bool): Indicates that 'Head' elements are not form elements, 
as they represent meta-information about the document.

# Methods:

- __init__(): Constructor method to initialize a 'Head' instance.
- add(element: ElementAbstract): Add meta tags, title, or other elements to the 'Head' container.
- get_tag() -> str: Get the name of the tag ("head").
- is_container() -> bool: Check if the 'Head' element is a container.
- is_form_element() -> bool: Check if the 'Head' element is a form element.
- get_string() -> str: Get the string representation of the 'Head' element, including its nested elements and content.
- generate(): Print the string representation of the 'Head' element to the console.

# Note:

- The 'Head' class is a specialization of the 'Tag' class for representing 'head' container elements, which typically 
contain meta-information about the document."""


class Head(Tag):
    _tag = "head"
    _container = True
    _form_element = False
