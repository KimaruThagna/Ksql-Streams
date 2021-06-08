from datetime import datetime
from random import randint
from faker import Faker

def generate_mock_product_ratings(): 
    faker = Faker()
    return {
        "date": datetime.now().timestamp(),
        "userid": randint(1,100),
        "productid": randint(100,200),
        "description": faker.text(20),
        "rating": randint(1,5)
    }
