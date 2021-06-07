import os, time, json
from kafka import KafkaProducer
from random import choices, randint
from string import ascii_letters, digits

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC = os.environ.get("TRANSACTIONS_TOPIC")


producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER_URL,
                         #json encode all values
                         value_serializer=lambda value: json.dumps(value).encode(),)

while True:
    transaction = create_random_transaction()
    # Kafka messages are sent in bytes
    producer.send(TRANSACTIONS_TOPIC, value=transaction) 