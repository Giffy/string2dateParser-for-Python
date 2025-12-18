"""
exceptions.py

This module contains custom exceptions for the project.
"""

class ParserError(Exception):
    """Base class for exceptions in the parser module."""
    pass

class InvalidDateFormatError(ParserError):
    """Exception raised for errors in the input date format."""
    def __init__(self, message="Invalid date format provided."):
        self.message = message
        super().__init__(self.message)

class InvalidTimestampError(ParserError):
    """Exception raised for errors in the input timestamp."""
    def __init__(self, message="Invalid timestamp format provided."):
        self.message = message
        super().__init__(self.message)