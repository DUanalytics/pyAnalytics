#Download Tweets from Internet
#-----------------------------
#Download tweets from twitter
import tweepy
from tweepy import OAuthHandler

#credentials : from developer account in twitter
consumerKey='uRDuync3BziwQnor1MZFBKp0x'
consumerSecret='t8QPLr7RKpAg4qa7vth1SBsDvoPKawwwdEhNRjdpY0mfMMdRnV'
AccessToken='14366551-Fga25zWM1YefkTb2TZYxsrx2LVVSsK0uSpF08sugW'
AccessTokenSecret='3ap8BZNVoBhE2GaMGLfuvuPF2OrHzM3MhGuPm96p3k6Cz'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(AccessToken, AccessTokenSecret)

api = tweepy.API(auth, wait_on_rate_limit=True)

keyword = "python"

tweets = api.search(keyword, count=10, lang="en", exclude="retweets", tweet_mode='extended')
for item in tweets:    print(item)

#data related to tweet, note its datastructure
#under development
