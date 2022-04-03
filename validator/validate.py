import os
from validator import exception
class CheckInput:
    
    def __init__(self, input) -> None:
        self._input = input
        self.is_exist()
    
    def is_exist(self):
        if os.path.isfile(self._input) or os.path.isdir(self._input):
            return True
        raise exception.TreeException("The '{}' does not exist as a file or Directory\n".format(self._input)+
            "Plese check your output or provide the absolute path")
