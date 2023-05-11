import time

import tweepy

auth = tweepy.OAuthHandler('asfdaswjkdfljkasgj', 'alksdflajgjklasjkldsjkl')
auth.set_access_token('access_token', 'access_token_secret')

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

user = api.me()
print(user.followers_count)


def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


# # Generous Bot
# for follower in tweepy.Cursor(api.get_followers).items():
#     print(follower.name)

search_string = 'python'
numbersOfTweets = 2

# Narcissist Bot
for tweet in tweepy.Cursor(api.search_tweets, search_string).items(numbersOfTweets):
    try:
        # tweet.favorite()
        tweet.retweet()
        print('i like it')
    except tweepy.TweepyException as e:
        print(e.reason)
    except StopIteration:
        break
