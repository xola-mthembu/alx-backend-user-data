# Session Authentication

This project implements a Session Authentication system for a simple HTTP API. It builds upon the Basic Authentication system and adds session-based authentication.

## Files

- `api/v1/app.py`: Main application file
- `api/v1/views/users.py`: Views for user-related routes
- `api/v1/auth/auth.py`: Base authentication class
- `api/v1/auth/session_auth.py`: Session authentication class
- `api/v1/views/session_auth.py`: Views for session authentication routes
- `api/v1/auth/session_exp_auth.py`: Session authentication with expiration
- `api/v1/auth/session_db_auth.py`: Session authentication with database storage
- `models/user_session.py`: UserSession model for database storage

## Setup

1. Install dependencies:
