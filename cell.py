from datetime import datetime
colors = ['White', 'Black', 'Red', 'Orange', "Yellow", 'Blue', 'Green']

class Cell:
    def __init__(self, value = '', color = 0):
        self.__value = value
        if 0 <= color <= 6:
            self.__color = colors[color]
        else:
            self.__color = colors[color]

    def set_value(self, value):
        self.__value = value

    def set_color(self, color):
        if 0 <= color <= 6:
            self.__color = colors[color]
        else:
            self.__color = 0
            self.__color = colors[color]

    def get_value(self):
        return self.__value

    def get_color(self):
        return self.__color

    def to_int(self):
        if not isinstance(self.__value, int):
            raise TypeError('The value is not a string')
        self.__value = int(self.__value)
        return self.__value


    def to_float(self):
        if not isinstance(self.__value, float):
            raise TypeError('The value cannot be converted to a float')
        self.__value = float(self.__value)
        return self.__value

        self.__value = float(self.__value)

    def to_date(self):
        if isinstance(self.__value, str):
            try:
                self.__value = datetime.strptime(self.__value, '%Y-%m-%d')
            except:
                ValueError('The value is not suitable for converting to Date ')
        else:
            raise TypeError('The value is not a string')

    def reset(self, value= None):
        self.__value = ''
        self.__color = 0

