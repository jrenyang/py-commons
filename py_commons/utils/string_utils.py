
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
    
    # 轉駝峰命名
    @staticmethod
    def to_camel_case(value):
        result = ""
        str = value.split("_")

        for v in str:
            result += v.capitalize()

        return result

    # 欄位轉駝峰命名
    @staticmethod
    def field_to_camel_case(value):
        result = None
        str = value.split("_")

        if str:
            result = str[0].lower()

        for v in str[1:]:
            result += v.capitalize()

        return result
    
    # 取得字串長度
    @staticmethod
    def length(value:str):
        if value == None:
            return 0
        
        return len(value)
        