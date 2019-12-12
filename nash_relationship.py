class nash_relationship(object):

    def __init__(self, relation, relation_time):
        self.__relation = relation
        self.__relation_time = relation_time
        self.__key = None
        self.__From = None
        self.__to = None

    @property
    def relation(self):
        return self.__relation

    @relation.setter
    def relation(self, value):
        self.__relation = value

    @property
    def relation_time(self):
        return self.__relation_time

    @relation_time.setter
    def relation_time(self, value):
        self.__relation_time = value

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
