
class Position():
    def __init__(self, address, location_in_building):
        self.address = address
        self.location_in_building = location_in_building


class LocationInBuilding():
    def __init__(self, floor, door):
        self.floor = floor
        self.door = door


class Floor():
    def __init__(self, number):
        self.number = number

    ##number may vary as function of country

    
class Door():
    def __init__(self, info):
        self.info = info #can store any kind of information


