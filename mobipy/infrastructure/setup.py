# -*- coding: utf-8 -*-


__all__ = ["app_path", "connexion", "engine"]

from mobipy.infrastructure.database.connexion import mysql 
from mobipy.infrastructure.app_path import AppPath

app_path = AppPath()
engine = mysql.engine

