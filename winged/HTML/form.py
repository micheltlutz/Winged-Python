from winged.core.tag import Tag

"""
The Form class represents an HTML 'form' tag. It inherits from the Tag class and override its attributes
to comply with HTML 'form' tag specifications. This element is a container and can hold other HTML elements.

## Typical usage example:
```python
# Instantiate a Form object:
form = Form()

# Add other tags or content:
form.add(Tag()) # Adding a generic Tag as an example

# Generate the HTML code:
form.generate()
```
This will generate the following HTML: <form><tag></tag></form>
"""


class Form(Tag):
    _tag = "form"  # Specifies the name of the tag.
    _container = True  # Specifies that Form is a container tag.
    _form_element = True  # Specifies that Form is a form element.
