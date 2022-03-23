####################################################
'''
VSD Performance Checker 
Mass Enterprise Deletion with VSDK API


@author Muzaffer Kahraman 2022
'''
####################################################

#!/usr/bin/env python3
from property_parser import credentials
from vspk import v5_0 as vsdk
from datetime import date
import logging

class enterprise:

    def __init__(self,name):
        global org
        self.name=name      
        org = vsdk.NUEnterprise(name=self.name)
       
    def delete(self):
        delete_item=nc.user.enterprises.get_first(filter='name=="%s"'%org.name)
        delete_item.delete()
                
if __name__=="__main__":
    
    today = date.today()
    logfile = "/var/log/"+str(today) + "_vsd_performance_checker.log"
    logging.basicConfig(filename=logfile,level=logging.INFO,format='%(asctime)s %(levelname)s  %(message)s')
    logging.info("Enterprise Deletion Started")

    # Let's parse the config file using the credentials class
    creds=credentials("credential.properties")

    nc = vsdk.NUVSDSession(username=creds.get_user(), password=creds.get_passwd(), enterprise=creds.get_org(), api_url=creds.get_url())
    nc.start()
    
    for i in range (0,10):
        enterprise_name="TestEnterprise_"+str(i)
        ent=enterprise(enterprise_name)
        ent.delete()
        logging.info(enterprise_name+" deleted")
    
    logging.info("Enterprise Deletion Ended")

    
  

