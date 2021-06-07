from random import randint
from faker import Faker

def generate_mock_product_ratings(): 
    faker = Faker()
    return {
        "userid": randint(1,100),
        "productid": randint(100,200),
        "description": faker.description(),
        "rating": randint(1,5)
    }