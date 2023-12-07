from winged.core.tag import Tag

"""
The Strong class is a specific representation of the HTML 'strong' tag in the Winged-Python library.
It inherits from the Tag class and provides the necessary methods to generate 'strong' HTML elements.

The 'strong' tag is used to specify text with strong importance, and the contained text is typically displayed in bold.

# Features:
- It is a container element and can hold other HTML elements.
- It is not considered a form element.

## Example Usage:

```python
important_text = Strong()
important_text.add(String("This is important text"))  # Adding a string to the strong tag
```

This would generate: <strong>This is important text</strong>

Methods:
- All methods available in the Tag class can be called by Strong instances.

Note:
The 'strong' tag in HTML5 gives text strong importance which is typically displayed in bold. 
Use the 'strong' element to denote text with stern importance.
"""


class Strong(Tag):
    _tag = "strong"  # Specifies the name of the tag.
    _container = True  # Specifies that Strong tag can contain other HTML elements.
    _form_element = False  # Specifies that Strong is not a form element.
