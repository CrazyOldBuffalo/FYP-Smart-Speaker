from datetime import datetime, date, time


class EventObj:
    def __init__(self, start_date: date, start_time: time, end_date: date, end_time: time, summary: str, url) -> None:
        self.__start_date = start_date
        self.__start_time = start_time
        self.__end_date = end_date
        self.__end_time = end_time
        self.__title = summary
        self.__url = url

    # Getters
    def get_start_date(self) -> date:
        return self.__start_date

    def get_start_time(self) -> time:
        return self.__start_time

    def get_start_date_time(self) -> datetime:
        start_date_time = datetime.combine(self.__start_date, self.__start_time)
        return start_date_time

    def get_end_date(self) -> date:
        return self.__end_date

    def get_end_time(self) -> time:
        return self.__end_time

    def get_end_date_time(self) -> datetime:
        end_date_time = datetime.combine(self.__end_date, self.__end_time)
        return end_date_time

    def get_summary(self) -> str:
        return self.__title

    def get_url(self):
        return self.__url

    # Setters
    def set_url(self, url):
        self.__url = url

    def set_start_date(self, start_date: date) -> None:
        self.__start_date = start_date

    def set_start_time(self, start_time: time) -> None:
        self.__start_time = start_time

    def set_end_date(self, end_date: date) -> None:
        self.__end_date = end_date

    def set_end_time(self, end_time: time) -> None:
        self.__end_time = end_time

    def set_summary(self, summary: str) -> None:
        self.__title = summary

    # Manipulation of dates and times
    def convert_dt_to_str(self, dt: datetime) -> str:
        return str(dt)
