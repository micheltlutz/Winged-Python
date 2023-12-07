from winged.core.tag import Tag

"""The Nav class is a specialized implementation of the HTML 'nav' tag using the structure provided by the 
Winged-Python library. The Nav class inherits from the Tag base class and customizes for 'nav' tag specifics.

The 'nav' tag in HTML5 represents a section of navigation links. 

Features:
- Can act as a container for other HTML elements.
- Does not serve as a form element.

Sample usage:
    ```
    navigation = Nav()   # Create an instance of Nav
    navigation.add(Tag()) # Add other HTML elements as needed
    ```
This results in the following HTML: <nav><tag></tag></nav>

Methods: 
The Nav class has access to all methods implemented in the Tag base class.

Note:
The 'nav' element is a way to help users locate themselves on the site, 
but does not help with the accessibility of other sections of a page.
"""


class Nav(Tag):
    _tag = "nav"  # Specifies the name of the tag.
    _container = True  # Specifies that Nav can contain inner elements.
    _form_element = False  # Specifies that Nav is not a form element.
