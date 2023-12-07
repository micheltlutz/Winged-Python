from winged.core.tag import Tag

"""
The OL class is a specific implementation of the HTML 'ol' tag in the Winged-Python library.
It inherits from the Tag class and provides necessary methods to generate 'ol' tag-based HTML elements.

The 'ol' tag is used for grouping a collection of items which have a numerical ordering, often displayed with numbers.

# Features:
- It can act as a container and encapsulate other HTML elements.
- It is not considered a form element.


## Example Usage:

```python
ol = Ol()   # Create an instance of OL
ol.add(Tag()) # Add other HTML elements as needed
```

This results in the following HTML: <ol><tag></tag></ol>

Methods:
The OL class has access to all methods implemented in the Tag base class.

Note:
The 'ol' tag contains 'li' tags, each of which represents one item in the list.
"""


class Ol(Tag):
    _tag = "ol"  # Specifies the name of the tag
    _container = True  # Specifies that OL can encapsulate other HTML elements
    _form_element = False  # Specifies that OL is not a form element
