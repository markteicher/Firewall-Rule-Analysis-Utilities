# Firewall-Rule-Analysis-Utilities

FIREMON SPLUNK APP
===================

Overview
--------
The FireMon Splunk App integrates FireMon Security Manager data with Splunk to provide security teams with centralized visibility into firewall policy compliance, risk exposure, and change tracking across enterprise networks.

This app includes:
- Prebuilt dashboards for compliance, risk, rule usage, and device inventory.
- Modular input support for FireMon REST API data ingestion.
- Bundled FireMon Python SDK (https://github.com/lukejohannsen/firemon-api) for native API access.
- Setup UI for API key and FireMon URL configuration.
- Saved searches and macros for reuse across dashboards.
- Role-based access control via `default.meta`.

Installation
------------
1. Copy the app folder (`firemon_splunk_app/`) into your Splunk `$SPLUNK_HOME/etc/apps/` directory.
2. Restart Splunk (`splunk restart`).
3. Go to **Apps > Manage Apps > FireMon Splunk App**.
4. Use the setup UI to input your FireMon API base URL and token.
5. Configure data collection via `firemon_input.py` or `inputs.conf`.

Dependencies
------------
- Python 3.7+
- Internet access or internal routing to FireMon API
- Splunk Enterprise 8.0+

Directory Layout
----------------
- `bin/firemon_api/`: Full FireMon SDK
- `dashboards/`: XML dashboards
- `default/`: app.conf, inputs.conf, restmap.conf
- `metadata/`: permissions
- `static/`, `appserver/static/`: logos and icons

Support
-------
For FireMon platform questions:
https://support.firemon.com

For Splunk app customization or integration help:
Contact your FireMon Solutions Architect or Splunk Admin.

License
-------
MIT License. See embedded LICENSE file if applicable.
