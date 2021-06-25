

# This code sample uses the 'requests' library:
# http://docs.python-requests.org
# import requests
# from requests.auth import HTTPBasicAuth
# import json

# url = "https://your-domain.atlassian.net/rest/api/3/issue/{issueIdOrKey}"

# auth = HTTPBasicAuth("mark@dencreative.com", "<api_token>")

# headers = {
#    "Accept": "application/json"
# }

# response = requests.request(
#    "GET",
#    url,
#    headers=headers,
#    auth=auth
# )

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))