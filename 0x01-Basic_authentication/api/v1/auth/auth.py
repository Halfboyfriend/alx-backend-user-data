#!/usr/bin/env python3
"""authentication class"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class"""
    def require_auth(self, 
                     path: str, 
                     excluded_paths: List[str]
                     ) -> bool:
        """Returns False, path and excluded path"""
        return f'{False} - {path} {excluded_paths}'
    

    def authorization_header(self, request=None) -> str:
        """Returns None"""
        return f'{None} - {request}'
    
    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None"""
        return f'{None} - {request}'
