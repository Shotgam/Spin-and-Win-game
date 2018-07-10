class UserDetails():

    finalURL = 'https://chatimetest.redcatcloud.com.au/api/v1/login'
    authType = 'U'
    username = 'No input'
    password = 'No input'
    
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def GetName(self):
        return self.username

    def GetCoupon(self):
        pass

    def AdminConnect(self):
        adUsername = "HAVASapi"
        adPassword = "4@5asap1"
        payload = {'username':adUsername,'psw':adPassword,'auth_type':authType}
        request = requests.post(finalURL,data=payload)
        print(request)

    def GetUserEligibility(self):
        return True
        

    


