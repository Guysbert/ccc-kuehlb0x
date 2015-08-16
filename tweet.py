import twitter_api


def tweet(temperatures):
    if len(temperatures) == 0:
        return
    api = twitter_api.get_api()
    the_tweet = ''
    for sensor in temperatures:
        the_tweet += "%s: %s, " % (sensor, temperatures[sensor])
    the_tweet = the_tweet[:-2]
    api.PostUpdate(the_tweet)

