# eCeipt — AWS Receipt Parser

**eCeipt** is an AWS cloud-native project designed to automate the process of extracting information from uploaded receipt files and sending a parsed summary via email. Built with serverless technologies and AWS native services, the system is event-driven and real-time.

## 🚀 Features

- Upload receipts (PDF format) to an S3 bucket
- Automatically parses receipt content using Amazon Textract
- Extracted fields (e.g., vendor, total, items) are stored in DynamoDB
- Summary email is sent to a predefined email address using Amazon SES
- Fully serverless: triggers Lambda function on file upload

---

## 🧱 Architecture

**Technologies & Services Used:**

- **Amazon S3** – stores uploaded receipts
- **Amazon Lambda** – core for receipt parsing and emailing
- **Amazon Textract** – extracts text from uploaded PDFs
- **Amazon DynamoDB** – stores parsed metadata
- **Amazon SES** – sends summary emails
- **IAM** – secure access across services
- **CloudWatch** – centralized logs for debugging

---

## 🛠️ Setup Instructions

1. **Create an S3 bucket** with a folder named `incoming/`
2. **Create a DynamoDB table** named `Receipts`
   - Primary key: `receipt_id` (String)
   - Sort (optional): `date` (String)
3. **Configure SES**
   - Verify both sender and recipient emails
   - (Move SES out of sandbox for full deployment)
4. **Create IAM Role**
   - Name: `ReceiptProcessingLambdaRole`
   - Trusted entity: Lambda
   - Policies:
     - `AmazonS3ReadOnlyAccess`
     - `AmazonTextractFullAccess`
     - `AmazonDynamoDBFullAccess`
     - `AmazonSESFullAccess`
     - `AWSLambdaBasicExecutionRole`
5. **Create Lambda Function**
   - Name: `ReceiptProcessor`
   - Runtime: Python 3.9
   - Attach IAM Role
   - Configure Env Variables:
      - `DYNAMODB_TABLE`
      - `SES_RECIPIENT_EMAIL`
      - `SES_SENDER_EMAIL`
   - Deploy parsing code
6. **Set up S3 Event Trigger**
   - Event type: ObjectCreated
   - Prefix: `incoming/`
   - Destination: Lambda function

---

## 📊 Architectural Diagram
Below is the high-level architecture for this project, illustrating how AWS services interact with one another in a serverless pipeline:

<img width="1200" height="800" alt="AWS (2025) horizontal framework" src="https://github.com/user-attachments/assets/a66a0b7e-ead9-4ced-9eb4-9d896ad64d32" />
