# -*- coding: utf-8 -*-
import datetime

class TimeRange(object):
    """
    Parameters
    ----------
    start : DateTime

    end: DateTime
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end

        self.check_range()

    def check_range(self):
        if self.start > self.end:
            raise ValueError("Start cannot be greater than end.")



    def elapsed_time(self):
        return datetime.datetime.now() - self.start

    def remaining_time(self):
        import datetime
        
        remaining_time = self.end - datetime.datetime.now()
        
        if remaining_time < 0:
            return datetime.timedelta(0)
        else:
            return remaining_time

