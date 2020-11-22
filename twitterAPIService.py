import tweepy

class TwitterAPIService:
    def __init__(self, auth):
        self.auth = auth
        self.twitterApi = tweepy.API(auth)

    # retrieve tweetIds by using multiple hashtags
    def multipleHashtagsTweetIds(self, hashtags, geocode=None):
        tweetIds = set()
        for hashtag in hashtags:
            tweets = self.twitterApi.search(hashtag, count=30, geocode=geocode)
            for tweet in tweets:
                tweetIds.add(tweet.id)

        return tweetIds

    # retrieve tweet texts by using multipleHashtagsTweetIds
    def retrieveTweets(self, tweetIds, geocode=None):
        tweets = set()
        for tweetId in tweetIds:
            tweet = self.twitterApi.get_status(tweetId)
            tweets.add(tweet.text)
        return tweets

    # starts a tweet stream, and returns a stream object
    # on_status: callback function when there is a new tweet
    def startstreamOnKeywords(self, hashtags, on_status):
        # create a stream for every hashtag listed

        myStreamListener = tweepy.StreamListener
        myStreamListener.on_status = on_status

        myStream = tweepy.Stream(listener=myStreamListener(), auth=self.auth, is_async=True)
        myStream.filter(track=hashtags)

        return myStream

    def retweetTweets(self, tweetIds):
        for tweet_id in tweetIds:
            try:
                self.twitterApi.retweet(id=tweet_id)
                print("Retweeted " + str(tweet_id))
            except tweepy.TweepError as e:
                print(e)
