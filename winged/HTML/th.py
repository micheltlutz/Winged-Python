from winged.core.tag import Tag

"""
The TH class is a specific implementation of the HTML 'th' tag in the Winged-Python library.
It inherits from the Tag class and provides the necessary methods to generate 'th' HTML elements.

The 'th' tag defines a header cell in a table.

Features:
- It is a container element and can contain other HTML elements.
- It is not considered a form element.

Example Usage:
    ```
    table_header = TH()
    table_header.add(String("Column Header"))   # Add header text as needed
    ```

This would generate: <th>Column Header</th>

Methods:
- All methods available in the Tag class can be called by TH instances.

Note:
The 'th' tag is used to create a table header cell, which is used to label the column(s) that it spans.
By default, browsers render the content of a 'th' cell in bold and centered.
"""


class Th(Tag):
    _tag = "th"  # Specifies the name of the tag
    _container = True  # Specifies that TH can contain other HTML elements
    _form_element = False  # Specifies that TH is not a form element
