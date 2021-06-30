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


def get_issue(issue_id):
    headers = {"Accept": "application/json"}
    url = base_url + issue_id
    response = requests.request("GET", url, headers=headers, auth=auth)
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

def update_issue(issue_id, priority):
    headers = {"Accept": "application/json","Content-Type": "application/json"}
    url = base_url + issue_id
    payload = json.dumps({"update":{"priority":[{"set":{"name" : priority}}]}})
    response = requests.request("PUT", url, headers=headers, data=payload, auth=auth)
    print(response)

def open_file(file):
    pass

# with open('issues.csv', newline='') as csvfile:
#     csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
#     # Skip first row
#     next(csv_reader)
#     for row in csv_reader:
#         update_issue(row[0],row[1].strip())

# get_issue('EL-1409')
# update_issue('EL-1409', 'Critical')