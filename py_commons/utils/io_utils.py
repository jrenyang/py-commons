"""
The IoUtils module: Support for IO
"""

import os

class IoUtils:
    
    @staticmethod
    def write(dir:str, file_name:str, content:any):
        if isinstance(dir, str) and isinstance(file_name, str) and isinstance(content, str):
            IoUtils._str_write_to_file(dir, file_name, content)
            
    @staticmethod
    def _str_write_to_file(dir:str, file_name:str, content:str, encoding:str="utf-8"):
        IoUtils._write(dir, file_name, content, 'w', encoding)
    
    @staticmethod
    def _write(dir, file_name, content, mode, encoding):
        with open(os.path.join(dir, file_name), mode, encoding=encoding) as f:
            f.write(content)
            
            