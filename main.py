import tweepy
import config
# from twilio.rest import Client

# setup authentication
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)
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
# todo: figure out how to search multiple hashtags
tweets = api.search('#free', count=3)
user_ids = []
for tweet in tweets:
    user_ids.append(tweet.id) 
print(user_ids)   

# if api search call didn't work print helpful error message
if not tweets:
    print('API search call didnt work')

# API.update_status
# While not rate limited by the API, a user is limited in the number of Tweets they can create at a time. If the number of updates posted by the user reaches the current allowed limit this method will return an HTTP 403 error.

# creating a tweet with resources that will help the homeless
# retweet a tweet with the users
for user_id in user_ids:
    api.retweet(id=user_id)

 