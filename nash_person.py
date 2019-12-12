class nash_person(object):
    def __init__(self, name, family_name, national_code, birth_day, birth_place, work_company, work_address):
        self.__name = name
        self.__family_name = family_name
        self.__national_code = national_code
        self.__birth_day = birth_day
        self.__birth_place = birth_place
        self.__work_company = work_company
        self.__work_address = work_address
        self.__key = national_code

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def family_name(self):
        return self.__family_name

    @family_name.setter
    def family_name(self, value):
        self.__family_name = value

    @property
    def birth_day(self):
        return self.__birth_day

    @birth_day.setter
    def birth_day(self, value):
        self.__birth_day = value

    @property
    def national_code(self):
        return self.national_code

    @national_code.setter
    def national_code(self, value):
        self.__national_code = value

    @property
    def birth_place(self):
        return self.__birth_place

    @birth_place.setter
    def birth_place(self, value):
        self.__birth_place = value

    @property
    def work_company(self):
        return self.__work_company

    @work_company.setter
    def work_company(self, value):
        self.__work_company = value

    @property
    def work_address(self):
        return self.__work_address 
    
    @work_address.setter
    def work_address(self, value):
        self.__work_address = value

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, value):
        self.__key = value
