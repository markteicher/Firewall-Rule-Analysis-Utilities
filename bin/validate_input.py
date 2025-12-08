def validate_input(self, definition):
firemon_url = definition.parameters["firemon_url"]
api_key = definition.parameters["api_key"]

headers = {
"Authorization": f"Token {api_key}",
"Content-Type": "application/json"
}

test_url = f"{firemon_url.rstrip('/')}/securitymanager/api/version"

try:
response = requests.get(test_url, headers=headers, timeout=10, verify=True)
if response.status_code != 200:
raise ValueError(f"Unable to connect to FireMon API. Status code: {response.status_code}")
except Exception as e:
raise ValueError(f"Validation failed: {str(e)}")
