import os, time, json
from kafka import KafkaProducer
from random import choices, randint
from .mock_ratings import generate_mock_product_ratings
from .mock_server_logs import generate_mock_logs
from .mock_transactions import generate_mock_transactions

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC = os.environ.get("TRANSACTIONS_TOPIC")
RATINGS_TOPIC = os.environ.get("RATINGS_TOPIC")
LOGS_TOPIC = os.environ.get("LOGS_TOPIC")


producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER_URL,
                         #json encode all values
                         value_serializer=lambda value: json.dumps(value).encode(),)

while True:
    transaction = generate_mock_transactions()
    rating = generate_mock_product_ratings()
    log = generate_mock_logs()
    # Kafka messages are sent in bytes
    print("sending to transactions topic")
    producer.send(TRANSACTIONS_TOPIC, value=transaction) 
    print("sending to logs topic")
    producer.send(LOGS_TOPIC, value=log) 
    print("sending to ratings topic")
    producer.send(RATINGS_TOPIC, value=rating) 