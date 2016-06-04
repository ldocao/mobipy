# -*- coding: utf-8 -*-

__all__ = ["mysql"]

from mobipy.infrastructure.database.connexion import (Driver,
                                                      Database,
                                                      User,
                                                      Engine)



_dialect = "mysql"
_driver = "pymysql"
_host = 'localhost'
_port = 3306
_name = 'mobipy'
_username = "root"
_password = "root"


psycopg2 = Driver(_dialect, _driver)
mobipy = Database(_host, _port, _name)
root = User(_username, _password)
mysql = Engine(psycopg2, mobipy, root)

