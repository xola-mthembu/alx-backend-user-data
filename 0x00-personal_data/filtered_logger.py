#!/usr/bin/env python3
"""
Module for filtering log messages with sensitive information.
"""

import re
import logging
from typing import List
import os
import mysql.connector
from mysql.connector import connection


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
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
        message = re.sub(
            rf"{field}=[^{separator}]*", f"{field}={redaction}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class for filtering PII fields in logs.
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record by obfuscating sensitive fields.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log record with obfuscated fields.
        """
        original = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION, original,
                            self.SEPARATOR)


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """
    Creates and returns a logger that obfuscates PII fields.

    Returns:
        logging.Logger: Configured logger object.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def get_db() -> connection.MySQLConnection:
    """
    Establishes a secure connection to a MySQL database.

    Returns:
        mysql.connector.connection.MySQLConnection: Database connection object.
    """
    db_user = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    db_host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    return mysql.connector.connect(
        user=db_user,
        password=db_password,
        host=db_host,
        database=db_name
    )


def main():
    """
    Retrieves and filters user data from the database and logs the output.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT name, email, phone, ssn, password, ip, last_login, "
        "user_agent FROM users;")
    for row in cursor:
        row_str = (
            "name={}; email={}; phone={}; ssn={}; password={}; "
            "ip={}; last_login={}; user_agent={};".format(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
            )
        )
        logger = get_logger()
        logger.info(row_str)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
