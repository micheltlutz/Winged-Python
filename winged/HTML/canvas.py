from winged.core.tag import Tag

"""
This module defines a class called 'Canvas' that represents a 'canvas' HTML-like container element for graphics.

The 'Canvas' class is a specific implementation of the 'Tag' class and is used to create and manipulate 'canvas' elements within an HTML-like document. It inherits attributes and methods from the 'Tag' class and specializes in handling canvas elements, which are commonly used for drawing graphics in HTML5.

# Usage Example:

```python
from winged.core.tag import Tag

# Create a 'Canvas' instance
canvas_element = Canvas()

# Add graphic content or other elements to the 'Canvas'
canvas_element.add(Tag("Graphic content"))

# Get the string representation of the 'Canvas' element
canvas_string = canvas_element.get_string()

# Generate and print the 'Canvas' element
canvas_element.generate()
```

# Class Attributes:

- _tag (str): The name of the tag, which is set to "canvas" for 'Canvas' elements.
- _container (bool): Indicates that 'Canvas' elements are container elements.
- _form_element (bool): Indicates that 'Canvas' elements are not form elements, as they are used for drawing graphics.

# Methods:

- __init__(): Constructor method to initialize a 'Canvas' instance.
- add(element: ElementAbstract): Add graphic content or other elements to the 'Canvas' container.
- get_tag() -> str: Get the name of the tag ("canvas").
- is_container() -> bool: Check if the 'Canvas' element is a container.
- is_form_element() -> bool: Check if the 'Canvas' element is a form element.
- get_string() -> str: Get the string representation of the 'Canvas' element, including its nested elements and content.
- generate(): Print the string representation of the 'Canvas' element to the console.

# Note:

- The 'Canvas' class is a specialization of the 'Tag' class for representing 'canvas' elements commonly used in HTML5 for drawing graphics.
"""

class Canvas(Tag):
    _tag = "canvas"
    _container = True
    _form_element = False