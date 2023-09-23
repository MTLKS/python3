class calculator:
    """calculator class"""

    def __init__(self, vector):
        """calculator constructor"""
        self.vector = vector

    def __add__(self, object):
        """calculator addition"""
        self.vector = [elem + object for elem in self.vector]
        print(self.vector)

    def __sub__(self, object):
        """calculator subtraction"""
        self.vector = [elem - object for elem in self.vector]
        print(self.vector)

    def __mul__(self, object):
        """calculator multiplication"""
        self.vector = [elem * object for elem in self.vector]
        print(self.vector)

    def __truediv__(self, object):
        """calculator division"""
        if object == 0:
            print("ERROR (div by zero)")
            return

        self.vector = [elem / object for elem in self.vector]
        print(self.vector)
