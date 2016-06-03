# -*- coding: utf-8 -*-


class Surface():
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

        
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self._add_two_geometrical_surfaces(other)
        else:
            raise TypeError("Cannot add Surface to a different class")


    def _add_two_geometrical_surfaces(self, other):
        self.check_same_unit(other)
        sum_value = self.value + other.value
        return self.__class__(sum_value, self.unit)

        
    def check_same_unit(self, other):
        if not self.have_same_unit(other):
            raise TypeError("Cannot perform operation on instances with different units.")

        
    def have_same_unit(self, other):
        return self.unit == other.unit

    
    def __radd__(self, other):
        return self.__add__(other)

    def __eq__(self, other):
        ## TODO: we could handle automatically the change in units
        value_are_equal = (self.value == other.value)
        unit_are_equal = (self.unit == other.unit)
        return value_are_equal & unit_are_equal

    def __gt__(self, other):
        self.check_same_unit(other)
        return self.value > other.value

    def __lt__(self, other):
        self.check_same_unit(other)
        return self.value < other.value
