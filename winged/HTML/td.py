from winged.core.tag import Tag

"""
The TD class is a specific implementation of the HTML 'td' tag in the Winged-Python library.
It inherits from the Tag class and provides the necessary methods to generate 'td' HTML elements.

'dt' tags define a standard cell in an HTML table.

Features:
- It can act as a container and encapsulate other HTML elements.
- It is not considered a form element.

Example Usage:
    ```
    cell = TD()
    cell.add(String("Cell Text"))  # Add text or other HTML elements as necessary
    ```

This would generate: <td>Cell Text</td>

Methods:
- All methods available in the Tag class can be called by TD instances.

Note:
'td' tags must be nested within 'tr' tags. Text within 'td' tag will by default, be regular and left-aligned.
"""


class Td(Tag):
    _tag = "td"  # Specifies the name of the tag
    _container = True  # Specifies that TD can encapsulate other HTML elements
    _form_element = False  # Specifies that TD is not a form element
