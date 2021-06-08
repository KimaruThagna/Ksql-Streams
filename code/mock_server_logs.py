from random import randint
from datetime import datetime

def generate_mock_logs(): 
    log_status = ["ERROR","SUCCESS","WARNING","HEALTHCHECK"]
    return {
        'date':datetime.now(),
        "url": f'https://www.mockeserver.com/AP{randint(56786878,5678787878)}HIJ',
        "status": log_status[randint(0,3)]
    }   
    