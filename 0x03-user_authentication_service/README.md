# 0x03. User Authentication Service

This project implements a user authentication service using Python, Flask, and SQLAlchemy. It covers various aspects of user management, including registration, login, session handling, and password reset functionality.

## Features

- User registration
- User login and logout
- Password hashing
- Session management
- Password reset functionality

## Requirements

- Python 3.7 or higher
- Flask
- SQLAlchemy
- bcrypt

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-username/alx-backend-user-data.git
   ```

2. Navigate to the project directory:
   ```
   cd alx-backend-user-data/0x03-user_authentication_service
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```
   python3 app.py
   ```

## Usage

The application provides various endpoints for user authentication and management. Refer to the individual files for detailed implementation of each feature.

## Files

- `user.py`: Defines the User model
- `db.py`: Handles database operations
- `auth.py`: Implements authentication logic
- `app.py`: Contains the Flask application and routes
- `main.py`: Includes end-to-end integration tests
