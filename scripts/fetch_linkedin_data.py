import json

import requests

api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
api_key = "qsG_uovpfvcTXCytp2p7Gg"
header_dic = {"Authorization": "Bearer " + api_key}
params = {
    "url": "https://www.linkedin.com/in/ericnessdata/",
}
response = requests.get(api_endpoint, params=params, headers=header_dic)
with open("data/linkedin_profile.json", "w") as f:
    f.write(json.dumps(response.json()))
