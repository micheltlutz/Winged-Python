from winged.core.tag import Tag

"""
The Img class is a particular implementation of the HTML 'img' tag in the Winged-Python library.
It inherits from the Tag class and provides the necessary methods to generate 'img' HTML elements.

Features:
- It is not a container element, thus cannot hold other HTML elements.
- It is not considered a form element.

Example Usage:
    ```
    img = Img(attributes={'src': 'image.png', 'alt': 'An example image'}) 
    img.generate()  # generates the HTML string
    ```

This would generate: <img src="image.png" alt="An example image" />

Methods:
- All methods available in the Tag class can be called by Img instances.

Notes: The 'img' tag is used in HTML to embed images in the webpage. It requires the 'src' attribute specifying the 
source file of the image and other optional attributes like 'alt', 'width', 'height' and so on."""


class Img(Tag):
    _tag = "img"  # Specifies the name of the tag.
    _container = False  # Specifies that Img tag cannot contain other HTML elements.
    _form_element = False  # Specifies that Img is not a form element.
