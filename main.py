import tweepy
import config
import enhancedTwitterAPI
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
hashtags = ["free", "food"]

ETA = enhancedTwitterAPI.EnhancedTwitterApi(twitterApi)
tweet_ids = ETA.multipleHashtagsTweetIds(hashtags)
print(tweet_ids)   

# if twitterApi search call didn't work print helpful error message
if not tweet_ids:
    print('API search call didnt work')

# API.update_status
# While not rate limited by the API, a user is limited in the number of Tweets they can create at a time. If the number of updates posted by the user reaches the current allowed limit this method will return an HTTP 403 error.

hashtags = ["free", "food"]

ETA = enhancedTwitterAPI.EnhancedTwitterApi(twitterApi)
tweet_ids = ETA.multipleHashtagsTweetIds(hashtags)

# creating a tweet with resources that will help the homeless
# retweet a tweet with the users
for tweet_id in tweet_ids:
    twitterApi.retweet(id=tweet_id)

 