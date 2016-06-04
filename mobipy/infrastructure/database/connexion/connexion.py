# -*- coding: utf-8 -*-


__all__ = ["Engine", "Driver", "Database", "User"]



import sqlalchemy
    

class Engine(object):
    def __init__(self, driver, database, user, option=None):
        self.driver = driver
        self.database = database
        self.user = user
        self.option = option
        self.engine = self.create()


    def create(self):
        from mobipy.infrastructure.storage import CSV
        encoding = CSV.ENCODING
        driver = self.driver.as_string()
        user = self.user.login()
        database = self.database.entry_point()

        create_engine_query = """{0}://{1}@{2}""".format(driver,
                                                         user,
                                                         database)

        create_engine_query = self.add_option(create_engine_query)
        
        return sqlalchemy.create_engine(create_engine_query,
                                        encoding=encoding)

    
    def add_option(self, query):
        try:
            return query + self.option
        except TypeError:
            return query



    
class Driver(object):
    """
    Parameters
    ----------
    dialect: string
        Type of database (eg: "posgreSQL", "redshift", "mysql", etc.)

    driver: string
        Package used to connect python to the database (eg: "psycopg2")
    """
    def __init__(self, dialect, driver):
        self.dialect = dialect
        self.driver = driver

    def as_string(self):
        return "+".join([self.dialect, self.driver])



    
    
class Database(object):
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name

    def entry_point(self):
        return self.host + ":" + str(self.port) + "/" + self.name
        



    
class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        return self.username + ":" + self.password
