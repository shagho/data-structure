class nash_bank_account(object):
    def __init__(self,national_code, bank_name, shba_number, account_number):
        self.__national_code = national_code
        self.__bank_name = bank_name
        self.__shaba_number = shba_number
        self.__account_number = account_number
        self.__key = shba_number
        
    @property
    def national_code(self):
        return self.__national_code
    
    @national_code.setter
    def national_code(self, value):
        self.__national_code = value

    @property
    def bank_name(self):
        return self.__bank_name

    @bank_name.setter
    def bank_name(self, value):
        self.__bank_name = value

    @property
    def shaba_number(self):
        return self.__bank_name

    @shaba_number.setter
    def shaba_number(self, value):
        self.__shaba_number = value

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, value):
        self.__account_number = value

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, value):
        self.__key = value

