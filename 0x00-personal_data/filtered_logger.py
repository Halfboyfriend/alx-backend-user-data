#!/usr/bin/env python3
"""
Write a function called filter_datum that returns the
log message obfuscated:
"""
from typing import List
import re


def filter_datum(fields: List, redaction: str, message: str, separator: str):
    """
    :param fields:
    :param redaction:
    :param message:
    :param separator:
    :return:
    """
    return re.sub(r'(?<={0})[^{1}]+'
                  .format(separator,separator)
                  .join(fields), redaction, message)

