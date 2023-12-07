from winged.core.tag import Tag

"""
The DL class is a specific implementation of the HTML 'DL' tag in the Winged-Python library.
It inherits from the Tag class and provides the necessary methods for generating 'DL' HTML elements.

The 'DL' tag is used in description lists (dl), and it is used to name a term to be described in 'dd' tags.

Features:
- This class acts as a container and can contain other HTML elements.
- It is not a form element.

Example Usage:
    ```
    term = DL()
    term.add(String("Example Term")) # Add term as needed
    ```

This would generate: <DL>Example Term</DL>

Methods:
- All methods available in the Tag class can be called by DL instances.

Note:
The 'DL' tag is used in conjunction with 'dl' (The Description List element) and 'dd' tags 
to specify a list of terms and their descriptions.
"""


class Dl(Tag):
    _tag = "dl"  # Specifies the name of the tag
    _container = True  # Specifies that DL can contain other HTML elements
    _form_element = False  # Specifies that DL is not a form element
