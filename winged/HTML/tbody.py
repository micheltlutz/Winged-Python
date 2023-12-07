from winged.core.tag import Tag

"""
The TBody class is a specific implementation of the HTML 'tbody' tag in the Winged-Python library.
It inherits from the Tag class and provides the necessary methods to generate 'tbody' HTML elements.

The 'tbody' tag is used to group the body content in an HTML table.

# Features:
- TBody is a container and can encapsulate other HTML elements.
- It is not a form element.

## Example Usage:

```python
tbody = TBody()    # Create an instance of 'tbody' 
tbody.add(Tag()) # Add rows (tr elements) to the tbody tag
```

This would generate: <tbody><tag></tag></tbody>

Methods:
- All methods available in the Tag class can be called by TBody instances.

Note:
The 'tbody' HTML tag is used for grouping the body content in a table. The tbody element is long, 
thereby helping the user agent to incrementally render the table. 
However, collapsing borders and scrolling of the table are not affected by this division.
"""


class TBody(Tag):
    _tag = "tbody"  # Specifies the name of the tag
    _container = True  # Specifies that TBody can contain other HTML elements
    _form_element = False  # Specifies that TBody is not a form element
