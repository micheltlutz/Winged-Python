from winged.core.tag import Tag

"""
This module defines a class called 'Script' that represents a 'script' HTML-like container element for controlling 
and loading JavaScript code.

The 'Script' class is a specific implementation of the 'Tag' class and is used to create and manipulate 'script' 
container elements within an HTML-like document. It inherits attributes and methods from the 'Tag' class and 
specializes in handling 'script' elements, which are used to control and load JavaScript code.

Usage Example:
```python
from winged.core.tag import Tag

# Create a 'Script' instance
script_element = Script()

# Add JavaScript code or external script source to the 'Script' container
script_element.add("console.log('Hello, world!');")

# Get the string representation of the 'Script' element
script_string = script_element.get_string()

# Generate and print the 'Script' element
script_element.generate()
```

# Class Attributes:

- _tag (str): The name of the tag, which is set to "script" for 'Script' container elements. - _container (bool): 
Indicates that 'Script' elements are container elements. - _form_element (bool): Indicates that 'Script' elements are 
not form elements, as they are used for controlling and loading JavaScript code.

# Methods:

- __init__(): Constructor method to initialize a 'Script' instance.
- add(content: str): Add JavaScript code or external script source to the 'Script' container.
- get_tag() -> str: Get the name of the tag ("script").
- is_container() -> bool: Check if the 'Script' element is a container.
- is_form_element() -> bool: Check if the 'Script' element is a form element (always returns False).
- get_string() -> str: Get the string representation of the 'Script' element, including its JavaScript content.
- generate(): Print the string representation of the 'Script' element to the console.

# Note:

- The 'Script' class is a specialization of the 'Tag' class for representing 'script' container elements used for 
controlling and loading JavaScript code in an HTML-like document."""
class Script(Tag):
    _tag = "script"
    _container = True
    _form_element = False
