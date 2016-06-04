# -*- coding: utf-8 -*-


import datetime
import pandas as pd
from mobipy.infrastructure.setup import engine
import ipdb


class CumulativeProfit(object):
    def __init__(self, rentable, at=datetime.datetime.now()):
        self.rentable = rentable
        self.at = at


    @property
    def value(self):
        contracts = self.select_contract()
        contracts["total"] = contracts["rent"] + contracts["expenditure"]
        contracts["duration"] = self.duration(contracts[["entry_date", "exit_date"]])
        contracts["rent_factor"] = contracts["duration"] / datetime.timedelta(30) # TODO: we do the approximation that each month lasts 30days. eventually we could do that exactly, but it's a pain...
        return (contracts["total"]*contracts["rent_factor"]).sum()

    
    def duration(self, contracts):
        ## we first fill the NaN with self.at, then we replace the exit_date by self.at if exit_date is after
        contracts["exit_date"] = contracts["exit_date"].fillna(self.at)
        contracts["exit_date"] = contracts["exit_date"].apply(lambda x: x if x < self.at else self.at)
        return contracts["exit_date"] - contracts["entry_date"]


        
    def select_contract(self):
        ## select contract of the rentable whose entry date was before the requested_date
        with engine.begin() as connexion:
            columns = ["entry_date", "exit_date", "rent", "expenditure"]
            entries = """ SELECT {0} 
                          FROM {1}
                          WHERE rentable = '{2}' AND entry_date < '{3}'
                      """.format(", ".join(columns),
                                 "lodgercontract",
                                 self.rentable,
                                 self.at)

            query = connexion.execute(entries)
            
        return pd.DataFrame(query.fetchall(), columns=columns)

