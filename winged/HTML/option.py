from winged.core.tag import Tag

"""
The Option class in the Winged-Python library corresponds to the HTML 'option' tag.
It inherits attributes and methods from the Tag base class and modifies some properties to align 
with the HTML 'option' tag semantics.

The 'option' HTML tag defines an option in a select list.

# Features:
- The Option class is a container that can encapsulate other HTML elements.
- It is considered a form element.

## Example Usage:

```python
option = Option(('value', 'option_value'))
option.add(String('Option Text'))
```

This generates the following HTML: <option value="option_value">Option Text</option>

Methods: 
The Option class has access to all methods of the Tag base class.

Note:
The 'option' HTML tag is used to specify items within a 'select', 'optgroup', or 'datalist' element.
Users will see the content of the 'option' tag (Option Text in the example), but the value of the 'value' attribute 
is what gets sent in the form data.
"""


class Option(Tag):
    _tag = "option"  # Specifies the HTML equivalent tag
    _container = True  # Specifies that Option tags can contain other HTML elements
    _form_element = True  # Specifies that Option is a form element
