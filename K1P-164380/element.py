class Element:
    def __init__(self, name: str = None, year: int = 1970) -> None:
        self.__name = name
        if year < 1980 and year > 2023:
            self.__year = 1970
        else:
            self.__year = year

    @property
    def name(self) -> str:
        return self.__name
    @property
    def year(self) -> int:
        return self.__year

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @year.setter
    def year(self, year: int) -> None:
        if year < 1980 and year > 2023:
            print("wartosc argumentu nie spelnia zalozen")
        else:
            self.__year = year

    def __str__(self) -> str:
        return f'Nazwa: {self.name}. Utworzony {self.year}'

    def __eq__(self, other: 'Element') -> bool:
        if self.name == other.name and self.year == other.year:
            return True
        else:
            return False

    def __ne__(self, other: 'Element') -> bool:
        if self.name != other.name or self.year != other.year:
            return True
        else:
            return False
