class MyInt(int):
    """
    MyInt - Inherits from int but reverses the behavior of == and != operators
    """

    def __eq__(self, other):
        """Overrides the equality operator (==)"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Overrides the inequality operator (!=)"""
        return not super().__ne__(other)
