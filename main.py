import tweepy
import config
import twitterAPIService
import twilioHandler


# the function that gets called when there's a new tweet
def on_status(self, status):
    twitterService.retweetTweets([status.id])
    twilioHandler.sendText(status.text, config.my_phone_number)

def searchAndRetweet(twitterService, query, geocode):
  twitterService = twitterAPIService.TwitterAPIService(auth)
  tweet_ids = twitterService.multipleHashtagsTweetIds(query, geocode=geocode)
  print(tweet_ids)
  twitterService.retweetTweets(tweet_ids)


# setup authentication
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

twitterService = twitterAPIService.TwitterAPIService(auth)

# coordinates and radius
SAN_FRANCISCO_GEOCODE = "37.773972,-122.431297,100mi"

# include all the hashtags we want to search for
SEARCH_HASHTAGS = ["freefood"]
STREAM_QUERY = ["@FoodBankSF0"]

#runs the search function every hour
searchAndRetweet(twitterService=twitterService, query=SEARCH_HASHTAGS, geocode=SAN_FRANCISCO_GEOCODE)

#starts the stream for the scanning new tweets
twitterService.startstreamOnKeywords(STREAM_QUERY, on_status)


