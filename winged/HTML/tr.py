from winged.core.tag import Tag

"""
The TR class is a specific implementation of the HTML 'tr' tag in the Winged-Python library.
It inherits from the Tag class and provides the necessary methods to generate 'tr' HTML elements.

The 'tr' tag defines a row of cells in a table.

Features:
- This is a container and can encapsulate other HTML elements.
- It is not considered a form element.

Example Usage:
    ```
    row = Tr()
    ```

This would generate: <tr></tr>

Methods:
- All methods available in the Tag class can be called by TR instances.

Note:
The 'tr' tag in HTML is used to group together th or td values into a single row of table heading or data values.
The 'tr' tag must be nested inside a 'table' tag or must be be placed between 'thead', 'tbody', or 'tfoot' tags.
"""


class Tr(Tag):
    _tag = "tr"  # Specifies the name of the tag
    _container = True  # Specifies that TR can contain other HTML elements
    _form_element = False  # Specifies that TR is not a form element
