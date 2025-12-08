# Copyright 2020 FireMon, LLC. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
from firemon_api.core.app import App
from firemon_api.core.api import API


class Reports(App):

path = "reports"
warnings = {"2.0.0": ["Reports API does not support create or delete."]}

def __init__(self, api: API):
self.api = api
super().__init__(api, self.path)

def list(self):
"""List all reports"""
return super()._list()

def get(self, id: int):
"""Get report by ID"""
return super()._get(id)

def download(self, id: int):
"""Download a report PDF by ID"""
path = f"{self.path}/{id}/download"
return self.api.connection.get(path, stream=True)
