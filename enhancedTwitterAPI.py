class EnhancedTwitterApi:
  def __init__(self, tweepy):
    self.twitterApi = tweepy
    
  def multipleHashtagsTweetIds(self, hashtags):
    tweetIds = set()
    for hashtag in hashtags:
      tweets = self.twitterApi.search(hashtag, count=30)
      for tweet in tweets:
        tweetIds.add(tweet.id) 
      
    return tweetIds

  #hashtags = list of hashtags, on_data = function called on new data
  def streamOnHashTags(self, hashtags, on_data):
    #create a stream on every 
    for hashtag in hashtags:
      print("brbv")
    