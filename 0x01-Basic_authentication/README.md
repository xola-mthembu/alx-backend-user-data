# 0x01. Basic Authentication

This project involves implementing a basic authentication system for a simple API. The project includes setting up error handlers, creating an authentication class, and implementing basic authentication methods.

## Directory Structure

- `api/v1/auth/`: Contains the authentication-related modules.
- `api/v1/views/`: Contains the view-related modules.
- `api/v1/app.py`: Main application file that sets up the Flask app and handles requests.

## Requirements

- Python 3.7 on Ubuntu 18.04 LTS
- All Python scripts must be executable and use `#!/usr/bin/env python3` as the shebang.
- Code must follow the `pycodestyle` (version 2.5) style guidelines.
- Ensure all modules, classes, and functions are documented.

## Setup and Installation

1. Install dependencies using pip:
    ```sh
    pip3 install -r requirements.txt
    ```
2. Start the server:
    ```sh
    API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
    ```
3. Test the API endpoints using `curl` or any HTTP client.

## Tasks Overview

### Task 0: Simple-basic-API
Set up a simple API and start the server.

### Task 1: Error handler: Unauthorized
Implement a 401 error handler for unauthorized requests.

### Task 2: Error handler: Forbidden
Implement a 403 error handler for forbidden requests.

### Task 3: Auth class
Create an `Auth` class to manage the API authentication.

### Task 4: Define which routes don't need authentication
Update the `Auth` class to exclude certain routes from requiring authentication.

### Task 5: Request validation!
Implement request validation in the `Auth` class to ensure the correct authorization header is present.

### Task 6-13: Further development
Implement additional methods and extend the `Auth` and `BasicAuth` classes to handle different authentication scenarios and edge cases.

## How to Use

- Start the Flask server as shown in the setup instructions.
- Use `curl` commands to interact with the API endpoints and test different scenarios.
