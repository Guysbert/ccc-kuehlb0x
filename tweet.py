import twitter
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.ini')

consumer_key = config.get('Consumer', 'consumer_key')
consumer_secret = config.get('Consumer', 'consumer_secret')
access_token_key = config.get('Access', 'access_token_key')
access_token_secret = config.get('Access', 'access_token_secret')

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)


def tweet(source, temperature):
    new_tweet = dict()
    new_tweet['source'] = source
    new_tweet['temperature'] = temperature
    api.PostUpdate('the temperature at %s is %s' % (new_tweet['source'], new_tweet['temperature']))

