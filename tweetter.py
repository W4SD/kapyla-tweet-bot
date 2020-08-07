import conf
import tweepy


class Tweetter():

    # init twitter client
    def __init__(self):
        auth = tweepy.OAuthHandler(conf.twt_api_key, conf.twt_api_secret)
        auth.set_access_token(conf.twt_access_tkn, conf.twt_access_tkn_secret)
        self.twt = tweepy.API(auth)

    def tweet_match(self, tweet_text):

        # @ToDo add match url as "attachment_url"
        self.twt.update_status(tweet_text)
