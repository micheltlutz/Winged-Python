from winged.core.tag import Tag

"""
 The Footer class is a specific implementation of the HTML 'footer' tag in the Winged-Python library.
 It inherits from the Tag class and provides the methods to generate HTML footer elements.

 Features:
 - It can hold other HTML elements as it is a container element.
 - It is not a form element.

 Example Usage:
    ```
    footer = Footer()
    footer.add(Tag())  # adding another generic tag inside the footer
    footer.generate()  # generates the HTML string
    ```
 This will generate: <footer><tag></tag></footer>

 # Methods
 The Footer class has access to all methods present in the 'Tag' class.

 Note: 
 The 'footer' tag is used to define a footer for a document or a section. 
 It typically contains authorship information, copyright data, contact info, and more.
"""


class Footer(Tag):
    _tag = "footer"  # the name of the tag
    _container = True  # specifies that it can hold other HTML elements
    _form_element = False  # specifies that this is not a form element
