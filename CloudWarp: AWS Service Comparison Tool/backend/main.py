from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel
import json

app = FastAPI(title="AWS Service Comparison API", version="1.0.0")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AWSService(BaseModel):
    id: str
    name: str
    category: str
    description: str
    key_features: List[str]
    pricing_model: str
    pricing_notes: str
    use_cases: List[str]
    free_tier: Optional[str] = None

class ServiceCategory(BaseModel):
    name: str
    services: List[AWSService]

# Sample AWS services data
AWS_SERVICES = [
    AWSService(
        id="ec2",
        name="Amazon EC2",
        category="Compute",
        description="Secure and resizable compute capacity in the cloud",
        key_features=[
            "Virtual servers in the cloud",
            "Multiple instance types and sizes",
            "Auto Scaling",
            "Elastic Load Balancing",
            "Amazon EBS storage"
        ],
        pricing_model="Pay-as-you-use",
        pricing_notes="Pricing varies by instance type, region, and usage. On-Demand, Reserved, and Spot pricing available.",
        use_cases=[
            "Web applications",
            "Development and testing",
            "High-performance computing",
            "Machine learning"
        ],
        free_tier="750 hours per month for 12 months (t2.micro or t3.micro)"
    ),
    AWSService(
        id="s3",
        name="Amazon S3",
        category="Storage",
        description="Object storage built to store and retrieve any amount of data from anywhere",
        key_features=[
            "99.999999999% durability",
            "Multiple storage classes",
            "Lifecycle management",
            "Cross-region replication",
            "Server-side encryption"
        ],
        pricing_model="Pay-as-you-use",
        pricing_notes="Pricing based on storage amount, requests, and data transfer. Different rates for storage classes.",
        use_cases=[
            "Backup and restore",
            "Data archiving",
            "Static website hosting",
            "Content distribution"
        ],
        free_tier="5 GB of standard storage for 12 months"
    ),
    AWSService(
        id="rds",
        name="Amazon RDS",
        category="Database",
        description="Managed relational database service for MySQL, PostgreSQL, Oracle, SQL Server, and MariaDB",
        key_features=[
            "Automated backups",
            "Multi-AZ deployments",
            "Read replicas",
            "Automated software patching",
            "Database snapshots"
        ],
        pricing_model="Pay-as-you-use",
        pricing_notes="Pricing based on instance class, storage, backup storage, and data transfer.",
        use_cases=[
            "Web and mobile applications",
            "E-commerce platforms",
            "Enterprise applications",
            "Analytics workloads"
        ],
        free_tier="750 hours of db.t2.micro instance for 12 months"
    ),
    AWSService(
        id="lambda",
        name="AWS Lambda",
        category="Compute",
        description="Run code without thinking about servers or clusters",
        key_features=[
            "Event-driven execution",
            "Automatic scaling",
            "Built-in fault tolerance",
            "Support for multiple languages",
            "Pay per request"
        ],
        pricing_model="Pay-per-request",
        pricing_notes="Pricing based on number of requests and compute time. First 1M requests per month are free.",
        use_cases=[
            "API backends",
            "Data processing",
            "Real-time file processing",
            "IoT backends"
        ],
        free_tier="1M requests and 400,000 GB-seconds per month"
    ),
    AWSService(
        id="dynamodb",
        name="Amazon DynamoDB",
        category="Database",
        description="Fast and flexible NoSQL database service for any scale",
        key_features=[
            "Single-digit millisecond latency",
            "Automatic scaling",
            "Built-in security",
            "Global tables",
            "DynamoDB Streams"
        ],
        pricing_model="Pay-as-you-use",
        pricing_notes="Pricing based on read/write capacity, storage, and additional features like backups and streams.",
        use_cases=[
            "Mobile applications",
            "Gaming applications",
            "IoT applications",
            "Real-time analytics"
        ],
        free_tier="25 GB storage, 2.5M reads, 1M writes per month"
    ),
    AWSService(
        id="cloudfront",
        name="Amazon CloudFront",
        category="Networking",
        description="Global content delivery network (CDN) service",
        key_features=[
            "Global edge locations",
            "DDoS protection",
            "SSL/TLS encryption",
            "Real-time metrics",
            "Lambda@Edge"
        ],
        pricing_model="Pay-as-you-use",
        pricing_notes="Pricing based on data transfer out, HTTP/HTTPS requests, and additional features.",
        use_cases=[
            "Website acceleration",
            "Video streaming",
            "API acceleration",
            "Software distribution"
        ],
        free_tier="1 TB data transfer out and 10M requests for 12 months"
    ),
    AWSService(
        id="iam",
        name="AWS IAM",
        category="Security",
        description="Identity and Access Management service",
        key_features=[
            "Fine-grained permissions",
            "Multi-factor authentication",
            "Identity federation",
            "Access analyzer",
            "Temporary credentials"
        ],
        pricing_model="Free",
        pricing_notes="IAM is provided at no additional charge. You pay only for use of other AWS services by your users.",
        use_cases=[
            "User access management",
            "Application authentication",
            "Cross-account access",
            "Compliance requirements"
        ],
        free_tier="Always free"
    ),
    AWSService(
        id="vpc",
        name="Amazon VPC",
        category="Networking",
        description="Virtual private cloud for isolated cloud resources",
        key_features=[
            "Private subnets",
            "Security groups",
            "Network ACLs",
            "VPN connections",
            "Internet gateways"
        ],
        pricing_model="Free + usage fees",
        pricing_notes="VPC itself is free. You pay for VPN connections, NAT gateways, and data transfer.",
        use_cases=[
            "Secure cloud infrastructure",
            "Hybrid cloud connectivity",
            "Multi-tier applications",
            "Compliance requirements"
        ],
        free_tier="VPC service is free; some features have usage charges"
    )
]

@app.get("/")
async def root():
    return {"message": "AWS Service Comparison API", "version": "1.0.0"}

@app.get("/services", response_model=List[AWSService])
async def get_services(category: Optional[str] = None):
    """Get all AWS services, optionally filtered by category"""
    if category:
        return [service for service in AWS_SERVICES if service.category.lower() == category.lower()]
    return AWS_SERVICES

@app.get("/services/{service_id}", response_model=AWSService)
async def get_service(service_id: str):
    """Get a specific AWS service by ID"""
    for service in AWS_SERVICES:
        if service.id == service_id:
            return service
    return {"error": "Service not found"}

@app.get("/categories")
async def get_categories():
    """Get all available service categories"""
    categories = list(set(service.category for service in AWS_SERVICES))
    return {"categories": sorted(categories)}

@app.get("/categories/{category_name}/services", response_model=List[AWSService])
async def get_services_by_category(category_name: str):
    """Get all services in a specific category"""
    return [service for service in AWS_SERVICES if service.category.lower() == category_name.lower()]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
