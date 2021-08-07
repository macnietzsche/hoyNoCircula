class SettingsHandler():
    def __init__(self,day_of_week_as_integer) -> None:
        self.day_of_week_as_integer=day_of_week_as_integer

    @property
    def day_of_week_as_integer(self):
        return self._day_of_week_as_integer
    
    @day_of_week_as_integer.setter
    def day_of_week_as_integer(self,day_of_week_as_integer):
        if not (isinstance(day_of_week_as_integer, int) and day_of_week_as_integer>=0 and day_of_week_as_integer<=6): raise Exception("Day parameter is not valid")
        self._day_of_week_as_integer=day_of_week_as_integer

    def get_restricted_time_segments(self):
        return None
    
    def get_restricted_plate_ending_digits(self):
        return None