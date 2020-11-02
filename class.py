class Automobile:
    class COLORS:
        red = 'red'
        white = 'white'
        green = 'green'


    def __init__(self, brand, price, year):
        self.brand = brand
        self.price = price
        self.year = year

    def colorify(self, color):
        if color not in (Automobile.COLORS.red, Automobile.COLORS.white, Automobile.COLORS.green):
            raise ValueError("Неизвестный цвет машины")
        self.color = color

