#!/usr/bin/env python3
"""
Write a function called filter_datum that returns the
log message obfuscated:
"""
from typing import List
import re


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str):
    """
    :param fields:
    :param redaction:
    :param message:
    :param separator:
    :return:
    """
    for field in fields:
        message = re.sub(field + '=.*?' + separator,
                         field + '=' + redaction + separator, message)
    return message
