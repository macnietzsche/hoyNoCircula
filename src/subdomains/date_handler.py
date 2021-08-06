class DateHandler:
    def __init__(self,date_time) -> None:
        self.datetime=date_time

    @property
    def datetime(self):
        return self._datetime

    @datetime.setter
    def datetime(self,datetime):
        self._datetime=datetime

