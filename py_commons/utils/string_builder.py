from io import StringIO
from py_commons.utils.string_utils import StringUtils

class StringBuilder:
 
    def __init__(self):
        self._string = StringIO()
 
    def append(self, param1:any=None, param2:any=None, param3:any=None):
        if isinstance(param1, bool) and isinstance(param2, str) and isinstance(param3, str):
            self._condition_append(param1, param2, param3)
        elif isinstance(param1, str):
            self._append(param1)
        return self
    
    def _append(self, str1:str):
        self._string.write(str1)

    def _condition_append(self, condition:bool, str1:str, str2:str):
        if(condition):
            self._string.write(str1)
        else:
            self._string.write(str2)
        return self
    
    def new_line(self):
        self._string.write(StringUtils.LF)
        return self
    
    def to_string(self):
        return self._string.getvalue()
 
    def __str__(self):
        return self._string.getvalue() 