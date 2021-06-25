import requests
from requests.auth import HTTPBasicAuth
import json
import csv

from dotenv import dotenv_values

config = dotenv_values(".env")

api_token = config['API_TOKEN']
email = config['EMAIL']
domain = config['COMPANY_DOMAIN']

base_url = "https://" + domain + ".net/rest/api/3/issue/"
auth = HTTPBasicAuth(email, api_token)
headers = {"Accept": "application/json"}

def get_issue(issue_id):
    url = base_url + issue_id
    response = requests.request("GET", url, headers=headers, auth=auth)
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

with open('issues.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    # Skip first row
    next(csv_reader)
    for row in csv_reader:
        get_issue(row[0])