from winged.core.tag import Tag

"""
The Main class in the Winged-Python library is a specific representation of the 'main' HTML tag.
Inherits from the base 'Tag' class and modifies attributes to conform to HTML 'main' tag specifications.

The 'main' tag is a container element used for encapsulating the primary content of a document. Usually, it includes 
content that is unique to the document and excludes content that is repeated across a set of documents such as site 
navigation links, header or footer information.

Features:
- The Main element is a container and hence can include other HTML elements.
- The Main tag is not considered a form element.

Usage example:
    ```
    main_content = Main()
    main_content.add(Tag()) # Adding other generic HTML elements to the main tag
    ```
This would generate: <main><tag></tag></main>

Methods:
The Main class has access to all methods present in the 'Tag' class.

Note: The 'main' tag, as per HTML5 specifications, must be unique to the document and should exclude content that's 
repeated across a set of documents."""


class Main(Tag):
    _tag = "main"  # Specifies the equivalent HTML tag.
    _container = True  # Specifies that Main tag can contain other HTML elements.
    _form_element = False  # Specifies that Main is not a form element.
