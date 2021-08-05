import re
class LicensePlate:
    def __init__(self,plate) -> None:
        self.plate=plate

    @property
    def plate(self):
        return self._plate

    @plate.setter
    def plate(self,plate):
        matched_plate_pattern = re.match(r'^[A-Z]{3}-\d{3,4}$',plate)
        if not bool(matched_plate_pattern): raise Exception("Input plate does not match with Ecuadorian license plate format.")
        self._plate=plate