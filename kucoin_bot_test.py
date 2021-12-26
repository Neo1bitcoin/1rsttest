#from io import open_code

# from flask import Flask, render_template, request, jsonify
#from numpy import busday_count
import requests
#from binance.client import Client
# import numpy as np
from datetime import datetime
import pytz



# start_time = time.time()

# from kucoin.client import Client

# client = Client(config.API_KEY,config.API_SECRET, config.API_PASSPHARASE)
###############################################################################################################################
###############################################################################################################################
##################################                                      #######################################################
##################################               trade bot              #######################################################
##################################                                      #######################################################
###############################################################################################################################
###############################################################################################################################




############# Discord 
webhook_url = 'https://discord.com/api/webhooks/924644920738844692/FZWIyVLy5Da9YQz5SqPxTeEtvmltXgR0jByWLt7LVl67evEpFIwUKaIBj_kuEYxlTUyj'
tz_tehran = pytz.timezone('asia/tehran') 
datetime_tehran = datetime.now(tz_tehran).strftime("%m/%d/%Y, %H:%M:%S")

discort_message = "Server Message\n\nTime: " + str(datetime_tehran)
print(discort_message)
payload = {
    "username" : 'alert_server_test',
    "content" : discort_message
}
requests.post(webhook_url, json=payload)


                
                



# if __name__ == "__main__":
#     app.run()
#     app.run(debug = True)


# set FLASK_APP=app
# set FLASK_ENV=development
# flask run

#pip install virtualenv
#virtualenv venv
#venv\Scripts\activate
#Set-ExecutionPolicy Unrestricted -Scope Process


