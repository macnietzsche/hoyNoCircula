from configparser import ConfigParser

day_names_hashmap={0: "MONDAY",1:"TUESDAY",2:"WEDNESDAY",3:"THURSDAY",4:"FRIDAY",5:"SATURDAY",6:"SUNDAY"}
class SettingsHandler():
    def __init__(self,day_of_week_as_integer) -> None:
        self.settings_of_day=day_of_week_as_integer

    @property
    def settings_of_day(self):
        return self._settings_of_day
    
    @settings_of_day.setter
    def settings_of_day(self,day_of_week_as_integer):
        if not (isinstance(day_of_week_as_integer, int) and day_of_week_as_integer>=0 and day_of_week_as_integer<=6): raise Exception("Day parameter is not valid")
        config=ConfigParser()
        config.read('config/restrictions.ini')
        self._settings_of_day=config[day_names_hashmap[day_of_week_as_integer]]
        

    def get_restricted_time_segments(self):
        return None
    
    def get_restricted_plate_ending_digits(self):
        return None