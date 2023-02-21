#!/usr/bin/python3

# *********************************************************************************
#
# Nuage VSD Provisioning PoC
#
# Required  : [Python requests,json, base64, urllib3]
#
# Muzaffer Kahraman (Muzo)
#
# *********************************************************************************

import requests
import json
import base64
import urllib3

# Prevent Warning Messages for Certificates, to be displayed
urllib3.disable_warnings()

 # Global Vars
A=[]

# Get Global Vars
globalVarsFileName = "globalvars.csv"

try:
  f = open(globalVarsFileName,"r")
except FileNotFoundError:
  print(f"globalvars.csv not found!\n")

s=f.readline()
A=s.split(",")
userName=A[0]
passWord=A[1]
enterprise=A[2]
url=A[3].rstrip()

def bas64encode(st):
  st_bytes = st.encode('ascii')
  base64_bytes = base64.b64encode(st_bytes)
  base64_st = base64_bytes.decode('ascii')
  return(base64_st)

def getToken():
  headers={'X-Nuage-Organization':'csp','Authorization':'XREST {}'.format(bas64encode(userName+":"+passWord))}
  res = requests.get(url+"/nuage/api/v5_0/me", headers=headers,  verify=False)
  token=res.json()[0]["APIKey"]
  return(token)

def listEnterprises():
  headers={'X-Nuage-Organization':'csp','Authorization':'XREST {}'.format(bas64encode(userName+":"+token))}
  res=requests.get(url+"/nuage/api/v5_0/enterprises", headers=headers,  verify=False)
  enterprises=res.json()
  for item in enterprises:
    print(item["name"],item["ID"])

def findEnterpriseID(name):
  headers={'X-Nuage-Organization':'csp','Authorization':'XREST {}'.format(bas64encode(userName+":"+token)),'X-Nuage-Filter':f'name contains "{name}"' }
  res=requests.get(url+"/nuage/api/v5_0/enterprises", headers=headers,  verify=False)
  enterprises=res.json()[0]
  return(enterprises["ID"])
  
def createEnterprise(name,profileID,localAS):
  profileID = "d7939e80-7fb4-11ed-a038-4d6d86f4dbb7"
  data={}
  data['name'] = name
  data['enterpriseProfileID']= profileID 
  data["localAS"]= localAS
  headers={'X-Nuage-Organization':'csp','Authorization':'XREST {}'.format(bas64encode(userName+":"+token))}
  res=requests.post(url+"/nuage/api/v5_0/enterprises", headers=headers,json=data,  verify=False)
  result=str(res)
  return(result[11:14])

def deleteEnterprise(name):
  id=findEnterpriseID(name)
  headers={'X-Nuage-Organization':'csp','Authorization':'XREST {}'.format(bas64encode(userName+":"+token))}
  res=requests.delete(url+"/nuage/api/v5_0/enterprises/"+id+"/?responseChoice=1", headers=headers,  verify=False);
  result=str(res)
  return(result[11:14])

def updateEnterprise(name,newname):
  data={}
  data['name'] = newname
  id=findEnterpriseID(name)
  headers={'X-Nuage-Organization':'csp','Authorization':'XREST {}'.format(bas64encode(userName+":"+token))}
  res=requests.put(url+"/nuage/api/v5_0/enterprises/"+id, headers=headers,json=data, verify=False);
  result=str(res)
  return(result[11:14])



    


