class nash_transaction(object):

    def __init__(self, transaction_time, transaction_number, amount):
        self.__transaction_time = transaction_time
        self.__transaction_number = transaction_number
        self.__amount = amount
        self.__key = transaction_number
        self.__From = None
        self.__to = None


    @property
    def transaction_time(self):
        return self.__transaction_time

    @transaction_time.setter
    def transaction_time(self, value):
        self.__transaction_time = value

    @property
    def transaction_number(self):
        return self.__transaction_number

    @transaction_number.setter
    def transaction_number(self, value):
        self.__transaction_number = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value

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
