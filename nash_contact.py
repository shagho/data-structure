class nash_contact(object):

    def __init__(self, contact_number, contact_time, contact_duration):
        self.__contact_number = contact_number
        self.__contact_time = contact_time
        self.__contact_duration = contact_duration
        self.__key = contact_number
        self.__From = None
        self.__to = None

    @property
    def contact_duration(self):
        return self.__contact_duration

    @contact_duration.setter
    def contact_duration(self, value):
        self.__contact_duration = value

    @property
    def contact_time(self):
        return self.__contact_time

    @contact_time.setter
    def contact_time(self, value):
        self.__contact_time = value

    @property
    def contact_number(self):
        return self.__contact_number

    @contact_number.setter
    def contact_number(self, value):
        self.__contact_number = value

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, value):
        self.__key = value

    @property
    def From(self):
        return self.__From

    @From.setter
    def From(self, value):
        self.__From = value

    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        self.__to = value
