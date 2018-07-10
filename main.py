from flask import Flask, render_template
from flask import request
import requests

import ServeTemplate
import APICall
import SpinWin

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def Spin():
    if request.method == 'POST':
        name = request.args.get('un')
        pwd = request.args.get('pass')
        #Begin by connecting to Redcat to retrieve the current users information
        userAccount = APICall.UserDetails(name,pwd)
        userAccountName = userAccount.GetName()
        #True/False to determine if user is eligible to play the current game
        userEligibility = userAccount.GetUserEligibility()
        if (userEligibility):
        #Determine the prize that an eligible user will win, and the number of rotations the Spin Wheel should rotate. 
            spinWin = SpinWin.SpinWin()
            prizeValue = spinWin.GetPrizeNumber()
            numberOfSpins = spinWin.GetWheelRotation()
        #Fetch the site template
        siteTemplate = ServeTemplate.ServeTemplate(userEligibility)
        siteTemplate = siteTemplate.GetSiteTemplate()
    #Insert site template into page.
        return render_template(siteTemplate, Name = userAccountName, prizeWon = prizeValue, rotation = numberOfSpins)

    elif request.method == 'GET':
        name = request.args.get('un')
        pwd = request.args.get('pass')

        #Begin by connecting to Redcat to retrieve the current users information
        userAccount = APICall.UserDetails(name,pwd)
        userAccountName = 'Is a Get Request -- Deny Access'
        #True/False to determine if user is eligible to play the current game
        userEligibility = userAccount.GetUserEligibility()
        if (userEligibility):
        #Determine the prize that an eligible user will win, and the number of rotations the Spin Wheel should rotate. 
            spinWin = SpinWin.SpinWin()
            prizeValue = spinWin.GetPrizeNumber()
            numberOfSpins = spinWin.GetWheelRotation()
        #Fetch the site template
        siteTemplate = ServeTemplate.ServeTemplate(userEligibility)
        siteTemplate = siteTemplate.GetSiteTemplate()
    #Insert site template into page.
        return render_template(siteTemplate, Name = userAccountName, prizeWon = prizeValue, rotation = numberOfSpins)
    
    
    
    #text = request.form['un']
    #Begin by connecting to Redcat to retrieve the current users information
    #userAccount = APICall.UserDetails('username','password')
    #userAccountName = userAccount.GetName()
    #True/False to determine if user is eligible to play the current game
    #userEligibility = userAccount.GetUserEligibility()
    #if (userEligibility):
        #Determine the prize that an eligible user will win, and the number of rotations the Spin Wheel should rotate. 
    #    spinWin = SpinWin.SpinWin()
    #    prizeValue = spinWin.GetPrizeNumber()
    #    numberOfSpins = spinWin.GetWheelRotation()
    #Fetch the site template
    #siteTemplate = ServeTemplate.ServeTemplate(userEligibility)
    #siteTemplate = siteTemplate.GetSiteTemplate()
    #Insert site template into page.
    #return render_template(siteTemplate, Name = userAccountName, prizeWon = prizeValue, rotation = numberOfSpins)



#@app.route('/')
#The main serves up the main HTML content to feed into the users browser that a user will see.
#def Main():
    


 #   return render_template('success.html')



if __name__== "__main__":
    app.run(debug=True)



