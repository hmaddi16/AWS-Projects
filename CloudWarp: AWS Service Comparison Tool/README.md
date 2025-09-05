# AWS Service Comparison Tool

A full-stack web application for comparing AWS services across categories, features, and pricing models. Built with React TypeScript frontend and Python FastAPI backend.

## Features

- **Service Browsing**: View all AWS services with detailed information
- **Category Filtering**: Filter services by categories (Compute, Storage, Database, etc.)
- **Side-by-Side Comparison**: Compare multiple services simultaneously
- **Detailed Service Information**: 
  - Service descriptions
  - Key features
  - Pricing models and notes
  - Free tier information
  - Common use cases
- **Responsive Design**: Works on desktop and mobile devices
- **Real-time API**: FastAPI backend with automatic API documentation

## Project Structure

```
cloud-service-comparison/
├── backend/                 # Python FastAPI backend
│   ├── main.py             # Main FastAPI application
│   └── requirements.txt    # Python dependencies
├── frontend/               # React TypeScript frontend
│   ├── public/
│   │   └── index.html      # Main HTML template
│   ├── src/
│   │   ├── components/     # React components
│   │   │   ├── ServiceCard.tsx
│   │   │   └── ServiceComparison.tsx
│   │   ├── services/       # API service layer
│   │   │   └── api.ts
│   │   ├── types/          # TypeScript type definitions
│   │   │   └── aws.ts
│   │   ├── App.tsx         # Main App component
│   │   └── index.tsx       # React entry point
│   ├── package.json        # Node.js dependencies
│   └── tsconfig.json       # TypeScript configuration
└── README.md               # This file
```

## Technology Stack

### Frontend
- **React 18.2.0** - UI library
- **TypeScript 4.9.5** - Type-safe JavaScript
- **Axios 1.6.2** - HTTP client for API calls
- **React Scripts 5.0.1** - Create React App toolchain

### Backend
- **FastAPI 0.104.1** - Modern Python web framework
- **Pydantic 2.5.0** - Data validation using Python type hints
- **Uvicorn 0.24.0** - ASGI server for running the API
- **Python 3.8+** - Programming language

## Getting Started

### Prerequisites

- **Node.js** (v14 or higher)
- **Python** (3.8 or higher)
- **npm** or **yarn**
- **pip** (Python package installer)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the FastAPI server:
   ```bash
   python main.py
   ```
   
   Or using uvicorn directly:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

4. The backend API will be available at:
   - **API**: http://localhost:8000
   - **Interactive API Documentation**: http://localhost:8000/docs
   - **ReDoc Documentation**: http://localhost:8000/redoc

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

4. The frontend will be available at:
   - **Application**: http://localhost:3000

## API Endpoints

### Available Endpoints

- `GET /` - API status and version
- `GET /services` - Get all AWS services (with optional category filter)
- `GET /services/{service_id}` - Get specific service by ID
- `GET /categories` - Get all available service categories
- `GET /categories/{category_name}/services` - Get services by category

### Example API Usage

```bash
# Get all services
curl http://localhost:8000/services

# Get services in a specific category
curl http://localhost:8000/services?category=Compute

# Get all categories
curl http://localhost:8000/categories

# Get specific service
curl http://localhost:8000/services/ec2
```

## Usage

1. **Browse Services**: View all available AWS services on the main page
2. **Filter by Category**: Use the dropdown to filter services by category
3. **Select Services**: Click on service cards to add them to comparison
4. **Compare Services**: View selected services side-by-side in the comparison section
5. **Remove Services**: Click the × button to remove services from comparison

## Development

### Running in Development Mode

1. Start the backend server:
   ```bash
   cd backend && python main.py
   ```

2. Start the frontend development server:
   ```bash
   cd frontend && npm start
   ```

### Building for Production

1. Build the React frontend:
   ```bash
   cd frontend && npm run build
   ```

2. The built files will be in the `frontend/build` directory

