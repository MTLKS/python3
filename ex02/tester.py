from DiamondTrap import King
from S1E7 import Baratheon, Lannister
from S1E9 import Character


def main():
    """Main function."""
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)

    if (isinstance(Joffrey, King) and issubclass(King, Lannister)
            and issubclass(King, Baratheon) and issubclass(King, Character)):
        print("OK")
    else:
        print("KO")


if __name__ == "__main__":
    main()
