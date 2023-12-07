from winged.core.tag import Tag

"""
This module defines a class called 'Blockquote' that represents a 'blockquote' HTML-like container element for block quotations.

The 'Blockquote' class is a specific implementation of the 'Tag' class and is used to create and manipulate 'blockquote' block quotation elements within an HTML-like document. It inherits attributes and methods from the 'Tag' class and specializes in handling blockquote elements.

# Usage Example:

```python
from winged.core.tag import Tag

# Create a 'Blockquote' instance
blockquote_element = Blockquote()

# Add text content or other elements to the 'Blockquote'
blockquote_element.add(Tag("This is a block quotation."))

# Get the string representation of the 'Blockquote' element
blockquote_string = blockquote_element.get_string()

# Generate and print the 'Blockquote' element
blockquote_element.generate()
```

"""


class Blockquote(Tag):
    _tag = "blockquote"
    _container = True
    _form_element = False
