
import http.client
import urllib.parse
import httplib, urllib
import requests
def LoginDNA():
    conn = http.client.HTTPSConnection("sandboxdnac.cisco.com")


    headers = {
    'content-type': "application/json",
    'authorization': ",Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE=",
    }



    conn.request("POST", "/dna/system/api/v1/auth/token", headers=headers)

    res = conn.getresponse()
    data = res.read()

def Create_Site(area_name,area_parentName):
    Token=LoginDNA()
    body={
     "type": "area",
        "site":{
            "area":{
                    "name":area_name,
                    "parentName":area_parentName
                    }
                }
                }
    response= {

        "executionId": "",
        "executionStatusUrl": "",
        "message": ""
        }
    headers = {
    '__runsync': "false",
    '__timeout': "30",
    '__persistbapioutput': "true",
    'x-auth-token':Token
    }


    res = conn.getresponse()
    data = res.read()
    print (res.status)
    print( "-----")
    print (res.reason)
    data = res.read()
    print (data)
    conn.close()
    #print(data.decode("utf-8"))


