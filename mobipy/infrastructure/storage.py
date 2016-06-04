# -*- coding: utf-8 -*-

__all__ = ["File", "LocalFile", "CSV"]


import os


class File(object):
    def __repr__(self):
        return self.path



class LocalFile(File):
    def __init__(self, path_in_app):
        self.path = self._reconstruct_absolute_path(path_in_app)

        
    def _reconstruct_absolute_path(self, path_in_app):
        from mobipy.infrastructure.setup import app_path
        
        path_to_app = app_path.app
        absolute_path = path_to_app+path_in_app

        return absolute_path


    
class CSV(LocalFile):
    ENCODING = "utf8"
    SEP_HEADER = "#"
    SEP_FIELD = ","
    SEP_LIST = ";"
