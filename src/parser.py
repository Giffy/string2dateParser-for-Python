import datetime as dt
import re
import time
import exceptions


def parse_date(date_str: str, date_format=None, timestamp=None) -> dt:

  if date_format:
    try:
      return dt.datetime.strptime(date_str, date_format)
    except Exception as e:
      raise exceptions.InvalidDateFormatError(f"Invalid date format for input: {date_str}. Expected format: {date_format}")
  
  if timestamp:
    try:
      if re.match('^\d{16}', date_str):
          time_in_seconds = int(date_str)/1000000
          return dt.datetime.fromtimestamp(time_in_seconds)
      elif re.match('^\d{13}', date_str):
          time_in_seconds = int(date_str)/1000
          return dt.datetime.fromtimestamp(time_in_seconds)
      elif re.match('^\d{10}', date_str):
          time_in_seconds = int(date_str)
          return dt.datetime.fromtimestamp(time_in_seconds)    
    except Exception as e:
      raise exceptions.InvalidTimestampError(f"Invalid timestamp format for input: {e}")

  # ISO 8601 Format: YYYY-MM-DD
  # Custom Format:   YYYY/MM/DD
  pattern = "^(\d{4})[-\/]([0-1]{1}[0-9]{1})[-\/]([0-3]{1}[0-9]{1})$"
  if re.match(pattern, date_str):
    if '-' in date_str:
      return dt.datetime.strptime(date_str, "%Y-%m-%d")
    if '/' in date_str:
      return dt.datetime.strptime(date_str, "%Y/%m/%d")
  
  # YYYY-MM-DD HH:MM:SS  YYYY/MM/DD HH:MM:SS
  pattern = "^(\d{4})[-\/]([0-1]{1}[0-9]{1})[-\/]([0-3]{1}[0-9]{1}) ([0-1]{1}[0-9]{1}):([0-5]{1}[0-9]{1}):([0-5]{1}[0-9]{1})$"
  if re.match(pattern, date_str):
    if '-' in date_str:
      return dt.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    if '/' in date_str:
      return dt.datetime.strptime(date_str, "%Y/%m/%d %H:%M:%S")

  # 2025-01-15 8:56 AM   2025-01-15 8:56 PM
  pattern = "^(\d{4})[-\/]([0-1]{1}[0-9]{1})[-\/]([0-3]{1}[0-9]{1}) ([0-1]{1}[0-9]{1}):([0-5]{1}[0-9]{1}) (A|P)?(M)?$"
  if re.match(pattern, date_str):
    if '-' in date_str:
      return dt.datetime.strptime(date_str, "%Y-%m-%d %I:%M %p")
    if '/' in date_str:
      return dt.datetime.strptime(date_str, "%Y/%m/%d %I:%M %p")

  return None
