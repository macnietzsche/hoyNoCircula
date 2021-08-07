from src.subdomains.date_handler import DateHandler
from src.subdomains.plate import LicensePlate
from src.services.settings_handler import SettingsHandler
from src.services.time_methods import is_time_in_range

class Predictor:
    def __init__(self,date_n_time,plates) -> None:
        self.date_n_time=DateHandler(date_n_time)
        self.plates=LicensePlate(plates)

    
    def can_my_vehicle_be_on_the_road(self)->bool:
        day_of_the_week_as_integer=self.date_n_time.get_day_as_integer()
        time=self.date_n_time.get_hour_as_time_object()
        last_digit_of_plate=self.plates.get_last_digit()

        day_settings=SettingsHandler(day_of_the_week_as_integer)
        restricted_time_segments=day_settings.get_restricted_time_segments()
        restricted_plate_last_digits=day_settings.get_restricted_plate_ending_digits()

        
        for restricted_time_segment in restricted_time_segments:
            if is_time_in_range(*restricted_time_segment,time): 
                if last_digit_of_plate in restricted_plate_last_digits:
                     return False
                else: 
                    break

        return True
    


    