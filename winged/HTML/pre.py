from winged.core.tag import Tag

"""
The Pre class is a unique implementation of the HTML 'pre' tag within the Winged-Python library.
It inherits from the Tag base class and overrides the base class properties to match the HTML 'pre' tag.

The 'pre' tag in HTML represents preformatted text. Text within a 'pre' element is displayed 
in a fixed-width font (usually Courier), and it preserves both spaces and line breaks.

Features:
- This element serves as a container, meaning it can contain other HTML elements.
- It is not a form element.

Example Usage:
    ```
    preformatted_text = Pre(text='    Four spaces\n    are preserved.')
    ```
This will generate: <pre>    Four spaces\n    are preserved.</pre>

Methods:
The Pre class has access to all methods of the 'Tag' class.

Note:
The 'pre' tag in HTML is used to define preformatted text. The text inside a pre element 
is displayed in a fixed-width font (usually Courier), and it preserves both spaces and line breaks.
"""


class Pre(Tag):
    _tag = "pre"  # This attribute specifies the name of the tag.
    _container = True  # This attribute indicates that the Pre tag can contains other elements.
    _form_element = False  # This attribute indicates that Pre is not a form element.
