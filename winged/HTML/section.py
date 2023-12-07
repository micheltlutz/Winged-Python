from winged.core.tag import Tag

"""
The Section class is a specific implementation of the HTML 'section' tag in the Winged-Python library.
It inherits from the Tag class and provides the necessary methods to generate 'section' HTML elements.

The 'section' tag defines sections in a document, such as chapters, headers, footers, or any other sections of the 
document.

# Features:
- It is a container element, meaning it can hold other HTML elements.
- It is not considered a form element.

## Example Usage:

```python
section = Section()
section.add(Tag())  # Adding other generic HTML elements to the section
```

This would generate: <section><tag></tag></section>

Methods:
- All methods available in the Tag class can be called by Section instances.

Note:
The 'section' tag is a block-level element in HTML, and it is a semantic element that specifies the 
content inside is grouped (forms one single thematic group) and is related to the single high-level concept.
"""


class Section(Tag):
    _tag = "section"  # Specifies the name of the tag.
    _container = True  # Specifies that Section tag can contain other HTML elements.
    _form_element = False  # Specifies that Section is not a form element.
