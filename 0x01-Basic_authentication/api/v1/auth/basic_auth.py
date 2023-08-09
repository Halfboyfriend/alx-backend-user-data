#!/usr/bin/env python3
"""A basic authentication frame that inherits from Auth"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """basic auth class"""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Authorizationn with base64"""
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        
        if not authorization_header.startswith('Basic '):
            return None
        
        return authorization_header[len('Basic '):]
    

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        '''pass'''
        if base64_authorization_header is None or not isinstance(base64_authorization_header, str):
            return None
        
        