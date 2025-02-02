# Feature Toggle API

A Flask-based REST API for managing feature toggles with MongoDB backend, designed for seamless feature flag management across different packages.

## Table of Contents
- [Technologies](#technologies)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Error Handling](#error-handling)

## Technologies

- Python 3.9
- Flask (Web Framework)
- MongoDB (Database)
- Flasgger (Swagger Documentation)
- Vercel (Deployment Platform)

## Prerequisites

- Python 3.9 or higher
- MongoDB Atlas account
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd feature-toggle-api
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```plaintext
DB_CONNECTION_STRING=your-mongodb-connection-string
DB_NAME=your-database-name
DB_USERNAME=your-mongodb-username
DB_PASSWORD=your-mongodb-password
```

## API Endpoints

### Feature Toggle Management

#### Create Feature Toggle
- **POST** `/feature-toggle`
- Creates a new feature toggle
- Required body parameters:
  - package_name (string)
  - name (string)
  - description (string)
  - beginning_date (string: YYYY-MM-DD HH:MM:SS)
  - expiration_date (string: YYYY-MM-DD HH:MM:SS)

#### Get Feature Toggles
- **GET** `/feature-toggles/{package_name}`
- Retrieves all feature toggles for a specific package

#### Get Specific Feature Toggle
- **GET** `/feature-toggle/{package_name}/{feature_id}`
- Retrieves details of a specific feature toggle

#### Get Active Feature Toggles
- **GET** `/feature-toggles/{package_name}/active`
- Retrieves all currently active feature toggles

#### Get Feature Toggles by Date
- **GET** `/feature-toggles/{package_name}/by-date?date={YYYY-MM-DD}`
- Retrieves feature toggles active on a specific date

#### Update Feature Toggle Dates
- **PUT** `/feature-toggle/{package_name}/{feature_id}/update-dates`
- Updates the beginning and/or expiration dates of a feature toggle

#### Update Feature Toggle Name
- **PUT** `/feature-toggle/{package_name}/{feature_id}/update-name`
- Updates the name of a feature toggle

#### Delete Feature Toggle
- **DELETE** `/feature-toggle/{package_name}/{feature_id}`
- Deletes a specific feature toggle

#### Delete All Feature Toggles in Package
- **DELETE** `/feature-toggles/{package_name}`
- Deletes all feature toggles in a specific package

#### Delete All Feature Toggles (Testing)
- **DELETE** `/feature-toggles`
- Deletes all feature toggles across all packages

## Deployment

This API is configured for deployment on Vercel. The deployment configuration is specified in `vercel.json`:

```json
{
    "version": 2,
    "builds": [
        {
            "src": "app.py",
            "use": "@vercel/python"
        }
    ],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "app.py"
        }
    ]
}
```

## Error Handling

The API includes comprehensive error handling for:
- Invalid date formats
- Database connection issues
- Missing or invalid parameters
- Resource not found scenarios
- Logical date validation (e.g., beginning date before expiration date)

All error responses follow a consistent format:
```json
{
    "error": "Error message description"
}
```

## Swagger Documentation

The API includes Swagger documentation accessible at `/apidocs` when running locally. This provides interactive documentation for testing and exploring the API endpoints.

---

For additional questions or support, please open an issue in the repository.
