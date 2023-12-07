from winged.core.tag import Tag

"""This module defines a class called 'Title' that represents a 'title' HTML-like container element for specifying 
the document's title.

The 'Title' class is a specific implementation of the 'Tag' class and is used to create and manipulate 'title' 
container elements within an HTML-like document. It inherits attributes and methods from the 'Tag' class and 
specializes in handling 'title' elements, which specify the title of the document.

Usage Example:
```python
from winged.core.tag import Tag

# Create a 'Title' instance
title_element = Title()

# Set the text content of the 'Title' element
title_element.add("Page Title")

# Get the string representation of the 'Title' element
title_string = title_element.get_string()

# Generate and print the 'Title' element
title_element.generate()
```

# Class Attributes:

- _tag (str): The name of the tag, which is set to "title" for 'Title' elements. - _container (bool): Indicates that 
'Title' elements are container elements. - _form_element (bool): Indicates that 'Title' elements are not form 
elements, as they represent the title of the document.

# Methods:

- __init__(): Constructor method to initialize a 'Title' instance.
- add(element: ElementAbstract): Set the text content of the 'Title' element.
- get_tag() -> str: Get the name of the tag ("title").
- is_container() -> bool: Check if the 'Title' element is a container.
- is_form_element() -> bool: Check if the 'Title' element is a form element.
- get_string() -> str: Get the string representation of the 'Title' element, including its nested elements and content.
- generate(): Print the string representation of the 'Title' element to the console.

# Note:

- The 'Title' class is a specialization of the 'Tag' class for representing 'title' container elements, which specify 
the title of the document."""


class Title(Tag):
    _tag = "title"
    _container = True
    _form_element = False
