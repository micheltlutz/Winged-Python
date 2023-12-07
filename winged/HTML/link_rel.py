from winged.core.tag import Tag

"""
This module defines a class called 'LinkRel' that represents a 'link' HTML-like element for specifying relationships between the current document and an external resource.

The 'LinkRel' class is a specific implementation of the 'Tag' class and is used to create and manipulate 'link' elements within an HTML-like document. It specializes in handling 'link' elements that are used to specify relationships between the current document and external resources, such as stylesheets.

# Usage Example:

```python
from winged.core.tag import Tag

# Create a 'LinkRel' instance with 'rel' and 'href' attributes
link_element = LinkRel(AttributeType("rel", "stylesheet"), AttributeType("href", "styles.css"))

# Get the string representation of the 'LinkRel' element
link_string = link_element.get_string()

# Generate and print the 'LinkRel' element
link_element.generate()
```

# Class Attributes:

- _tag (str): The name of the tag, which is set to "link" for 'LinkRel' elements. - _container (bool): Indicates that 
'LinkRel' elements are not container elements. - _form_element (bool): Indicates that 'LinkRel' elements are not form 
elements, as they are used to specify relationships between the current document and external resources.

# Methods:

- __init__(*attributes: AttributeType): Constructor method to initialize a 'LinkRel' instance with 'rel' and 'href' 
attributes. - get_tag() -> str: Get the name of the tag ("link"). - is_container() -> bool: Check if the 'LinkRel' 
element is a container. - is_form_element() -> bool: Check if the 'LinkRel' element is a form element. - get_string() 
-> str: Get the string representation of the 'LinkRel' element, including its nested elements and content. - 
generate(): Print the string representation of the 'LinkRel' element to the console.

# Note:

- The 'LinkRel' class is a specialization of the 'Tag' class for representing 'link' elements that are used to 
specify relationships between the current document and external resources, such as stylesheets.

"""


class LinkRel(Tag):
    _tag = "link"
    _container = False
    _form_element = False
