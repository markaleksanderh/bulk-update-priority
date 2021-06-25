import requests
from requests.auth import HTTPBasicAuth
import json

from dotenv import dotenv_values

config = dotenv_values(".env")

api_token = config['API_TOKEN']
email = config['EMAIL']
domain = config['COMPANY_DOMAIN']

base_url = "https://" + domain + ".net/rest/api/3/issue/"
auth = HTTPBasicAuth(email, api_token)
headers = {
   "Accept": "application/json"
}

def get_issue(issue_id):
    url = base_url + issue_id
    response = requests.request("GET", url, headers=headers, auth=auth)
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

get_issue('EL-1409')