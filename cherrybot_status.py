#Importing libraries
import subprocess
import sys
import os
import jsonpickle
import tweepy
import random

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
#Setting up new api wrapper, using authentication only
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

#printing username for confirmation of correct information
user = api.me()
#print(user.name)
#print(user.location)


#Error handling
if (not api):
    print ("Problem Connecting to API")
    
    
new_status1 = (os.popen('fortune linux -n 100; echo "#cherrybombbot powered by: #linux and #python"').read()) 
new_status2 = (os.popen('fortune startrek -n 100; echo "#cherrybombbot powered by: #linux and #python"').read()) 
new_status3 = (os.popen('fortune definitions -n 100; echo "#cherrybombbot powered by: #linux and #python"').read()) 
new_status4 = (os.popen('fortune futurama -n 100; echo "#cherrybombbot powered by: #linux and #python"').read()) 
new_status5 = (os.popen('fortune startrek-tng -n 100; echo "#cherrybombbot powered by: #linux and #python"').read()) 
new_status6 = (os.popen('fortune science -n 100; echo "#cherrybombbot powered by: #linux and #python"').read()) 
new_status7 = (os.popen('fortune computers -n 100; echo "#cherrybombbot powered by: #linux and #python"').read()) 
new_status8 = (os.popen('fortune zippy -n 100; echo "#cherrybombbot powered by: #linux and #python"').read()) 
new_status9 = (os.popen('fortune riddles -n 100; echo "#cherrybombbot powered by: #linux and #python"').read()) 
#print new_status1
#print new_status2
#print new_status3
#print new_status4
#print new_status5
#print new_status6
#print new_status7

new_status = random.choice([new_status1, new_status2, new_status3, new_status4, new_status5, new_status6, new_status7, new_status8, new_status9])
print new_status
api.update_status(new_status)

