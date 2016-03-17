# -*- coding: utf-8 -*-



class Room():
    def __init__(self, surface):
        self.surface = surface
        

class HabitableRoom(Room):
    pass


class UnhabitableRoom(Room):
    pass








class BedRoom(HabitableRoom):
    pass

    
class LivingRoom(HabitableRoom):
    pass
    
class Kitchen(UnhabitableRoom):
    pass

    
class MainRoom(HabitableRoom):
    pass
    
class BathRoom(UnhabitableRoom):
    pass

class Lavatory(UnhabitableRoom):
    pass


