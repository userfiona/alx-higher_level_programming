#!/usr/bin/python3
"""My integer"""


class MyInt(int):
    """My integer"""

    def __eq__(self, value):
        """Override == operator with != behavior."""
        return not super().__eq__(value)

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return not super().__ne__(value)
