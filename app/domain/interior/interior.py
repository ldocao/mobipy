# -*- coding: utf-8 -*-


        
class Interior():
    def __init__(self, caracteristics, equipment):
        self.caracteristics = caracteristics
        self.equipment = equipment



class Caracteristics():
    """

    Parameters
    ----------
    surface: Surface
        Surface of the interior
    
    rooms: list
        List of all rooms
    """
    def __init__(self, surface, rooms):
        self.surface = surface
        self.rooms = rooms
        self.category = self.category()


    def category(self):
        """Returns the category of the apartment (eg: 2 pièces)"""

        label = {0: "impossible",
                 1: "studio",
                 2: "2 pièce(s)"}
        
        return label[self.number_of_habitable_room()]


    def number_of_habitable_room(self):
        return  sum([self.is_habitable(room) for room in self.rooms])

    @staticmethod
    def is_habitable(room):
        from domain.interior.room import HabitableRoom
        return issubclass(room.__class__, HabitableRoom)











    
class Surface():
    def __init__(self, ground, carrez=None, unit="square meter"):
        self.ground = ground
        self.carrez = carrez
        self.unit = unit

        self._check_value_consistency()


    def _check_value_consistency(self):
        self._auto_fill_carrez_if_empty()
        self._compare_ground_and_carrez()


    def _auto_fill_carrez_if_empty(self):
        if self.carrez is None:
            self.carrez = self.ground

    
    def _compare_ground_and_carrez(self):
        if self.ground < self.carrez:
            raise ValueError("carrez cannot be greater than ground")
        
        
        
class Equipment():
    def __init__(self):
        pass
