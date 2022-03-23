class credentials:

    def __init__(self,filename):
        
        global url
        global user
        global passwd
        global org
        
        self.filename=filename
        f = open("credential.properties","r")
        A=f.readlines()
        url=A[0].partition("=")[2].replace('\n', '')
        user=A[1].partition("=")[2].replace('\n', '')
        passwd=A[2].partition("=")[2].replace('\n', '')
        org=A[3].partition("=")[2].replace('\n', '')
        f.close()
            
    def get_url(self):
        return url

    def get_user(self):
        return user
 
    def get_passwd(self):
        return passwd

    def get_org(self):
        return org

