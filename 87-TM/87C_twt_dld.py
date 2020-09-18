#Twitter : Tweets Download
#-----------------------------
#Download tweets from twitter
#pip install tweepy
import tweepy  #install pip install tweepy
import csv
import pandas as pd

#credentials
consumerKey='uRDuync3BziwQnor1MZFBKp0x'
consumerSecret='t8QPLr7RKpAg4qa7vth1SBsDvoPKawwwdEhNRjdpY0mfMMdRnV'
AccessToken='14366551-Fga25zWM1YefkTb2TZYxsrx2LVVSsK0uSpF08sugW'
AccessTokenSecret='3ap8BZNVoBhE2GaMGLfuvuPF2OrHzM3MhGuPm96p3k6Cz'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(AccessToken, AccessTokenSecret)

api = tweepy.API(auth, wait_on_rate_limit=True)

#open / Create a file
csvFile = open('du.csv','w')
#r - read, w -new, a -append,r+ read&write
csvWriter = csv.writer(csvFile)
handle ='@dupadhyaya'
#change to see the values, tweets will be stored in du.csv in project folder #run the for loop together
#run together
for tweet in tweepy.Cursor(api.search, q=handle, count=100, lang= "en", since = "2019-07-01").items():
    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode( 'utf-8') ])

handle ='@Kamaksh44382698'
for tweet in tweepy.Cursor(api.search, q=handle, count=100, lang= "en", since = "2020-01-01").items():
    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode( 'utf-8') ])

handle='@shambo_23'
for tweet in tweepy.Cursor(api.search, q=handle, count=100, lang= "en", since = "2020-01-01").items():
    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode( 'utf-8') ])

#https://twitter.com/IIMC_India
handle='@IIMC_India'
for tweet in tweepy.Cursor(api.search, q=handle, count=100, lang= "en", since = "2020-01-01").items():
    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode( 'utf-8') ])

    
    
csvFile = open('ua.csv','w')
csvWriter = csv.writer(csvFile)
topic = '#unitedAirlines'
for tweet in tweepy.Cursor(api.search, q=topic, count=100, lang="en", since = "2019-01-01").items():
    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode( 'utf-8')])
                 
csvFile = open('corona.csv','w')
csvWriter = csv.writer(csvFile)
topic = '#corona'
for tweet in tweepy.Cursor(api.search, q="#corona", count=100, lang="en", since = "2020-01-01").items():
    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])


#search with string
search_words = "ipl2020"
date_since = "2019-09-01"

tweets = tweepy.Cursor(api.search, q=search_words, lang="en", since=date_since).items(5)
tweets
#Cursor can return text, who setn, date sent of tweet
for tweet in tweets:
    print(tweet.text)
#https://twitter.com/hashtag/ipl2020?lang=en
#as collection
tweets = tweepy.Cursor(api.search, q=search_words, lang="en", since=date_since).items(5)  #run again
[tweet.text for tweet in tweets]  #list of collection


#Remove Retweets
new_search = search_words + "-filter:retweets"
new_search
tweets = tweepy.Cursor(api.search, q=new_search, lang="en", since=date_since).items(5)  #run again
[tweet.text for tweet in tweets]  #list of collection


#who is tweeting about xxxx
#tweet.user.screen_name, tweet.user.location
tweets = tweepy.Cursor(api.search, q=search_words, lang="en", since=date_since).items(10)  #run again

user_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]
user_locs
#Convert to pandas
tweet.text = pd.DataFrame(data=user_locs, columns=['user', 'location'])
tweet.text


#my research area GamifiedLearningAnalytics
tweets = tweepy.Cursor(api.search, q="GamifiedLearningAnalytics", lang="en", since="2019-01-01").items(5)
tweets
for tweet in tweets:    print(tweet.text)
user_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]
user_locs #???


#Customise
new_search = "business + analytics -filter:retweets"
date_since = "2019-08-01"
tweets = tweepy.Cursor(api.search, q=new_search, lang="en", since=date_since).items(100)  #run again
all_tweets = [[tweet.text for tweet in tweets]]
all_tweets[:5]

#timeline :10 most recent tweet
public_tweets = api.home_timeline()
for tweet in public_tweets:    print(tweet.text)
    
for tweet in public_tweets:
    print(tweet.created_at)
    print(tweet.user.screen_name)
    print(tweet.user.location)
    

#usertimeline :10 most recent tweet
user_tweets = api.user_timeline()
#can specify since_id, max_id, count, id/user_id, screen_name
for tweet in user_tweets:
    print(tweet.text)
    
for tweet in user_tweets:
    print(tweet.created_at)
    print(tweet.user.screen_name)
    print(tweet.user.location)

user_tweets = api.user_timeline(count=10)
#can specify since_id, max_id, count, id/user_id, screen_name
for tweet in user_tweets:
    print(tweet.text, "\t", tweet.created_at, "\t" ,tweet.user.screen_name, "\t", tweet.user.location)

#NYtimes tweets
name = "nytimes"
tweetCount=20
results = api.user_timeline(id=name, count=tweetCount)
for tweet in results:
    print(tweet.text, "\n")

#search using keyword
query ="Cricket"
language = "en"
results = api.search(q=query, lang=language)
for tweet in results:
    print( tweet.user.screen_name, "\t", tweet.text ,"\n" )

#Assignment - spatial Graph on where ICC was mentioned in the world
#Assignment - Sentimental Analysis on tweet, find overall opinion on GST in india
#Assignment - Social graph on most popular users that tweet about ICC cricket

