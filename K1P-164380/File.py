from element import Element

class File(Element):
    def __init__(self, name: str = None, year: int = 1970,  size: int = 0) -> None:
        if size < 0:
            self.__size = 0
        else:
            self.__size = size

        super().__init__(name, year)

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int) -> None:
        if size < 0:
            print("wartosc argumentu nie spelnia zalozen")
        else:
            self.__size = size

    def __eq__(self, other: 'File') -> bool:
        if self.name == other.name and self.year == other.year and self.size == other.size:
            return True
        else:
            return False

    def __ne__(self, other: 'File') -> bool:
        if self.name != other.name or self.year != other.year or self.size != other.size:
            return True
        else:
            return False

    def __str__(self) -> str:
        return f'Nazwa: {self.name}. Utworzony {self.year}. Rozmiar {self.size}'
