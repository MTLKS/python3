from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the legitimate king :D"""

    def __init__(self, first_name, is_alive=True):
        """King Init method"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def set_eyes(self, eyes):
        """Set eyes color"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Set hairs color"""
        self.hairs = hairs

    def get_eyes(self):
        """Get eyes color"""
        return self.eyes

    def get_hairs(self):
        """Get hairs color"""
        return self.hairs
