#!/usr/bin/env python3
"""
SessionDBAuth module for the API
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """
    SessionDBAuth class to manage API authentication with database storage
    """

    def create_session(self, user_id=None):
        """
        Create and store new instance of UserSession and return Session ID
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Return User ID by requesting UserSession in the database
        """
        if session_id is None:
            return None
        UserSession.load_from_file()
        user_session = UserSession.search({'session_id': session_id})
        if not user_session:
            return None
        user_session = user_session[0]
        expired = super().user_id_for_session_id(session_id)
        if expired is None:
            return None
        return user_session.user_id

    def destroy_session(self, request=None):
        """
        Destroy UserSession based on Session ID from request cookie
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False
        user_session = UserSession.search({'session_id': session_id})
        if not user_session:
            return False
        user_session = user_session[0]
        user_session.remove()
        return True
