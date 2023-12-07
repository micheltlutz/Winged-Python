from winged.core.tag import Tag

"""
The I class is a specific implementation of the HTML 'i' tag in the Winged-Python library.
It inherits from the Tag class and provides the necessary methods to generate 'i' HTML elements.

Features:
- It is a container element and can hold other HTML elements.
- It is not considered a form element.

Example Usage:
    ```
    italic_text = I(text="This is an italic text")
    italic_text.generate()  # generates the HTML string
    ```

This would generate: <i>This is an italic text</i>

Methods:
- All methods available in the Tag class can be called by I instances.

Note: The 'i' tag is used in HTML indicate a different quality of text such as a technical term, a phrase from 
another language, a thought, or a ship name in Western texts."""


class I(Tag):
    _tag = "i"  # Specifies the name of the tag.
    _container = True  # Specifies that I tag can contain other HTML elements.
    _form_element = False  # Specifies that I is not a form element.
