
class StringUtils:
    
    LF = "\n"
    
    CR = "\r"
    
    EMPTY = ""
    
    SPACE = " "
    
    @staticmethod
    def remove_lf(value:str):       
        return StringUtils.replace(value, StringUtils.LF, StringUtils.EMPTY)
    
    @staticmethod
    def remove_cr(value:str):
        return StringUtils.replace(value, StringUtils.CR, StringUtils.EMPTY)
    
    @staticmethod
    def replace(value:str, source_str:str, target_str:str):
        if value == None:
            return value
        
        return value.replace(source_str, target_str)
    
    @staticmethod
    def length(value:str):
        if value == None:
            return 0
        
        return len(value)
        