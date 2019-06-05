#Importing libraries
import datetime
import sys
import os
import jsonpickle
import tweepy
from datetime import timedelta, datetime
import random

# time set up to gather status from the past 5 hours used in the search query
rtime = datetime.now() - timedelta(hours=-5)

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
#Setting up new api wrapper, using authentication only
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

user = api.me()
#only if you want to I used it to confirm information
print(user.name)
print(user.location)

 
#Error handling
if (not api):
    print ("Problem Connecting to API")


#Getting Geo ID for USA
places = api.geo_search(query="USA", granularity="country")

#Copy USA id
place_id = places[0].id
print('USA id is: ',place_id)

#You can check how many queries you have left using rate_limit_status() method
api.rate_limit_status()['resources']['search']
{'/search/tweets': {'limit': 450, 'remaining': 450, 'reset': 1470850812}}

#This is what we are searching for
#We can restrict the location of tweets using place:id 
#We can search for multiple phrases using OR
searchQuery = 'place:' + place_id + '#linux OR #opensource OR #python OR #internet2 OR' \
              '#aws OR #ansible OR #kubernetes OR #openshift OR #bash OR #cloudformation OR' \
              '#devops OR #100daysofcode OR #ruby OR #freecodecamp OR #learntocode OR #womenintech OR' \
              '#networking OR #openstack OR #github OR #gitlab'

#Maximum number of tweets we want to collect 
maxTweets = 100

#The twitter Search API allows up to 50 tweets per query
tweetsPerQry = 50 

tweetCount = 0
ids = []
#Open a text file to save the tweets to
with open('devops.json', 'w') as f:

    #Tell the Cursor method that we want to use the Search API (api.search)
    #Also tell Cursor our query, and the maximum number of tweets to return
    for tweet in tweepy.Cursor(api.search,q=searchQuery,lang="en").items(maxTweets) :
        if tweet.created_at <= rtime:
            ids.append(tweet.id_str)

        #Verify the tweet has place info before writing (It should, if it got past our place filter)
        if tweet.place is not None:

            #Write the JSON format to the text file, and add one to the number of tweets we've collected
            f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
            tweetCount += 1


    #Display how many tweets we have collected, the ids of the status's and pick a random status to retweet and favorite
    print("Downloaded {0} tweets".format(tweetCount))
    print (ids)
    fav  = (random.choice(ids))
    print (fav)
    api.create_favorite(fav)
    api.retweet(fav)
   
   #remove the devops.json file- you can always keep the file to confirm the search query
os.remove('devops.json')
