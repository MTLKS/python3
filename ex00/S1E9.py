from abc import ABC, abstractmethod


class Character(ABC):
    """Character class"""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Character Init method"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Unalive method"""
        self.is_alive = False


class Stark(Character):
    """Stark class"""

    def __init__(self, first_name, is_alive=True):
        """Stark Init method"""
        super().__init__(first_name, is_alive)
