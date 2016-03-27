# -*- coding: utf-8 -*-

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


