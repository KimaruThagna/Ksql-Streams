from random import randint
from datetime import datetime
import json
def generate_mock_logs(): 
    log_status = ["ERROR","SUCCESS","WARNING","HEALTHCHECK"]
    return json.dumps({"date": f'[{datetime.now()}]',
            "url": f'https://www.mockeserver.com/AP{randint(56786878,5678787878)}HIJ',
            "status":f'{log_status[randint(0,3)]}'
    })