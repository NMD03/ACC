
class MathStructure:
    """Base class for mathematical structures like finite fields, elliptic curves, etc."""
    def __add__(self, other):
        raise NotImplementedError("Addition is not implemented for this structure.")

    def __sub__(self, other):
        raise NotImplementedError("Subtraction is not implemented for this structure.")

    def __mul__(self, other):
        raise NotImplementedError("Multiplication is not implemented for this structure.")

    def __truediv__(self, other):
        raise NotImplementedError("Division is not implemented for this structure.")

    def inv(self):
        """Inverse of an element (if applicable)."""
        raise NotImplementedError("Inverse is not implemented for this structure.")

    def __repr__(self):
        return "Abstract MathStructure"
