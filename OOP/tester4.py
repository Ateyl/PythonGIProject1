class Car:
    def __init__(self, make, model, color):
        self.__make = make
        self.__model = model
        self.__color = color


    @property
    def make(self):
        return self.__make


    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        self.__color = new_color

    @color.deleter
    def color(self):
        self.__color = None
car1 = Car('Honda', 'Civic', 'black')
car1.model = 'CRV'
print(car1.model)
print(car1.make)
del car1.color