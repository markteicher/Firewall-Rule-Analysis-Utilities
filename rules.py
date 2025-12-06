# rules.py

from .utils import FiremonApiRequest

class Rules:
def __init__(self, token, base):
self.token = token
self.base = base

def search(self, filter=None):
"""
Search all rules with optional filters.

:param filter: Optional dictionary of search filters
:return: List of rules
"""
endpoint = f"{self.base}/rules/search"
return FiremonApiRequest.get(self.token, endpoint, params=filter)

def get(self, rule_id):
"""
Retrieve a specific rule by ID.

:param rule_id: Rule identifier
:return: Rule details
"""
endpoint = f"{self.base}/rules/{rule_id}"
return FiremonApiRequest.get(self.token, endpoint)

def update(self, rule_id, data):
"""
Update a rule with new data.

:param rule_id: Rule identifier
:param data: Dictionary of fields to update
:return: Updated rule
"""
endpoint = f"{self.base}/rules/{rule_id}"
return FiremonApiRequest.put(self.token, endpoint, json=data)

def delete(self, rule_id):
"""
Delete a rule by ID.

:param rule_id: Rule identifier
:return: API response
"""
endpoint = f"{self.base}/rules/{rule_id}"
return FiremonApiRequest.delete(self.token, endpoint)
