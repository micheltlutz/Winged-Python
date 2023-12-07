from winged.core.tag import Tag

"""
The Hr class represents an HTML 'hr' tag within the Winged-Python framework.
It inherits from the Tag class and modifies the properties to correspond to
those of an 'hr' tag in HTML.

An 'hr' tag in HTML is used for creating a thematic break between paragraph-level elements.

# Features:
- The Hr element isn't a container, meaning it cannot hold other HTML elements.
- The Hr tag is not considered a form element.

## Example usage:

```python
hr = Hr()       # Create an Hr instance
hr.generate()   # Generate the HTML content
```

This will generate: <hr />

Methods:
- All methods from the 'Tag' superclass are available for use with the Hr class.

Note:
The 'hr' tag in HTML doesn't have an end tag. It's used for separating
content at a thematic level, such as a scene change in a story, or a shift of topic within a section.
"""


class Hr(Tag):
    _tag = "hr"  # Specifies the name of the tag.
    _container = False  # Specifies that the Hr tag can't contain other HTML elements.
    _form_element = False  # Specifies that Hr is not a form element.
