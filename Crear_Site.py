import json
import requests
import urllib3
from requests.auth import HTTPBasicAuth
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import http.client


def LoginDNA(host,username,password):
    headers={
     'content-type':"application/json"
     }
    url="https://{}/api/system/v1/auth/token".format(host)
    response=requests.request("POST",url,auth=HTTPBasicAuth(username,password),headers=headers,verify=False)
    print(response.status_code)
    return response.json()["Token"]


def Create_Site(area_name,area_parentName):
    Token=LoginDNA("ip,"admin","admin)")
    payload ={
     "type": "area",
        "site":{
            "area":{
                    "name":area_name,
                    "parentName":area_parentName
                    }
                }
                }

    headers = {
    '__runsync': "false",
    '__timeout': "30",
    '__persistbapioutput': "true",
    'x-auth-token':Token
    }

    url="https://ip/dna/intent/api/v1/site"
    response=requests.request("POST",url,headers=headers,payload=payload,verify=True)
    print(response.status_code)







#LoginDNA("sandboxdnac.cisco.com","devnetuser","Cisco123!")
#Create_Site("Catalunya","Global")
Create_Site("Lleida","Global")
#Token=LoginDNA("10.1.11.35","admin","DActti19!)")

#Create_Building("Balaguer","Lleida","Teatre","Carrer Angel Guimera, 28, 25600 Balaguer, Lleida")
#Create_Floor("Balaguer","Lleida","Teatre","Planta1")
