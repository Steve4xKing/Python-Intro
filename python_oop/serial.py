"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=100):
        """Initialize the serial number generator."""
        self.start = start

    def __repr__(self):
        """Return the representation of the serial number generator."""
        return "<SerialGenerator start=100 next=101>"
    

    def generate(self):
        """Generate a new serial number."""
        self.gen = self.start
        self.start += 1
        return self.gen
    
    def reset(self):
        """Reset the serial number to the original start number."""
        self.start = 100


# sg = SerialGenerator()
# print(sg)

# print(sg.generate())
# print(sg.generate())
# print(sg.generate())
# print(sg.generate())
# sg.reset()
# print(sg.generate())
# print(sg.generate())
# print(sg.generate())
# print(sg.generate())
# print(sg.generate())
