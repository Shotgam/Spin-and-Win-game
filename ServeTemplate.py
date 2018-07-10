class ServeTemplate():
    def __init__(self,userEligibility):
        self.userEligibility = userEligibility
    #Fetch the correct site template
    def GetSiteTemplate(self):
        #If user is eligible to play the game, serve them index.html
        if (self.userEligibility):
            return 'index.html'
        #Otherwise, send them a Spin and Win promo
        else:
            return 'Spin&Win-ReturnLater.html'
        
