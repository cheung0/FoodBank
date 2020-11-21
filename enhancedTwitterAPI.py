class EnhancedTwitterApi:
  def __init__(self,tweepy):
    self.twitterApi = tweepy
    
  def multipleHashtagsTweetIds(self,hashtags):
    # .append()doesn't work for dictionaries ...
    tweetIds = set()
    for hashtag in hashtags:
      tweets = self.twitterApi.search(hashtag, count=30)
      for tweet in tweets:
        tweetIds.add(tweet.id) 
      
    return tweetIds
