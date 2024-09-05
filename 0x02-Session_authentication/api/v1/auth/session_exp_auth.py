#!/usr/bin/env python3
"""
SessionExpAuth module for the API
"""
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """
    SessionExpAuth class to manage API authentication with expiration
    """

    def __init__(self):
        """
        Initialize SessionExpAuth
        """
        super().__init__()
        try:
            self.session_duration = int(getenv('SESSION_DURATION', '0'))
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """
        Create a Session ID with expiration
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dictionary = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Return User ID based on Session ID, considering expiration
        """
        if session_id is None:
            return None
        session_dictionary = self.user_id_by_session_id.get(session_id)
        if session_dictionary is None:
            return None
        if self.session_duration <= 0:
            return session_dictionary.get('user_id')
        created_at = session_dictionary.get('created_at')
        if created_at is None:
            return None
        exp_time = created_at + timedelta(seconds=self.session_duration)
        if exp_time < datetime.now():
            return None
        return session_dictionary.get('user_id')
