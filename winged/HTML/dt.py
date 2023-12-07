from winged.core.tag import Tag

"""
The DT class is a specific implementation of the HTML 'dt' tag in the Winged-Python library.
It inherits from the Tag class and provides the necessary methods for generating 'dt' HTML elements.

The 'dt' tag is used in description lists (dl), and it is used to name a term to be described in 'dd' tags.

# Features:
- This class acts as a container and can contain other HTML elements.
- It is not a form element.

## Example Usage:

    ```python
    term = Dt()
    term.add(String("Example Term")) # Add term as needed
    ```

This would generate: <dt>Example Term</dt>

Methods:
- All methods available in the Tag class can be called by DT instances.

Note:
The 'dt' tag is used in conjunction with 'dl' (The Description List element) and 'dd' tags 
to specify a list of terms and their descriptions.
"""


class Dt(Tag):
    _tag = "dt"  # Specifies the name of the tag
    _container = True  # Specifies that DT can contain other HTML elements
    _form_element = False  # Specifies that DT is not a form element
