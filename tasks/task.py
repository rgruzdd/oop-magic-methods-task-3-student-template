from __future__ import annotations
from typing import Type


class Currency:

    def __init__(self, value: float):
        self.value = value

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        return ''

    def to_currency(self, other_cls: Type[Currency]):
        return ''

class Euro(Currency):
    def __init__(self, value: float):
        super().__init__(value)

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        current_currency = str(1) + ' EUR'
        foreign_currency = str(1.0) + ' EUR'
        if other_cls == Dollar:
            foreign_currency = str(2.0) + ' USD'
        elif other_cls == Pound:
            foreign_currency = str(100.0) + ' GBP'
        return str(foreign_currency) + ' for ' + str(current_currency)

    def to_currency(self, other_cls: Type[Currency]):
        current_currency = int(self.value)
        foreign_currency = 0
        if other_cls == Euro:
            foreign_currency = float(current_currency)
            return Euro(foreign_currency)
        elif other_cls == Dollar:
            foreign_currency = (float(current_currency) * 2)
            return Dollar(foreign_currency)
        elif other_cls == Pound:
            foreign_currency = (float(current_currency) * 100)
        return Pound(foreign_currency)

    def __str__(self):
        return str(self.value) + ' EUR'

    def __add__(self, other):
        if type(other) == Euro:
            new_value = float(self.value + other.value)
        elif type(other) != Euro:
            new_value = float(self.value + float(other.to_currency(Euro).split(' ')[0]))
        return str(new_value) + ' EUR'

    def __eq__(self, other):
        if type(other) == Euro:
            new_value = self.value == other.value
        elif type(other) != Euro:
            new_value = self.value == float(other.to_currency(Euro).split(' ')[0])
        return new_value

    def __lt__(self, other):
        if type(other) == Euro:
            new_value = self.value < other.value
        elif type(other) != Euro:
            new_value = self.value < float(other.to_currency(Euro).split(' ')[0])
        return new_value

    def __gt__(self, other):
        if type(other) == Euro:
            new_value = self.value > other.value
        elif type(other) != Euro:
            new_value = self.value > float(other.to_currency(Euro).split(' ')[0])
        return new_value

class Dollar(Currency):
    def __init__(self, value: float):
        super().__init__(value)

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        current_currency = str(1) + ' USD'
        foreign_currency = str(1.0) + ' USD'
        if other_cls == Euro:
            foreign_currency = str(0.5) + ' EUR'
        elif other_cls == Pound:
            foreign_currency = str(50.0) + ' GBP'
        return str(foreign_currency) + ' for ' + str(current_currency)

    def to_currency(self, other_cls: Type[Currency]):
        current_currency = int(self.value)
        foreign_currency = 0
        if other_cls == Euro:
            foreign_currency = float(current_currency) * 0.5
            return Euro(foreign_currency)
        elif other_cls == Dollar:
            foreign_currency = float(current_currency)
            return Dollar(foreign_currency)
        elif other_cls == Pound:
            foreign_currency = float(current_currency) * 50
        return Pound(foreign_currency)

    def __str__(self):
        return str(self.value) + ' USD'

    def __add__(self, other):
        if type(other) == Dollar:
            new_value = float(self.value + other.value)
        elif type(other) != Dollar:
            new_value = float(self.value + float(other.to_currency(Dollar).split(' ')[0]))
        return str(new_value) + ' USD'

    def __eq__(self, other):
        if type(other) == Dollar:
            new_value = self.value == other.value
        elif type(other) != Dollar:
            new_value = self.value == float(other.to_currency(Dollar).split(' ')[0])
        return new_value

    def __lt__(self, other):
        if type(other) == Dollar:
            new_value = self.value < other.value
        elif type(other) != Dollar:
            new_value = self.value < float(other.to_currency(Dollar).split(' ')[0])
        return new_value

    def __gt__(self, other):
        if type(other) == Dollar:
            new_value = self.value > other.value
        elif type(other) != Dollar:
            new_value = self.value > float(other.to_currency(Dollar).split(' ')[0])
        return new_value

class Pound(Currency):
    def __init__(self, value: float):
        super().__init__(value)

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        current_currency = str(1) + ' GBP'
        foreign_currency = str(1.0) + ' GBP'
        if other_cls == Dollar:
            foreign_currency = str(0.02) + ' USD'
        elif other_cls == Euro:
            foreign_currency = str(0.01) + ' EUR'
        return str(foreign_currency) + ' for ' + str(current_currency)

    def to_currency(self, other_cls: Type[Currency]):
        current_currency = int(self.value)
        foreign_currency = 0
        if other_cls == Euro:
            foreign_currency = float(current_currency) * 0.01
            return Euro(foreign_currency)
        elif other_cls == Dollar:
            foreign_currency = float(current_currency) * 0.02
            return Dollar(foreign_currency)
        elif other_cls == Pound:
            foreign_currency = float(current_currency) * 1
        return Pound(foreign_currency)

    def __str__(self):
        return str(self.value) + ' GBP'

    def __add__(self, other):
        if type(other) == Pound:
            new_value = float(self.value + other.value)
        elif type(other) != Pound:
            new_value = float(self.value + float(other.to_currency(Pound).split(' ')[0]))
        return str(new_value) + ' GBR'

    def __eq__(self, other):
        if type(other) == Pound:
            new_value = self.value == other.value
        elif type(other) != Pound:
            new_value = self.value == float(other.to_currency(Pound).split(' ')[0])
        return new_value

    def __lt__(self, other):
        if type(other) == Pound:
            new_value = self.value < other.value
        elif type(other) != Pound:
            new_value = self.value < float(other.to_currency(Pound).split(' ')[0])
        return new_value

    def __gt__(self, other):
        if type(other) == Pound:
            new_value = self.value > other.value
        elif type(other) != Pound:
            new_value = self.value > float(other.to_currency(Pound).split(' ')[0])
        return new_value

