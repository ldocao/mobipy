# -*- coding: utf-8 -*-


from mobipy.infrastructure.setup import engine
from mobipy.infrastructure.database.orm import Base


## CREATE: in order for drop_all and create_all to work, you need the tables to be available in this scope
from mobipy.domain.accomodation.property.property import *
from mobipy.domain.accomodation.rentable.rentable import *
from mobipy.domain.accountancy.lodger import *
from mobipy.domain.accountancy.spending import *


with engine.begin() as connexion:
    connexion.execute("DROP DATABASE mobipy")
    connexion.execute("CREATE DATABASE mobipy")
    connexion.execute("USE mobipy")
    


## FILL FROM SOURCE
### you should not run Base.metadata.create_all(engine) because it raises an IntregityError
Address().source_to_sql()
Property().source_to_sql()
LodgerIdentity().source_to_sql()
LodgerContract().source_to_sql()

FixedSpending().source_to_sql()
RecurrencyType().source_to_sql()
RecurrentSpending().source_to_sql()

