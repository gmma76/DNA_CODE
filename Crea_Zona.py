import http.client
import urllib.parse
import json
import requests
import urllib3
from requests.auth import HTTPBasicAuth
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import http.client
import requests
host="ipserver"
username="admin"
password="admin)"

def LoginDNA(host,username,password):
    headers={
     'content-type':"application/json"
     }
    url="https://{}/api/system/v1/auth/token".format(host)
    response=requests.request("POST",url,auth=HTTPBasicAuth(username,password),headers=headers,verify=False)
    print(response.status_code)
    return response.json()["Token"]
