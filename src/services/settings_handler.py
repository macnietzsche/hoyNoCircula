from configparser import ConfigParser
from src.subdomains.date_handler import DateHandler

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
        time_segments = self._settings_of_day['restricted_time'].split("/")
        time_segments_list=[]
        for time_segment in time_segments:
            (start_time,end_time)=time_segment.split("-")
            start_time_as_date=DateHandler(start_time).get_hour_as_time_object()
            end_time_as_date=DateHandler(end_time).get_hour_as_time_object()
            if(end_time_as_date>=start_time_as_date):
                time_segments_list.append((start_time_as_date,end_time_as_date))
            else:
                raise Exception("End time must be greater or equals than start time")
       
        return time_segments_list
    
    def get_restricted_plate_ending_digits(self):
         digits_as_characters=self._settings_of_day['restricted_plate_ending_digit'].split(",")
         return list(map(lambda x: int(x),digits_as_characters))