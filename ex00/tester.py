from S1E9 import Character, Stark


def main():
    """Main function."""
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)

    try:
        hodor = Character("Hodor")
        print(hodor)
    except TypeError as e:
        print(e.__class__.__name__ + ":", e)


if __name__ == "__main__":
    main()
