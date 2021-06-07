from random import randint
from faker import Faker
import json

def generate_mock_product_ratings(): 
    faker = Faker()
    return json.dumps({
        "userid": randint(1,2000),
        "productid": randint(100,2000),
        "description": faker.description(),
        "rating": randint(1,5)
    })