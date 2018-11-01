# Basic_twitter-bots: A simple write up
Set status's and run a query of your choice to like and retweet.
You will need some background in python and pip for this bot.



## tweepy api
The tweepy api was easy to put together for this bot the documenation was robust and the examples are very educational.
I suggest you take a look [here](http://docs.tweepy.org/en/v3.6.0/index.html)
_________________
**For the authentication using tweepy please [click here](http://docs.tweepy.org/en/v3.6.0/cursor_tutorial.html)**

The cursor has proven to be an amazing way to connect and relatively easy to configure. While it is configured in these scripts, it is a very good read for knowledges sake.

## Prereqs for bots
+ python
+ python-pip
+ pip installed tweepy
+ pip installed jsonpickle

## What you need to set up on twitter

You will need to create a new [twitter app](https://apps.twitter.com/app/new) for these bots.
There is a fair amount of details required to be put in for apps with a minimum of 100 words for certain explinations of why you are running the app on twitter.


## Running on a cloud
I used the AWS free tier cloud instance with a very limited amount of strength because these run on a cron job every 6 and 10 hours.

## Keys you need from twitter 
These 4 keys are generated and provided when you create a new application within twitter.
```sh
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
```
You will need them to run the bots for the authentication against twitter.

## Configuring the bots
### cherrybot.py configuration

**Keys:** 
Enter the keys mentioned into this section of the script surrounded by single quotes.
```sh
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
```

**Search query configuration**

_example here and in the code is for devops related tweets_
```python
searchQuery = 'place:96683cc9126741d1 #linux OR #opensource OR #python OR #internet2 OR' \
              '#aws OR #ansible OR #kubernetes OR #openshift OR #bash OR #cloudformation OR' \
              '#devops OR #100daysofcode OR #ruby OR #freecodecamp OR #learntocode OR #womenintech OR' \
              '#networking OR #openstack OR #github OR #gitlab'
```

**Query count of tweet and json file to save to**

_Used for confirming the stringency of the search query and limiting or adding more to search for_

Current settings are the max you can collect and how many you want to grab per query for rate limiting.
The file the tweets are being written to are for confirming if your query is properly put together you can always go back and check as you test. 
_**Note: Currently in this set up the file is deleted after the actions of retweeting and favoriting is complete**_


```python
#Maximum number of tweets we want to collect 
maxTweets = 100

#The twitter Search API allows up to 50 tweets per query
tweetsPerQry = 50

tweetCount = 0
ids = []
#Open a text file to save the tweets to
with open('devops.json', 'w') as f:

```


### cherrybot_status.py configuration

This bot just sets a status in any time you want to run it. Right now the bot I have running is set to kick off every 6 hours with the out put from the fortune command with a character limitation of 120.

**Keys:** 
Enter the keys mentioned into this section of the script surrounded by single quotes.
```sh
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
```


**The main process**
```python
#char limit for the status so you can add more to it
new_status = (os.popen('fortune -n 120; echo "#basic_twitter_bot powered by: #cloudofyourchoice and #python"').read())
##used to confirm status was working
print new_status

#push status out
api.update_status(new_status)
```



The status option itself is changable at anypoint I chose a command that would produce some entertaining output.
You can always create a database of status's that you can pull from at random.




Copyright Information
---------------------

Copyright (C) 2018 Jessica Repka

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.
