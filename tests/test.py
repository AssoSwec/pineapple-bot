import os
import praw
import sys
import unittest

from hackerrank.HackerRankAPI import HackerRankAPI

sys.path.append("worker/")

from commands import get_food_pic, random_fact, gif, compile
from strings import USER_AGENT


class PineappleBotTest(unittest.TestCase):

    def setUp(self):
        self.reddit_client_id = os.environ.get("reddit_client_id")
        self.reddit_client_secret = os.environ.get("reddit_client_secret")
        self.hackerrank_key = os.environ.get("hackerrank_key")
        self.giphy_key = os.environ.get("giphy_key")

        self.reddit = praw.Reddit(client_id=self.reddit_client_id,
                                  client_secret=self.reddit_client_secret,
                                  user_agent=USER_AGENT)
        self.compiler = HackerRankAPI(api_key=self.hackerrank_key)

    def test_gifs(self):
        pass

    def test_reddit(self):
        pass

    def test_compile_good(self):
        message = ("/compile python3\n"
                   "```\n"
                   "x = 0\n"
                   "for i in range(10):\n"
                   "    x += i\n"
                   "print(x)\n"
                   "```")

        value = compile(message, self.compiler)

        self.assertEqual(value, '```45\n```')

if __name__ == "__main__":
    unittest.main()
