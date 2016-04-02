# -*- coding: utf-8 -*-


class Frequency(object):
    def __init__(self, unit):
        self.unit = unit


class FrequencyAtFixedDate(Frequency):
    def __init__(self, unit, each=1):
        super().init(unit)
        self.each = each
    
class Recurrence(object):
    def __init__(self, frequency_at_fixed_date, time_range):
        self.frequency = frequency_at_fixed_date
        self.start = time_range.start
        self.end = time_range.end

        
ONCE_A_MONTH = Frequency("month")
ONCE_A_YEAR = Frequency("year")
ONCE_A_WEEK = Frequency("week")

EVERY_FIRST_OF_MONTH = FrequencyAtFixedDate("month", each=1)
