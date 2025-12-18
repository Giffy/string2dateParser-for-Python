import datetime as dt
import re
import time


def parse_date(date_str: str, date_format=None, timestamp=None) -> dt:

  if date_format:
    return dt.datetime.strptime(date_str, date_format)

  # ISO 8601 Format: YYYY-MM-DD
  # Custom Format:   YYYY/MM/DD
  pattern = "^(\d{4})[-\/]([0-1]{1}[0-9]{1})[-\/]([0-3]{1}[0-9]{1})$"
  if re.match(pattern, date_str):
    if '-' in date_str:
      return dt.datetime.strptime(date_str, "%Y-%m-%d")
    if '/' in date_str:
      return dt.datetime.strptime(date_str, "%Y/%m/%d")
  
  # YYYY-MM-DD HH:MM:SS
  pattern = "^(\d{4})[-\/]([0-1]{1}[0-9]{1})[-\/]([0-3]{1}[0-9]{1}) ([0-1]{1}[0-9]{1}):([0-5]{1}[0-9]{1}):([0-5]{1}[0-9]{1})$"
  if re.match(pattern, date_str):
    if '-' in date_str:
      return dt.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    if '/' in date_str:
      return dt.datetime.strptime(date_str, "%Y/%m/%d %H:%M:%S")
    
  return None