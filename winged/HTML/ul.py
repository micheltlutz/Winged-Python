from winged.core.tag import Tag

"""
The UL class is a specific implementation of the HTML 'ul' tag in the Winged-Python library.
It inherits from the Tag class and provides necessary methods for generating 'ul' tag-based HTML elements.

The 'ul' tag is used for grouping a collection of items which do not have a numerical ordering, often displayed with 
bullet points.

# Features:
- It can act as a container and encapsulate other HTML elements.
- It is not considered a form element.

## Example Usage:

```python
ul = Ul()   # Create an instance of UL
ul.add(Tag()) # Add other HTML elements as needed
```

This results in the following HTML: <ul><tag></tag></ul>

Methods:
The UL class has access to all methods implemented in the Tag base class.

Note:
The 'ul' tag contains 'li' tags, each of which represents one item in the list.
"""


class Ul(Tag):
    _tag = "ul"  # Specifies the name of the tag
    _container = True  # Specifies that UL can encapsulate other HTML elements
    _form_element = False  # Specifies that UL is not a form element
