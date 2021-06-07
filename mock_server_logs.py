from random import randint
from datetime import datetime

def generate_mock_logs(): 
    log_status = ["ERROR","SUCCESS","WARNING","HEALTHCHECK"]
    return f'[{datetime.now()}]-https://www.mockeserver.com/AP{randint(56786878,5678787878)}HIJ STATUS {log_status[randint(0,3)]}'