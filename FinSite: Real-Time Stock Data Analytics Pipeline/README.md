# FinSite – Real-Time Stock Data Analytics Pipeline on AWS

**FinSite** is a real-time, serverless analytics pipeline that ingests, processes, stores, and analyzes live stock market data using a suite of AWS services.  

---

## 🚀 Features

- Real-time stock data ingestion with **Amazon Kinesis Data Streams**
- Processing data and detecting anomalies using **AWS Lambda**
- Storage of recent data in **Amazon DynamoDB** for querying
- Long-term storage of raw data in **Amazon S3**
- Historical query capability with **Amazon Athena**
- Real-time alerts via **Amazon Lambda & Amazon SNS** (Email/SMS)

---

## 🧱 Architecture

**Technologies & Services Used:**

| Service                  | Role in the System |
|--------------------------|---------------------|
| **Amazon Kinesis Data Streams** | Ingests live stock ticker data |
| **AWS Lambda**           | Processes real-time events and identifies trends |
| **Amazon DynamoDB**      | Stores structured stock data for quick access and lookups |
| **Amazon S3**            | Archives raw stock data for historical analysis |
| **Amazon Athena**        | Runs SQL-like queries on stock data stored in S3 |
| **Amazon SNS**           | Sends trend alerts via email or SMS |
| **IAM Roles & Policies** | Secures service-to-service communication and access |

---
