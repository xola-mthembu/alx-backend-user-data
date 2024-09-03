#!/usr/bin/env python3
"""
This module provides basic authentication methods for the API.
"""
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """Class to handle basic authentication for the API."""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the Base64 encoded part of the Authorization header.

        Args:
            authorization_header (str): The full Authorization header string.

        Returns:
            str: The Base64 encoded string, or None if not found.
        """
        if not authorization_header or not isinstance(authorization_header,
                                                      str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """
        Decodes the Base64 encoded authorization header.

        Args:
            base64_authorization_header (str): The Base64 encoded string.

        Returns:
            str: The decoded string, or None if decoding fails.
        """
        if (not base64_authorization_header or
                not isinstance(base64_authorization_header, str)):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """
        Splits the decoded Base64 string into user credentials.

        Args:
            decoded_base64_authorization_header (str): The decoded Base64
            string.

        Returns:
            tuple: (user_email, user_password) or (None, None) if invalid.
        """
        if (not decoded_base64_authorization_header or
                not isinstance(decoded_base64_authorization_header, str)):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        user_email, user_password = decoded_base64_authorization_header.split(
            ':', 1)
        return user_email, user_password

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        Retrieves a User object using email and password.

        Args:
            user_email (str): The user's email.
            user_pwd (str): The user's password.

        Returns:
            User: The user object if found and password is correct, otherwise
            None.
        """
        if not user_email or not isinstance(user_email, str):
            return None
        if not user_pwd or not isinstance(user_pwd, str):
            return None
        try:
            user_list = User.search({'email': user_email})
        except Exception:
            return None
        for user in user_list:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the User instance based on the request.

        Args:
            request (flask.Request): The request object.

        Returns:
            User: The current user if authentication is successful, otherwise
            None.
        """
        header_auth = self.authorization_header(request)
        if header_auth is None:
            return None

        encoded_token = self.extract_base64_authorization_header(header_auth)
        if encoded_token is None:
            return None

        decoded_token = self.decode_base64_authorization_header(encoded_token)
        if decoded_token is None:
            return None

        email, pwd = self.extract_user_credentials(decoded_token)
        if email is None or pwd is None:
            return None

        return self.user_object_from_credentials(email, pwd)
