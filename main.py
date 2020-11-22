import tweepy
import config
import enhancedTwitterAPI
import twilioHandler
# from twilio.rest import Client
# setup authentication
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
twitterApi = tweepy.API(auth)
print('hope this works...')

# send direct message to food bank church
# API.send_direct_message

# create streaming bc we need realtime tweets
# searching for tweet
hashtags = ["#free", "#food", "#blanket"]

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

# send the tweet to organizations with registered phone numbers
phone_numbers = ["+14089307943"]
example_message = "lmaoooo"
for phone_number in phone_numbers:
    twilioHandler.sendText(example_message, phone_number)