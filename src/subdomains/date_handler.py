from datetime import datetime
class DateHandler:
    def __init__(self,date_time_input) -> None:
        self.date_time_object=date_time_input
    @property
    def date_time_object(self):
        return self._date_time_object

    @date_time_object.setter
    def date_time_object(self,date_time_input):
        try:
            self._date_time_object=datetime.strptime(date_time_input,"%Y-%m-%d %H:%M")
        except ValueError:
            raise Exception("Datetime input is not valid")

    def get_day_as_integer(self):
        return self.date_time_object.weekday()

    def get_hour_as_time_object(self):
        return self.date_time_object.time()
    
        

