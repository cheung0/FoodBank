import tweepy
import config
import twitterAPIService
# from twilio.rest import Client
# use aws rekognition to recognize the words free food in images 
# setup authentication
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
twitterApi = tweepy.API(auth)
print('hope this works...')

# send direct message to food bank church
# API.send_direct_message

# API.search30day

# maybe break code into different functions so it looks good in the demo

# create streaming bc we need realtime tweets
# geocode=37.7749,geocode=122.4194,geocode='30mi'
# geocode='37.7749, 122.4194, 300000000000000mi'
# https://twitter.com/_MealsOnWheels
# use twitter usernames that only tweet free shit
# searching for tweet
# be careful of the hashtags we put here
hashtags = ["#freefood"]

twitterService = twitterAPIService.TwitterAPIService(auth)
tweet_ids = twitterService.multipleHashtagsTweetIds(hashtags)
print(tweet_ids)   

# if twitterApi search call didn't work print helpful error message
if not tweet_ids:
    print('API search call didnt work')

#the function that gets called when there's a new tweet
def on_status(self, status):
    twitterService.retweetTweets([status.id])


twitterService = twitterAPIService.TwitterAPIService(auth)
twitterService.startstreamOnKeywords(hashtags, on_status)

# creating a tweet with resources that will help the homeless
# retweet a tweet with the users
twitterService.retweetTweets(tweet_ids)
