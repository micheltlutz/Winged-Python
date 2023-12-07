from winged.core.tag import Tag

"""
This module defines a class called 'Meta' that represents a 'meta' HTML-like element for specifying metadata about the document.

The 'Meta' class is a specific implementation of the 'Tag' class and is used to create and manipulate 'meta' elements within an HTML-like document. It specializes in handling 'meta' elements that are used to specify metadata about the document, such as character encoding, viewport settings, and more.

# Usage Example:

```python
from winged.core.tag import Tag

# Create a 'Meta' instance with metadata attributes
meta_element = Meta(AttributeType("charset", "UTF-8"), AttributeType("name", "viewport"))

# Get the string representation of the 'Meta' element
meta_string = meta_element.get_string()

# Generate and print the 'Meta' element
meta_element.generate()
```

# Class Attributes:

- _tag (str): The name of the tag, which is set to "meta" for 'Meta' elements. - _container (bool): Indicates that 
'Meta' elements are not container elements. - _form_element (bool): Indicates that 'Meta' elements are not form 
elements, as they are used to specify metadata about the document.

# Methods:

- __init__(*attributes: AttributeType): Constructor method to initialize a 'Meta' instance with metadata attributes.
- get_tag() -> str: Get the name of the tag ("meta").
- is_container() -> bool: Check if the 'Meta' element is a container.
- is_form_element() -> bool: Check if the 'Meta' element is a form element.
- get_string() -> str: Get the string representation of the 'Meta' element, including its nested elements and content.
- generate(): Print the string representation of the 'Meta' element to the console.

# Note:

- The 'Meta' class is a specialization of the 'Tag' class for representing 'meta' elements that are used to specify 
metadata about the document."""


class Meta(Tag):
    _tag = "meta"
    _container = False
    _form_element = False
