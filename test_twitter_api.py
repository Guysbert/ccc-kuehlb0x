from unittest import TestCase
from mock import patch
from collections import defaultdict
from twitter_api import get_api


__some_consumer_key__ = 'some_consumer_key'
__some_consumer_secret__ = 'some_consumer_secret'
__some_access_token_key__ = 'some_access_token_key'
__some_access_token_secret__ = 'some_access_token_secret'

__configuration__ = defaultdict(dict)
__configuration__['Consumer']['consumer_key'] = __some_consumer_key__
__configuration__['Consumer']['consumer_secret'] = __some_consumer_secret__
__configuration__['Access']['access_token_key'] = __some_access_token_key__
__configuration__['Access']['access_token_secret'] = __some_access_token_secret__


class TestTwitterApi(TestCase):

    @patch('twitter.Api')
    @patch('ConfigParser.ConfigParser')
    def test_api_gets_read(self, mock_config_parser, mock_twitter_api):
        def return_value_for_key(*args):
            return __configuration__[args[0]][args[1]]
        mock_config = mock_config_parser.return_value
        mock_config.get.side_effect = return_value_for_key
        get_api()
        mock_config.read.assert_called_with('config.ini')
        mock_twitter_api.assert_called_with(consumer_key=__some_consumer_key__,
                                            consumer_secret=__some_consumer_secret__,
                                            access_token_key=__some_access_token_key__,
                                            access_token_secret=__some_access_token_secret__)

