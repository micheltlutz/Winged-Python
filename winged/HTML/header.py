from winged.core.tag import Tag

"""
The Header class in Winged-Python is a representation of the HTML 'header' tag.
It is a derivation of the Tag class with additional specifications
to match the behavior and attributes of the HTML 'header' tag.

Features:
- Header is a container element, meaning it can envelop other HTML elements.
- Header is not a form element.

Example Usage:
    ```
    header = Header()        # Create a Header instance
    header.add(Tag())        # Add elements to the Header container
    header.generate()        # Generate the HTML output
    ```
This will output: <header><tag></tag></header>

Available methods:
The Header class has access to all methods of the 'Tag' class.

Note: 
The 'header' tag represents a container for introductory content 
or a set of navigational links. It may contain some heading elements 
but also other kinds of content, including logos, search forms, and so on.
"""


class Header(Tag):
    _tag = "header"  # This specifies the name of the tag
    _container = True  # This specifies that Header can contain other elements
    _form_element = False  # This specifies that Header is not a form element
