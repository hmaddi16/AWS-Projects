# FinSite – Real-Time Stock Data Analytics Pipeline on AWS

**FinSite** is a real-time, serverless analytics pipeline that ingests, processes, stores, and analyzes live stock market data using a suite of AWS services.  
Designed for scalability and low latency, the system enables immediate trend detection and alerting, while supporting historical querying and fast lookups.

---

## 🚀 Features

- Real-time stock data ingestion with **Amazon Kinesis Data Streams**
- Stream processing and trend detection using **AWS Lambda**
- Structured storage of recent data in **Amazon DynamoDB**
- Long-term storage of raw data in **Amazon S3**
- Historical query capability with **Amazon Athena**
- Real-time alerts via **Amazon SNS** (Email/SMS)
- Secure, role-based access control with **IAM**

---

## 🧱 Architecture

**Core AWS Services:**

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
