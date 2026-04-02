# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using FastAPI, including routing, request handling, and JSON responses.

## 📝 Tasks

### 🛠️ Build the API endpoints

#### Description
Create endpoints for managing a small collection of items, including listing items, retrieving a single item, and adding new items.

#### Requirements
Completed program should:

- Use FastAPI to define routes for GET and POST requests
- Return JSON responses for API clients
- Validate input data for new items
- Include at least one endpoint that returns a filtered or specific item by ID

### 🛠️ Add request validation and user feedback

#### Description
Implement request validation and clear response messages for successful and invalid requests.

#### Requirements
Completed program should:

- Validate incoming POST data using Pydantic models
- Return a 201 response for successfully created items
- Return a 400 response for invalid input
- Provide meaningful error or success messages in JSON format
