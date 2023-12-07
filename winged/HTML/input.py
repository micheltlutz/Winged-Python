from winged.core.tag import Tag

"""
The Input class is a specific implementation of the HTML 'input' tag in the Winged-Python library,
using 'text' as the type attribute.
It inherits from the Tag class and provides the methods to generate 'input' HTML elements.

The 'input' tag with type 'text' is used to create input fields in a form where the user can enter text.

# Features:
- It is not a container element, thus cannot hold other HTML elements.
- It is considered a form element.

## Example Usage:

```python
input_field = Input(('type', 'text'), ('name', 'username'), ('id', 'user-input'))
```
This would generate: <input type="text" name="username" id="user-input">

Methods:
- All methods available in the Tag class can be called by Input instances.

Note:
The 'input' tag with 'type' attribute 'text' creates text fields in a form.
This tag is a void element, so it doesn't have a closing tag.
"""


class Input(Tag):
    _tag = "input"  # Specifies the name of the tag.
    _container = False  # Specifies that Input tag cannot contain other HTML elements.
    _form_element = True  # Specifies that Input is a form element.
