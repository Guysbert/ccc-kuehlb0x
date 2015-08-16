__author__ = 'andi'

import ConfigParser
import twitter

__consumer_key__ = str()
__consumer_secret__ = str()
__access_token_key__ = str()
__access_token_secret__ = str()


def __read_config__():
    config = ConfigParser.ConfigParser()
    config.read('config.ini')
    global __consumer_key__
    __consumer_key__ = config.get('Consumer', 'consumer_key')
    global __consumer_secret__
    __consumer_secret__ = config.get('Consumer', 'consumer_secret')
    global __access_token_key__
    __access_token_key__ = config.get('Access', 'access_token_key')
    global __access_token_secret__
    __access_token_secret__ = config.get('Access', 'access_token_secret')


def get_api():
    __read_config__()
    return twitter.Api(consumer_key=__consumer_key__,
                       consumer_secret=__consumer_secret__,
                       access_token_key=__access_token_key__,
                       access_token_secret=__access_token_secret__)
