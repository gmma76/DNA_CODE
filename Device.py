import json
import requests
import urllib3
from requests.auth import HTTPBasicAuth
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import http.client
from prettytable import PrettyTable
dnac_devices=PrettyTable(['Hostname','Platform Id','Software Type','Software Version','Up Time'] )
dnac_devices.padding_width=1

def LoginDNA(host,username,password):
    headers={
     'content-type':"application/json",
     'x-aut-token':""
     }
    url="https://{}/api/system/v1/auth/token".format(host)
    response=requests.request("POST",url,auth=HTTPBasicAuth(username,password),headers=headers,verify=False)
    #print(response.status_code)
    return response.json()["Token"]

def network_device_list():
    Token=LoginDNA("sandboxdnac.cisco.com","devnetuser","Cisco123!")
    headers={
     'content-type':"application/json",
     'x-aut-token':""
     }
    url="https://sandboxdnac.cisco.com/api/v1/network-device"
    response=requests.request("GET",url,headers=headers, verify=False)
    data=response.json()
    for item in data['response']:

        dnac_devices.add_row([item["hostname"],item["platformId"],item["softwareType"],item["softwareversion"],item["upTime"]])

network_device_list()
print(dnac_devices)
