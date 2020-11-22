import tweepy
import config
import twitterAPIService
import twilioHandler

# setup authentication
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

#create a new twitter service object with the authentication we created
twitterService = twitterAPIService.TwitterAPIService(auth)

# the function that gets called when there's a new tweet, for streaming
def on_status(self, status):
    twitterService.retweetTweets([status.id])
    twilioHandler.sendText(status.id, config.my_phone_number)

# for searching
def searchAndNotify(twitterService, query, geocode):
  twitterService = twitterAPIService.TwitterAPIService(auth)
  tweet_ids = twitterService.multipleHashtagsTweetIds(query, geocode=geocode)
  print(tweet_ids)
  twitterService.retweetTweets(tweet_ids)
  messages = twitterService.retrieveTweets(tweet_ids)
  for message in messages:
    twilioHandler.sendText(message, config.my_phone_number)

# coordinates and radius
SAN_FRANCISCO_GEOCODE = "37.773972,-122.431297,100mi"

# include all the hashtags we want to search for
SEARCH_HASHTAGS = ["#freefood","#freemeals"]
STREAM_QUERY = ["@FoodBankSF0"]

#runs the search function every hour
searchAndNotify(twitterService=twitterService, query=SEARCH_HASHTAGS, geocode=SAN_FRANCISCO_GEOCODE)

#starts the stream for the scanning new tweets
twitterService.startstreamOnKeywords(STREAM_QUERY, on_status)
