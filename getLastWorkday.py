from datetime import datetime, timedelta
import pandas as pd

def get_previous_workday(date=None):
    if date is None:
        date = datetime.today()
    else:
        date = datetime.strptime(date, "%Y%m%d")
        
    previous_day = date - timedelta(days=1)
    
    while previous_day.weekday() >= 5:  # 5 for Saturday, 6 for Sunday
        previous_day -= timedelta(days=1)
    
    return previous_day.strftime("%Y%m%d")

# 示例调用
print(get_previous_workday())  # 获取今天的上一个工作日
# 或者指定日期：
print(get_previous_workday("20241107"))  # 指定日期为2024年11月7日