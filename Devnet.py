import json
import requests
import urllib3

from requests.auth import HTTPBasicAuth
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import http.client
DNAC="sandboxdnac.cisco.com/dna/system"
DNAC_PORT="443"
def create_url(path,controller_ip=DNAC):
    """ Helper function to create a DNAC API endpoint URL
    """

    return "https://%s/api/v1/%s" % (controller_ip, path)

def get_auth_token():
    url = create_url("auth/token",DNAC)
    print(url)
    username="devnetuser"
    password="Cisco123!"
    headers={
     'content-type':"application/json",
     'x-auth-token':""
     }

    response=requests.request("POST",url,auth=HTTPBasicAuth(username,password),headers=headers,verify=False)
    print(response.status_code)
    return response.json()["Token"]


def get_url(url):

    url = create_url(path="")
    print(url)
    token = get_auth_token()
    headers = {'x-auth-token' : ""}
    try:
        response = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.RequestException as cerror:
        print("Error processing request", cerror)
        sys.exit(1)

    return response.json()
    print (response.json(),indent=4)

def list_network_devices():
    return get_url("network-device")



if __name__ == "__main__":

    response = list_network_devices()
    print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
        format("hostname","mgmt IP","serial",
        "platformId","SW Version","role","Uptime"))
