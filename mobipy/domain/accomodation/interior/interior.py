# -*- coding: utf-8 -*-


        
class Interior():
    def __init__(self, caracteristics, equipment):
        self.caracteristics = caracteristics
        self.equipment = equipment



class Caracteristics():
    def __init__(self, surface, rooms):
        self.surface = surface
        self.rooms = rooms
        self.category = self.category()

        self.check_surface()

    def category(self):
        """Returns the category of the apartment (eg: 2 pièces)"""

        label = {0: "impossible",
                 1: "studio",
                 2: "2 pièce(s)",
                 3: "3 pièce(s)"}
        
        return label[self.number_of_habitable_room()]


    def number_of_habitable_room(self):
        return  sum([self.is_habitable(room) for room in self.rooms])

    @staticmethod
    def is_habitable(room):
        from domain.interior.room import HabitableRoom
        return issubclass(room.__class__, HabitableRoom)


    def check_surface(self):
        if self.sum_of_room_surface() > self.surface:
            raise ValueError("surface must be greater or equal the sum of room surfaces")


    def sum_of_room_surface(self):
        # TODO: allow for different unit surfaces between different rooms
        
        import utils.geometry as geometry
        
        if self.room_have_same_unit():
            common_unit = self.rooms[0].surface.ground.unit
            zero_surface = Surface(geometry.Surface(0, common_unit))
            room_surfaces = [room.surface for room in self.rooms]
            return sum(room_surfaces, zero_surface)
        else:
            raise NotImplementedError("Cannot sum surface with different units")

    def room_have_same_unit(self):
        room_units = [room.surface.ground.unit for room in self.rooms]
        is_same_unit = len(set(room_units)) == 1
        return is_same_unit
        



    
class Surface():
    def __init__(self, ground, carrez=None):
        self.ground = ground
        self.carrez = carrez

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


    def __add__(self, other):
        return Surface(self.ground + other.ground,
                       self.carrez + other.carrez)


    def __eq__(self, other):
        same_ground = self.ground == other.ground
        same_carrez = self.carrez == other.carrez
        return same_ground & same_carrez

    def __gt__(self, other):
        return self.ground > other.ground

    def __lt__(self, other):
        return self.ground < other.ground
