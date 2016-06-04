# -*- coding: utf-8 -*-


from mobipy.infrastructure.setup import engine
from mobipy.infrastructure.database.orm import Base


## CREATE: in order for drop_all and create_all to work, you need the tables to be available in this scope
from mobipy.domain.accomodation.property.property import *
#from mobipy.domain.accomodation.rentable.rentable import *


with engine.begin() as connexion:
    connexion.execute("DROP DATABASE mobipy")
    connexion.execute("CREATE DATABASE mobipy")
    connexion.execute("USE mobipy")
    

    
## FILL FROM SOURCE
Address().source_to_sql()
Property().source_to_sql()
# Solo().source_to_sql(if_exists="replace", index=False)
# Shared().source_to_sql(if_exists="replace", index=False)

