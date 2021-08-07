from src.subdomains.date_handler import DateHandler
from src.subdomains.plate import LicensePlate

class Predictor:
    def __init__(self,time,plates) -> None:
        self.time=DateHandler(time)
        self.plates=LicensePlate(plates)

    
    def can_my_vehicle_be_on_the_road(self)->bool:
        return None
    


    