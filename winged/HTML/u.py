from winged.core.tag import Tag

"""
The U class is a specific implementation of the HTML 'u' tag in the Winged-Python library.
It inherits from the Tag class and provides the necessary methods to generate 'u' HTML elements.

The 'u' tag represents an unarticulated annotation in the text, typically styled as underlined text.

# Features:
- It is a container element, meaning it can hold other HTML elements.
- It is not considered a form element.

## Example Usage:

```python
underlined_text = U()
underlined_text.add(String('This is underlined text'))  # Adding a string to the U tag
```

This would generate: <u>This is underlined text</u>

Methods:
- All methods available in the Tag class can be called by U instances.

Note: The 'u' tag in HTML is used to define text that should be stylistically different from normal text, 
such as misspelled words or proper nouns in Chinese."""


class U(Tag):
    _tag = "u"  # Specifies the name of the tag.
    _container = True  # Specifies that U tag can contain other HTML elements.
    _form_element = False  # Specifies that U is not a form element.
