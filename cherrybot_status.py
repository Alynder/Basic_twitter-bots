
#Importing libraries
import subprocess
import sys
import os
import jsonpickle
import tweepy


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


#char limit for the status so you can add more to it
new_status = (os.popen('fortune -n 120; echo "#basic_twitter powered by: #cloudofyourchoice and #python"').read()) 
##used to confirm status was working
print new_status

#push status out
api.update_status(new_status)
