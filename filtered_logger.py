#!/usr/bin/env python3
"""
Module for handling Personal Data
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscates specified fields in the log message.

    Args:
        fields: List of strings representing fields to obfuscate
        redaction: String to replace field values
        message: String representing the log line
        separator: String representing the character separating fields

    Returns:
        Obfuscated log message
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
