# Ksql-Streams
Learning stream processing using KSQL on top of Apache Kafka

I will be using this project to demonstrate real time analytics and also anomaly detection.
The use cases covered will be:

1. Anomaly detection- Use data generated from `mock_server_logs.py` in real time to perform anomaly detection. We will be checking for errors within a certain time frame. eg, if number of errors exceed 5 within 1 minute. This mimics the cloudwatch metrics in AWS.

2. Real time analytics for a product shop- Assume a high end online shop sells products and the business is very sensitive to bad ratings. The business would like to detect a bad rating as soon as it happens. This will then allow customer relations team to folow up. We will use KSQL to filter out bad ratings(less than 3 out of 5). We will use data from `mock_ratings.py`

3. Fraud detection using streaming analytics-