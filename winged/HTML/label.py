from winged.core.tag import Tag

"""
The Label class is a specific implementation of the HTML 'label' tag in the Winged-Python library.
It inherits from the Tag class and provides the necessary methods to generate 'label' HTML elements.

# Features:
- It is a container element and can hold other HTML elements.
- It is not considered a form element.

## Example Usage:

```python
label = Label(attributes={'for': 'input_id'}, text='Input Label')
label.generate()  # generates the HTML string
```

This would generate: <label for="input_id">Input Label</label>

Methods:
- All methods available in the Tag class can be called by Label instances.

Note:
The 'label' tag defines a label for several elements: input, meter, progress, select, textarea.
The 'for' attribute of the <label> tag should be equal to the id attribute of the related element to bind them together.
"""


class Label(Tag):
    _tag = "label"  # Specifies the name of the tag.
    _container = True  # Specifies that Label tag can contain other HTML elements.
    _form_element = False  # Specifies that Label is not a form element.
