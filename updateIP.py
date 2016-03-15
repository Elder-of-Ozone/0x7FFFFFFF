import requests

url = "https://dynamicdns.park-your-domain.com/update?"
domain = "0x7fffffff.xyz"
password = "580c72d8d80440fba6cb0320108f6ed5"

params = {"hosts": "@", "domain": domain, "password": password}

r = requests.post(url, params=params)
print r.text
