import requests
from requests.auth import HTTPBasicAuth
import json

from dotenv import dotenv_values

config = dotenv_values(".env")

api_token = config['API_TOKEN']
email = config['EMAIL']
domain = config['COMPANY_DOMAIN']

issue_id = 'EL-1409'

url = "https://dencreative.atlassian.net/rest/api/3/issue/" + issue_id

auth = HTTPBasicAuth(email, api_token)

headers = {
   "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))