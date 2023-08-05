#!/usr/bin/env python3
"""User passwords should NEVER be stored in plain text in a database."""
import bcrypt
from bcrypt import hashpw


def hash_password(password: str) -> bytes:
    """
    Hashed Password
    :param password:
    :return:
    """
    b = password.encode()
    hashed = hashpw(b, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Password validator
    :param hashed_password:
    :param password:
    :return:
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
