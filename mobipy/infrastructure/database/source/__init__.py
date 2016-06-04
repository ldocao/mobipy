# -*- coding: utf-8 -*-
## PURPOSE: source tables are meant to be temporary. We should do one bulk load every day. So the source table is flushed away every day. Then the step of copying from source to atom will handle the task to spot any duplicate rows.


from infrastructure.database.source.digitick_ticket import *
from infrastructure.database.source.show_catalog import *

