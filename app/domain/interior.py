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


    def category(self):
        """Returns the category of the apartment (eg: studio)"""
        ##we should add here a dictionary returning the category
        raise NotImplementedError
            
        
  

class Equipment():
    def __init__(self):
        pass
