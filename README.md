# Jira bulk update

Dependencies
- python-dotenv
- requests

Run `pip3 install python-dotenv requests` before beginning.

Go to Jira and get your basic-authentication API token.

Create a .env file in the directory with the following values:
```
API_TOKEN=<api_token>
EMAIL=<email>
COMPANY_DOMAIN=<domain>
```

Update the issues.csv with your issue IDs and priorities, format should be 

| ID | Priority |
| - | - |
| 1  | High |
| 2  | Low |

Finally, in the terminal enter `python3 run.py`.