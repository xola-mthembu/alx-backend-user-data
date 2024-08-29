#!/usr/bin/env python3
"""
Module for filtering log messages with sensitive information.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction:
           str, message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields (List[str]): List of fields to obfuscate.
        redaction (str): Replacement string for obfuscated fields.
        message (str): The original log message.
        separator (str): The separator between fields in the log message.

    Returns:
        str: The obfuscated log message.
    """
    for field in fields:
        message = re.sub(rf"{field}=[^{separator}]*",
                  f"{field}={redaction}", message)
    return message
