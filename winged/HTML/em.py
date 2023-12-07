from winged.core.tag import Tag

"""
This module defines a class called 'Em' that represents an 'em' HTML-like container element for emphasizing text.

The 'Em' class is a specific implementation of the 'Tag' class and is used to create and manipulate 'em' container 
elements within an HTML-like document. It inherits attributes and methods from the 'Tag' class and specializes in 
handling 'em' elements, which are used to emphasize text by rendering it in italic or with other styling, 
depending on CSS.

# Usage Example:

```python
from winged.core.tag import Tag

# Create an 'Em' instance
em_element = Em()

# Add text content or other elements to emphasize
em_element.add("This is emphasized text.")

# Get the string representation of the 'Em' element
em_string = em_element.get_string()

# Generate and print the 'Em' element
em_element.generate()
```
# Class Attributes:

- _tag (str): The name of the tag, which is set to "em" for 'Em' container elements.
- _container (bool): Indicates that 'Em' elements are container elements.
- _form_element (bool): Indicates that 'Em' elements are not form elements, as they are used for emphasizing text.

# Methods:

- __init__(): Constructor method to initialize an 'Em' instance.
- add(content: str): Add text content or other elements to emphasize within the 'Em' container.
- get_tag() -> str: Get the name of the tag ("em").
- is_container() -> bool: Check if the 'Em' element is a container.
- is_form_element() -> bool: Check if the 'Em' element is a form element (always returns False).
- get_string() -> str: Get the string representation of the 'Em' element, including its emphasized content.
- generate(): Print the string representation of the 'Em' element to the console.

# Note:

- The 'Em' class is a specialization of the 'Tag' class for representing 'em' container elements used to emphasize 
text within an HTML-like document."""


class Em(Tag):
    _tag = "em"
    _container = True
    _form_element = False
