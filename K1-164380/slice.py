from pizza import Pizza


class Slice:
    def __init__(self, how_many_slices: int, toppings: list[str], diameter: float):
        if self.how_many_slices < 4 or self.how_many_slices > 12:
            if self.how_many_slices % 2 == 1:
                print("Bledna ilosc kawalkow")
                exit(-10)
            else:
                self.__how_many_slices = how_many_slices
        super().__init__(how_many_slices, toppings, diameter)

    @property
    def how_many_slices(self) -> int:
        return self.__how_many_slices

    @how_many_slices.setter
    def how_many_slices(self, value: int) -> None:
        if value.how_many_slices < 4 or value.how_many_slices > 12:
            if value.how_many_slices % 2 == 1:
                print("Bledna ilosc kawalkow")
                exit(-10)
            value.how_many_slices = self.__how_many_slices
        return

    def part_price(self, ordered_slices) -> None:
        return

    def __repr__(self):
        for i in range(len(self.toppings)):
            i = i + 1
            if i = 0:
                return f'Pizza: \nsrednica: {self.diameter} \ncena: {self.cena()}'
            else:
                return f'Pizza: \nsrednica: {self.diameter} \ndodatki: {self.toppings} \ncena: {self.cena()}'
