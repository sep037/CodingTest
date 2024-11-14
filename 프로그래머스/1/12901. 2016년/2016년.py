import datetime # 라이브러리 쓰면 사기일까 ?

def solution(a, b):
    date = datetime.date(2016, a, b)
    
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    
    return days[date.weekday()]
