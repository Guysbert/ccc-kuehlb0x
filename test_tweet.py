from unittest import TestCase
from tweet import tweet
from mock import patch

class TestTweet(TestCase):

    def test_doesnt_do_anything_if_passed_dict_is_empty(self):
        temperatures = dict()
        tweet(temperatures)

    @patch('twitter_api.get_api')
    def test_posts_one_temperature(self, mock_twitter_api):
        mock_api = mock_twitter_api.return_value
        temperatures = dict()
        temperatures['Sensor1'] = 14.0
        tweet(temperatures)
        mock_api.PostUpdate.assert_called_with('Sensor1: 14.0')

    @patch('twitter_api.get_api')
    def test_posts_multiple_temperatures(self, mock_twitter_api):
        mock_api = mock_twitter_api.return_value
        temperatures = dict()
        temperatures['Sensor1'] = 14.0
        temperatures['Sensor2'] = 15.0
        tweet(temperatures)
        mock_api.PostUpdate.assert_called_with('Sensor1: 14.0, Sensor2: 15.0')
