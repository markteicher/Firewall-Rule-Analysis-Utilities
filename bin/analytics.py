# analytics.py

import logging
from .client import FiremonClient

logger = logging.getLogger(__name__)

class Analytics:
def __init__(self, client: FiremonClient):
self.client = client

def get_policy_violations(self, domain_id: int = None):
"""Retrieve all policy violations."""
path = "/analytics/policyviolations"
params = {}
if domain_id:
params['domainId'] = domain_id
return self.client.get(path, params=params)

def get_unused_rules(self, domain_id: int = None):
"""Retrieve all unused firewall rules."""
path = "/analytics/unusedrules"
params = {}
if domain_id:
params['domainId'] = domain_id
return self.client.get(path, params=params)

def get_cleanup_opportunities(self, domain_id: int = None):
"""Retrieve rule cleanup opportunities."""
path = "/analytics/cleanup"
params = {}
if domain_id:
params['domainId'] = domain_id
return self.client.get(path, params=params)

def get_top_violators(self, domain_id: int = None):
"""Retrieve top policy violators."""
path = "/analytics/topviolators"
params = {}
if domain_id:
params['domainId'] = domain_id
return self.client.get(path, params=params)
