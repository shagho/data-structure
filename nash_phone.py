class nash_phone(object):

    def __init__(self, national_code, phone_number, operator):
        self.__national_code = national_code
        self.__phone_number = phone_number
        self.__operator = operator
        self.__key = phone_number

    @property
    def national_code(self):
        return self.__national_code

    @national_code.setter
    def national_code(self, value):
        self.__national_code =value

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        self.__phone_number = value

    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, value):
        self.__operator = value

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, value):
        self.__key = value
