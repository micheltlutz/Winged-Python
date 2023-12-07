from winged.core.tag import Tag

"""
The DD class is a specific implementation of the HTML 'dd' tag in the Winged-Python library.
It inherits from the Tag class and provides the necessary methods to generate 'dd' HTML elements.

The 'dd' tag is used to provide details for a term named in a 'dt' tag within a description list (dl).

Features:
- The DD class is a container and can contain other HTML elements.
- It is not considered a form element.

# Example Usage:

    ```python
    description = Dd()
    description.add(String("Example Description"))    # Add description as needed
    ```

This would generate: <dd>Example Description</dd>

Methods:
- All methods available in the Tag class can be called by DD instances.

Note:
The 'dd' tag is used in conjunction with 'dl' (The Description List element) and 'dt' tags 
to specify a list of terms and their descriptions.
Each 'dd' tag provides the description for the preceding 'dt' tag.
"""


class Dd(Tag):
    _tag = "dd"  # Specifies the name of the tag
    _container = True  # Specifies that DD can contain other HTML elements
    _form_element = False  # Specifies that DD is not a form element
