import os

def abs_path(rel_path):
    return os.path.join(os.path.dirname(__file__), rel_path)