from random import randint
from datetime import datetime
from faker import Faker
import json 


def generate_mock_transactions(): 
    faker = Faker()
    action = ["DEPOSIT","WITHDRAWAL"]
    return {
        "action": action[randint(0,1)],
        "user-id": randint(1, 50),
        "tx_id": f'TX-#{randint(10000000,90000000000)}',
        "amount": randint(700000,10000000),
        "timestamp": datetime.timestamp()
        
    }