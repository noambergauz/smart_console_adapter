# Smart Console Adapter

## Overview
The Smart Console Adapter is a Python application that provides a REST API using FastAPI. It acts as an adapter to Checkpoint's Smart Console API, allowing users to interact with the API through well-defined endpoints.

## Features
- RESTful API built with FastAPI
- Typed requests and responses using Pydantic models
- Modular architecture with separate directories for models, adapters, and routers

## Project Structure
```
smart_console_adapter
├── src
│   ├── main.py               # Entry point of the application
│   ├── models                 # Contains Pydantic models for requests and responses
│   │   ├── __init__.py
│   │   ├── request_models.py   # Defines request payload models
│   │   └── response_models.py  # Defines response models
│   ├── adapters               # Contains the Smart Console adapter
│   │   ├── __init__.py
│   │   └── smart_console_adapter.py  # Adapter class for Smart Console API
│   ├── routers                # Contains API route definitions
│   │   ├── __init__.py
│   │   └── api.py            # API routes using the adapter
│   └── config                # Configuration settings
│       ├── __init__.py
│       └── settings.py       # Application settings
├── requirements.txt          # Project dependencies
├── pyproject.toml           # Project metadata and dependencies
└── README.md                 # Project documentation
```

## Installation
To install the required dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage
To start the FastAPI application, run the following command:

```
uvicorn src.main:app --reload
```

You can then access the API at `http://127.0.0.1:8000`.

## API Documentation
The automatically generated API documentation can be accessed at `http://127.0.0.1:8000/docs`.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.