# Ksql-Streams
Learning stream processing using KSQL on top of Apache Kafka

I will be using this project to demonstrate real time analytics and also anomaly detection.
The use cases covered will be:

1. Anomaly detection- Use data generated from `mock_server_logs.py` in real time to perform anomaly detection. We will be checking for errors within a certain time frame. eg, if number of errors exceed 5 within 1 minute. This mimics the cloudwatch metrics in AWS.

2. Real time analytics for a product shop- Assume a high end online shop sells products and the business is very sensitive to bad ratings. The business would like to detect a bad rating as soon as it happens. This will then allow customer relations team to folow up. We will use KSQL to filter out bad ratings(less than 3 out of 5). We will use data from `mock_ratings.py`

3. Fraud detection using streaming analytics- Use bank transactional data generated by `mock_transactions.py` to provide a stream of transation actions. To detect possible fraud, we will filter out transactions with large withdrawal amounts.(greater than 1000000).

# Concepts
**Stream** Immutable sequence of events of data coming into a Kafka topic. Good for real time granular analysis

**Topic** A structure that represents the current state of data coming into a stream. 
Consider it as the sum total of all events in the stream at a certain point in time. Just like a normal SQL table. Good for aggregate and grouping analysis

# Producer
The producer for this demo is in `common_producer.py`. This will produce transactions logs and rating records for the KSQL Demo.

# Setup
The setup involves 2 `docker-compose` files. One that spins up the KAFKA clusters, ksqldb and ksql-CLI instances and one that spins the local project that contains the producer.

Spin the Kafka cluster
``` 
docker-compose -f docker-compose.kafka.yaml up
```

Spin the app cluster that contains producer code

```
 docker-compose up
```

# Inspect different topics

## Transaction topic

```
docker-compose -f docker-compose.kafka.yml exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic transactions_topic
```

## Logs topic

```
docker-compose -f docker-compose.kafka.yml exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic logs_topic
```

## Ratings topic

```
docker-compose -f docker-compose.kafka.yml exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic ratings_topic
```

# KSQL Interactions

To connect to the KSQL CLI, run the command

## Create Stream and Tables
### Log Topic
A stream will monitor errors from  `logs_topic` and record when there is an error status 5 or more times within a 1 minute window.



A table would be used to store the total number of events per status from beginning till now.


## Transactions Topic

This stream will be created to filter out withdrawals above 1,000,000 as possible transactions of concern


A table can store records of possible illegal withdrawals where there are withdrawals of over 5,000,000 within 1 day per user.



A table can be generated to store the running sum of withdrawal and deposit amounts for each user.



## Ratings Topic

A stream can be created to record bad ratings where the value is less than 3.



A table can be created to rank the worst performing products by ratings


# Tear down
To bring down kafka cluster `docker-compose -d docker-compose.kafka.yaml down`

To bring down project 

`docker-compose down` 

To remove project network

`docker network rm kafka-network` 
