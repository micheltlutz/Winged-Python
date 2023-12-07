from winged.core.tag import Tag

"""
The LI class is a specific implementation of the HTML 'li' tag in the Winged-Python library.
It inherits from the Tag class and provides the necessary methods to generate 'li' HTML elements.

'li' tag is used to define a list item, either ordered or unordered.

Features:
- It is a container element, meaning it can hold other HTML elements.
- It is not considered a form element.

Example Usage:
    ```
    li = LI()   # Create an instance of an LI tag
    li.add(String("List Item")) # Add other HTML elements or text as needed
    ```

This would generate: <li>List Item</li>

Methods:
- All methods available in the Tag class can be called by LI instances.

Note: The 'li' tag is used to define a list item. The list items usually contain a block of text but can also contain 
other HTML elements like images, other lists, etc."""


class Li(Tag):
    _tag = "li"  # Specifies the name of the tag
    _container = True  # Specifies that IL can contain other HTML elements
    _form_element = False  # Specifies that LI is not a form element
