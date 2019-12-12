class nash_ownership(object):

    def __init__(self, document_registration_number, ownership_time, price):
        self.__document_registration_number = document_registration_number
        self.__ownership_time = ownership_time
        self.__price = price
        self.__key = document_registration_number
        self.__from = None
        self.__to = None


    @property
    def document_registration_number(self):
        return self.__document_registration_number 
    
    @document_registration_number.setter
    def document_registration_number(self, value):
        self.__document_registration_number = value
        
    @property
    def ownership_time(self):
        return self.__ownership_time 
    
    @ownership_time.setter
    def ownership_time(self, value):
        self.__ownership_time = value
        
    @property
    def price(self):
        return self.__price 
    
    @price.setter
    def price(self, value):
        self.__price = value
        
    @property
    def key(self):
        return self.__key 
    
    @key.setter
    def key(self, value):
        self.__key = value
        
    @property
    def From(self):
        return self.__from 
    
    @From.setter
    def From(self, value):
        self.__from = value
        
    @property
    def to(self):
        return self.__to 
    
    @to.setter
    def to(self, value):
        self.__to = value
