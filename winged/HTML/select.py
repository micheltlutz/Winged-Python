from winged.core.tag import Tag

"""
The Select class is a specific implementation of the HTML 'select' tag in the Winged-Python library.
It inherits from the Tag class and provides the necessary methods to generate 'select' HTML elements.

The 'select' tag is used to create a drop-down list of options for a form input.

Features:
- It is a container element and can hold other HTML elements.
- It is considered a form element.

Example Usage:
    ```
    option1 = Option(('value', 'option_value1'))
    option1.add(String('Option Text1'))

    option2 = Option(('value', 'option_value2'))
    option2.add(String('Option Text2'))

    select = Select(('name', 'options'))
    select.add(option1)
    select.add(option2)
    ```

This would generate: <select name='options'><option value='option_value1'>Option Text1</option><option 
value='option_value2'>Option Text2</option></select>

Methods:
- All methods available in the Tag class can be called by Select instances.

Note:
The 'select' tag defines a select list within a form. Each option within the select is defined by an 'option' tag.
"""


class Select(Tag):
    _tag = "select"  # Specifies the name of the tag.
    _container = True  # Specifies that Select tag can contain other HTML elements.
    _form_element = True  # Specifies that Select is a form element.
