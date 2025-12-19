import datetime as dt
import re
import time
import exceptions


def parse_date(date_str: str, date_format=None, timestamp=None, time_zone_offset="UTC") -> dt:

  def set_time_zone_offset(parsed_date: dt, time_zone_offset: str) -> dt:
    timezones = {
      "HST": "-10:00",  # Hawaii-Aleutian
      "AKST": "-09:00", # Alaska
      "PST": "-08:00",  # Pacific Time (Los Angeles)
      "MST": "-07:00",  # Mountain Time(US and Canada)
      "EAST": "-06:00", # Easter Island
      "CST": "-06:00",  # Central Time (US and Canada)
      "EST": "-05:00",  # Eastern Time (New York, Atlanta)
      "CLT": "-04:00",  # Santiago
      "AST": "-04:00",  # Atlantic Time(Canada)
      "PYT": "-04:00",  # Asuncion
      "NST": "-03:30",  # Newfoundland
      "PMST": "-03:00", # Miquelon
      "WGST": "-02:00", # Godthab,Nuuk
      "AZOT": "-01:00", # Azores
      "UTC": "+00:00",  # Universal Time Coordinated
      "GMT": "+00:00",  # London
      "WET": "+00:00",  # Lisbon
      "CET": "+01:00",  # Amsterdam,Berlin,Bern,Rome,Stockholm,Vienna
      "EET": "+02:00",  # Cairo,Chisinau,Beirut,Athens,Bucharest,Gaza,Hebron
      "IST": "+02:00",  # Israel Standard Time
      "ACST": "+09:30", # Adelaide
      "AEST": "+10:00", # Canberra,Melbourne,Sydney
      "LHST": "+10:30", # Lord Howe Island
      "NFT": "+11:00",  # Norfolk Island
      "NZST": "+12:00", # Auckland,Wellington
      "CHAST": "+12:45" # Chatham Island
    }
    
    if ":" not in time_zone_offset:
      print(f'--------- {time_zone_offset}')
      print(f'--------- {timezones[time_zone_offset]}')
      if time_zone_offset in timezones.keys():
        time_zone_offset = timezones[time_zone_offset]
    
    offset_hours, offset_minutes = map(int, time_zone_offset.split(":"))
    offset = dt.timedelta(hours=offset_hours, minutes=offset_minutes)
    parsed_date += offset
    return parsed_date


  if date_format:
    try:
      parsed_date = dt.datetime.strptime(date_str, date_format)
      parsed_date = set_time_zone_offset(parsed_date, time_zone_offset)
      return parsed_date
    except Exception as e:
      raise exceptions.InvalidDateFormatError(f"Invalid date format for input: {date_str}. Expected format: {date_format}")
  
  if timestamp:
    try:
      if re.match('^\d{16}', date_str):
          time_in_seconds = int(date_str)/1000000
          parsed_date = dt.datetime.fromtimestamp(time_in_seconds)
      elif re.match('^\d{13}', date_str):
          time_in_seconds = int(date_str)/1000
          parsed_date = dt.datetime.fromtimestamp(time_in_seconds)
      elif re.match('^\d{10}', date_str):
          time_in_seconds = int(date_str)
          parsed_date = dt.datetime.fromtimestamp(time_in_seconds)
      parsed_date = set_time_zone_offset(parsed_date, time_zone_offset)
      return parsed_date

    except Exception as e:
      raise exceptions.InvalidTimestampError(f"Invalid timestamp format for input: {e}")

  # ISO 8601 Format: YYYY-MM-DD   Custom Format:   YYYY/MM/DD
  pattern = "^(\d{4})[-\/]([0-1]{1}[0-9]{1})[-\/]([0-3]{1}[0-9]{1})$"
  if re.match(pattern, date_str):
    if '-' in date_str:
      parsed_date = dt.datetime.strptime(date_str, "%Y-%m-%d")
    if '/' in date_str:
      parsed_date = dt.datetime.strptime(date_str, "%Y/%m/%d")
    parsed_date = set_time_zone_offset(parsed_date, time_zone_offset)
    return parsed_date

  
  # YYYY-MM-DD HH:MM:SS   YYYY/MM/DD HH:MM:SS
  pattern = "^(\d{4})[-\/]([0-1]{1}[0-9]{1})[-\/]([0-3]{1}[0-9]{1}) ([0-1]{1}[0-9]{1}):([0-5]{1}[0-9]{1}):([0-5]{1}[0-9]{1})$"
  if re.match(pattern, date_str):
    if '-' in date_str:
      parsed_date = dt.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    if '/' in date_str:
      parsed_date = dt.datetime.strptime(date_str, "%Y/%m/%d %H:%M:%S")
    parsed_date = set_time_zone_offset(parsed_date, time_zone_offset)
    return parsed_date


  # 2025-01-15 8:56 AM   2025/01/15 8:56 PM
  pattern = "^(\d{4})[-\/]([0-1]{1}[0-9]{1})[-\/]([0-3]{1}[0-9]{1}) ([0-1]{1}[0-9]{1}):([0-5]{1}[0-9]{1}) (A|P)?(M)?$"
  if re.match(pattern, date_str):
    if '-' in date_str:
      parsed_date = dt.datetime.strptime(date_str, "%Y-%m-%d %I:%M %p")
    if '/' in date_str:
      parsed_date = dt.datetime.strptime(date_str, "%Y/%m/%d %I:%M %p")
    parsed_date = set_time_zone_offset(parsed_date, time_zone_offset)
    return parsed_date

  return None
