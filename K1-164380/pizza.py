import math


class Pizza:
    def __init__(self, toppings: list[str], diameter: float):
        self.__toppings = toppings
        self.__diameter = diameter

    @staticmethod
    def area(self, value) -> float:
        if self.__diameter < 20:
            print("Bledny promien")
            exit(-10)
        else:
            value = math.pi * (self.__diameter / 2) ^ 2
            return value

    def cena(self, price: float) -> float:
        for i in range(len(self.__toppings)):
            i = i + 1
            price = 0.005 * self.area(self.__diameter) + i
            return price

    @property
    def diameter(self) -> float:
        if self.__diameter.area() < 20:
            print("Bledna srednica")
            exit(-10)
        else:
            return self.__diameter

    def add_topping(self, topping: str) -> None:
        self.__toppings.append(topping)
        self.cena() + 2

    def __repr__(self):
        for i in range(len(self.__toppings)):
            i = i + 1
            if i = 0:
                return f'Pizza: \nsrednica: {self.__diameter} \ncena: {self.cena()}'
            else:
                return f'Pizza: \nsrednica: {self.__diameter} \ndodatki: {self.__toppings} \ncena: {self.cena()}'
