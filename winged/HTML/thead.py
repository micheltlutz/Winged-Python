from winged.core.tag import Tag

"""
The THead class is a specific implementation of the HTML 'thead' tag in the Winged-Python library.
It inherits from the Tag class and provides the necessary methods to generate 'thead' HTML elements.

The 'thead' tag is used to group the header content in an HTML table.

# Features:
- THead is a container and can encapsulate other HTML elements.
- It is not a form element.

## Example Usage:

```python
thead = THead()    # Create an instance of 'thead' 
thead.add(Tag()) # Add rows (tr elements) to the thead tag
```

This would generate: <thead><tag></tag></thead>

Methods:
- All methods available in the Tag class can be called by THead instances.

Note:
The 'thead' HTML tag is used for grouping the header content in a table. 
The 'thead' element is useful when dealing with large tables. 
If the table is taller than the viewport, the page will scroll, but the 'thead' section will remain visible.
"""


class THead(Tag):
    _tag = "thead"  # Specifies the name of the tag
    _container = True  # Specifies that THead can contain other HTML elements
    _form_element = False  # Specifies that THead is not a form element
