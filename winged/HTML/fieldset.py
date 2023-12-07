from winged.core.tag import Tag

"""This module defines a class called 'Fieldset' that represents a 'fieldset' HTML-like container element for 
grouping form controls.

The 'Fieldset' class is a specific implementation of the 'Tag' class and is used to create and manipulate 'fieldset' 
container elements within an HTML-like document. It inherits attributes and methods from the 'Tag' class and 
specializes in handling 'fieldset' elements, which are used for grouping form controls and providing a legend for the 
group.

# Usage Example:

```python
from winged.core.tag import Tag

# Create a 'Fieldset' instance
fieldset_element = Fieldset()

# Add form controls or other elements to the 'Fieldset' container
fieldset_element.add(Label("Name"))
fieldset_element.add(Input(type="text", name="name"))

# Get the string representation of the 'Fieldset' element
fieldset_string = fieldset_element.get_string()

# Generate and print the 'Fieldset' element
fieldset_element.generate()
```

# Class Attributes:

- _tag (str): The name of the tag, which is set to "fieldset" for 'Fieldset' container elements. - _container (bool): 
Indicates that 'Fieldset' elements are container elements. - _form_element (bool): Indicates that 'Fieldset' elements 
are not form elements, as they are used for grouping form controls. # Methods:

- __init__(): Constructor method to initialize a 'Fieldset' instance. - add(element: ElementAbstract): Add form 
controls or other elements to the 'Fieldset' container. - get_tag() -> str: Get the name of the tag ("fieldset"). - 
is_container() -> bool: Check if the 'Fieldset' element is a container. - is_form_element() -> bool: Check if the 
'Fieldset' element is a form element (always returns False). - get_string() -> str: Get the string representation of 
the 'Fieldset' element, including its grouped elements and content. - generate(): Print the string representation of 
the 'Fieldset' element to the console.

# Note:

- The 'Fieldset' class is a specialization of the 'Tag' class for representing 'fieldset' container elements used to 
group form controls and provide a legend for the group. Customize and expand this documentation as necessary to align 
with the specific requirements and structure of your project.
"""


class Fieldset(Tag):
    _tag = "fieldset"
    _container = True
    _form_element = False
