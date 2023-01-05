from element import Element
from File import File
from typing import List

class Directory(Element):

    def __init__(self, name: str = None, year: int = 1970,  elements: List[File] = []) -> None:
        self.__elements = elements
        super().__init__(name, year)

    @property
    def elements(self) -> List[File]:
        return self.__elements

    @elements.setter
    def elements(self, elements: List[File]) -> None:
        self.__elements = elements

    def add_element(self, plik: 'File') -> None:
        self.elements.append(plik)

    def rozmiar(self) -> int:
        size = 0
        for element in self.elements:
            size = size + element.size
        return size

    def __str__(self) -> str:
        return f'Nazwa: {self.name}. Utworzony {self.year}. Rozmiar: {self.rozmiar()}. Zawartosc: {self.elements}'
