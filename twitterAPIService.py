import tweepy


class TwitterAPIService:
    def __init__(self, auth):
        self.auth = auth
        self.twitterApi = tweepy.API(auth)

    def multipleHashtagsTweetIds(self, hashtags):
        # .append()doesn't work for dictionaries ...
        tweetIds = set()
        for hashtag in hashtags:
            tweets = self.twitterApi.search(hashtag, count=30)
            for tweet in tweets:
                tweetIds.add(tweet.id)

        return tweetIds

    # returns a stream object
    def startstreamOnKeywords(self, hashtags, on_status):
        # create a stream for every hashtag listed

        myStreamListener = tweepy.StreamListener
        myStreamListener.on_status = on_status

        myStream = tweepy.Stream(listener=myStreamListener(), auth=self.auth)
        myStream.filter(track=hashtags)

        return myStream

    def retweetTweets(self, tweetIds):
        for tweet_id in tweetIds:
            self.twitterApi.retweet(id=tweet_id)
