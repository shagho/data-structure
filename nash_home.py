class nash_home(object):
    def __init__(self, national_code, home_price, post_code, area, address):
        self.__national_code = national_code
        self.__home_price = home_price
        self.__post_code = post_code
        self.__area = area
        self.__address = address
        self.__key = post_code

    @property
    def national_code(self):
        return self.__national_code

    @national_code.setter
    def national_code(self, value):
        self.__national_code = value

    @property
    def home_price(self):
        return self.__home_price

    @home_price.setter
    def home_price(self, value):
        self.__home_price = value

    @property
    def post_code(self):
        return self.__post_code

    @post_code.setter
    def post_code(self, value):
        self.__post_code = value

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, value):
        self.__area = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, value):
        self.__key = value