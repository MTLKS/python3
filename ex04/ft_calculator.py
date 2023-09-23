class calculator:
    """calculator class"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """calculator dotproduct"""
        print("Dot product is:", sum([V1[i] * V2[i] for i in range(len(V1))]))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """calculator addition"""
        print("Add Vector is:",
              [float(V1[i] + V2[i]) for i in range(len(V1))])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """calculator subtraction"""
        print("Sous Vector is:",
              [float(V1[i] - V2[i]) for i in range(len(V1))])
