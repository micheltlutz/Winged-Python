from typing import Tuple, Optional

"""
This file contains the definition of the 'AttributeType' data type.

An 'AttributeType' is a tuple that represents an attribute with two elements:
1. A string describing the name of the attribute.
2. An optional string that can contain additional description of the attribute.

Usage Example:
attribute: AttributeType = ("name", "This is an optional description.")

The first element of the tuple ('str') is mandatory, while the second element ('Optional[str]') is optional and can 
be null (None) if there is no description available.

This is useful for documenting and typing attributes within data structures in a more informative and readable manner.

Important:
Ensure that you import 'AttributeType' when using it in your modules to avoid type errors.

Example Import:
from typing import Tuple, Optional

# AttributeType is a Tuple (str, str?)
AttributeType = Tuple[str, Optional[str]]
"""
AttributeType = Tuple[str, Optional[str]]