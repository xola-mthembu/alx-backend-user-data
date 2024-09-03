#!/usr/bin/env python3
"""
This module handles the authentication for the API.
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """A class to manage API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines whether a given path requires authentication.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): list of paths that do not require auth.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        if not path or not excluded_paths:
            return True

        trimmed_path = path.rstrip('/')

        for exclusion in excluded_paths:
            if exclusion.endswith('*'):
                if trimmed_path.startswith(exclusion[:-1]):
                    return False
            elif trimmed_path == exclusion.rstrip('/'):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the incoming request.

        Args:
            request (flask.Request): The request object.

        Returns:
            str: The Authorization header if present, None otherwise.
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user associated with the request.

        Args:
            request (flask.Request): The request object.

        Returns:
            TypeVar('User'): The current user, if available.
        """
        return None
