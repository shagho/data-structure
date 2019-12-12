class nash_car(object):

    def __init__(self, numberplate, national_code, model, color):
        self.__numberplate = numberplate
        self.__national_code = national_code
        self.__model = model
        self.__color = color
        self.__key = numberplate

    @property
    def numberplate(self):
        return self.__numberplate

    @numberplate.setter
    def numberplate(self, value):
        self.__numberplate = value

    @property
    def national_code(self):
        return self.__national_code

    @national_code.setter
    def national_code(self, value):
        self.__national_code = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, value):
        self.__key = value
