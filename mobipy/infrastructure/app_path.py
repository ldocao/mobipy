# -*- coding: utf-8 -*-

__all__ = ["AppPath"]


import os
import numpy as np


    
class AppPath(object):
    """Path to different directories"""
    def __init__(self):
        self.app = self.find_app_path()

        main_directories = ["domain",
                            "application",
                            "interface",
                            "infrastructure",
                            "utils",
                            "tests"]

        for directory in main_directories:
            value = os.path.join(self.app+directory, "")
            setattr(self, directory, value)


    @staticmethod
    def find_app_path():
        python_path = os.sys.path
        looks_like_my_repo = np.array([s.endswith("mobipy")
                                       for s in python_path])
        root_candidate = set(np.array(os.sys.path)[looks_like_my_repo])
        if len(root_candidate) > 1 or len(root_candidate) < 1:
            raise IndexError("Repo path cannot be uniquely determined")
        else:
            return os.path.join(list(root_candidate)[0], "")


    def __repr__(self):
        return self.app
