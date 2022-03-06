from datetime import datetime, timedelta

class DateUtils:
    
    DATE_DEFULT_FORMATE_YYYYMMDD = '%Y%m%d'
    
    @staticmethod
    def get_current_date(formate:str=DATE_DEFULT_FORMATE_YYYYMMDD):
        return datetime.now().strftime(formate)
    
    @staticmethod
    def add_date(date:str, add:int, formate:str=DATE_DEFULT_FORMATE_YYYYMMDD):
        _date = datetime.strptime(date, formate)
        _date += timedelta(add)
        return _date.strftime(formate)
    
    def minus_date(date:str, add:int, formate:str=DATE_DEFULT_FORMATE_YYYYMMDD):
        _date = datetime.strptime(date, formate)
        _date -= timedelta(add)
        return _date.strftime(formate)