from winged.core.attribute_type import AttributeType
from winged.core.tag import Tag

"""
The H class is a specific representation of the HTML 'h*' tags in the Winged-Python library.
It inherits from the Tag class and provides necessary methods to generate 'h*' HTML elements.

The 'h*' tags indicate headers, where '*' could be any number between 1 and 6 inclusive.
'h1' represents the highest level header and 'h6' the lowest.

Features:
- The H class is a container and can encapsulate other HTML elements.
- It is not a form element.

# Example Usage:

```pyhon
h1 = H('1')    # Create an H instance for 'h1'
h1.add("Header Text")  # Add header text

# Similarly for h2 to h5
h2 = H('2')    # Create an H instance for 'h2'
h2.add(String("Sub Header Text"))    # Add sub header text
...

# Output

```html

This would generate:
<h1>Header Text</h1>
<h2>Sub Header Text</h2>
...

Methods: 
All methods available in the Tag class can be accessed by H instances.

Note:
The 'h*' tag in HTML5 represents headers for a section or subsection. 
The number following the 'h' indicates the depth of the section in the structure of the document. 
"""


class H(Tag):
    def __init__(self, level, *attributes: AttributeType):
        self._tag = f"h{level}"  # Defines the specific header tag name
        super().__init__(*attributes)
        self._container = True  # Specifies that H can contain other elements
        self._form_element = False  # Specifies that H is not a form element
