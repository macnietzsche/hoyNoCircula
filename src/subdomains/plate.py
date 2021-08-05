class LicensePlate:
    def __init__(self,plate) -> None:
        self.plate=plate

    @property
    def plate(self):
        return self.plate

    @plate.setter
    def plate(self,plate):
        return None
        # raise Exception()