from winged.core.tag import Tag

"""
This module defines a class called 'Doctype' that represents a '<!DOCTYPE html>' declaration in an HTML-like document.

The 'Doctype' class is a specific implementation of the 'Tag' class and is used to create and manipulate the '<!DOCTYPE html>' declaration, which specifies the document type and version of an HTML document. It inherits attributes and methods from the 'Tag' class and specializes in handling the document type declaration.

# Usage Example:

```python
from winged.core.tag import Tag

# Create a 'Doctype' instance (no need for parameters)
doctype_declaration = Doctype()

# Get the string representation of the '<!DOCTYPE html>' declaration
doctype_string = doctype_declaration.get_string()

# Print the '<!DOCTYPE html>' declaration
print(doctype_string)
```

# Class Attributes:

- _tag (str): The fixed value of "<!DOCTYPE html>" for 'Doctype' elements. - _container (bool): Indicates that 
'Doctype' elements are not container elements. - _form_element (bool): Indicates that 'Doctype' elements are not form 
elements, as they are not part of the document content.

# Methods:

- __init__(): Constructor method to initialize a 'Doctype' instance (no parameters required).
- get_tag() -> str: Get the fixed value of "<!DOCTYPE html>" as the tag.
- is_container() -> bool: Check if the 'Doctype' element is a container (always returns False).
- is_form_element() -> bool: Check if the 'Doctype' element is a form element (always returns False).
- get_string() -> str: Get the string representation of the '<!DOCTYPE html>' declaration ("<!DOCTYPE html>").
- generate(): Print the '<!DOCTYPE html>' declaration to the console.

# Note:

- The 'Doctype' class is a specialization of the 'Tag' class for representing the '<!DOCTYPE html>' declaration in an 
HTML-like document."""


class Doctype(Tag):
    _tag = "<!DOCTYPE html>"
    _container = False
    _form_element = False

    def get_string(self):
        return self._tag
