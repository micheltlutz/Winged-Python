from winged.core.tag import Tag

"""
The Textarea class is a specific implementation of the HTML 'textarea' tag in the Winged-Python library.
It inherits from the Tag class and provides the necessary methods to generate 'textarea' HTML elements.

A 'textarea' tag defines a multi-line text input control for a form.

Features:
- It is a container element and can encapsulate other HTML elements.
- It is considered a form element.

Example Usage:
    ```
    textarea = Textarea(('name', 'message'), ('rows', '4'), ('cols', '50'))
    ```

This would generate: <textarea name="message" rows="4" cols="50"></textarea>

Methods: 
All methods in the Tag superclass are available to instances of the Textarea class.

Note: The 'textarea' tag in HTML defines a multiline input field, i.e., a control that allows the user to input text 
over multiple rows."""


class Textarea(Tag):
    _tag = "textarea"  # Specifies the tag name.
    _container = True  # Specifies that Textarea can container other elements.
    _form_element = True  # Specifies that Textarea is a form element.
