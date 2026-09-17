class Glassware:
    def __init__(self, capacity_ml: float):
        self.capacity_ml = capacity_ml

    def __repr__(self):
        return f"Glassware(capacity={self.capacity_ml}ml)"


class Beaker(Glassware):
    def __init__(self, capacity_ml: float, is_graduated: bool = True):
        super().__init__(capacity_ml)
        self.is_graduated = is_graduated

    def __repr__(self):
        return f"Beaker(capacity={self.capacity_ml}ml, graduated={self.is_graduated})"


class Tray:
    def __init__(self, beaker_capacity: float = 250.0):
        self.beakers = [Beaker(beaker_capacity) for _ in range(5)]

    def __del__(self):
        self.beakers.clear()

    def __repr__(self):
        return f"Tray(beakers={self.beakers})"


if __name__ == "__main__":
    lab_tray = Tray(beaker_capacity=500.0)
    print("Tray created with 5 composed Beakers:")
    print(lab_tray)
    
    del lab_tray
    print("Tray deleted. Composed Beakers are destroyed.")

 