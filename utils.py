import logging
import os
import time
import datetime
import json
import sys

logger = logging.getLogger(__name__)


def int_or_none(val):
try:
return int(val)
except (TypeError, ValueError):
return None


def float_or_none(val):
try:
return float(val)
except (TypeError, ValueError):
return None


def timestamp_now():
return int(time.time())


def date_now():
return datetime.date.today().isoformat()


def to_list(val):
if val is None:
return []
if isinstance(val, list):
return val
return [val]


def snake_to_camel(word):
return ''.join(x.capitalize() or '_' for x in word.split('_'))


def filter_params(params):
"""Removes keys with None values from a dictionary."""
return {k: v for k, v in params.items() if v is not None}


def json_pretty(data):
return json.dumps(data, indent=2, sort_keys=True)


def fatal(msg, code=1):
logger.error(msg)
sys.exit(code)


def get_env(key, default=None):
return os.environ.get(key, default)
