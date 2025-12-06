#!/usr/bin/env python
# encoding = utf-8

import sys
import json
import time
import datetime
import logging
import requests
from splunklib.modularinput import *

class FireMonInput(Script):
def get_scheme(self):
scheme = Scheme("FireMon Data Collector")
scheme.description = "Collects data from FireMon API."
scheme.use_external_validation = True
scheme.use_single_instance = False

scheme.add_argument(
Argument("firemon_url",
title="FireMon API Base URL",
description="Base URL of the FireMon Security Manager API",
required_on_create=True)
)

scheme.add_argument(
Argument("api_key",
title="FireMon API Key",
description="Your FireMon API key",
required_on_create=True)
)

scheme.add_argument(
Argument("interval",
title="Polling interval (in seconds)",
description="How often to poll the FireMon API",
required_on_create=True)
)

return scheme
