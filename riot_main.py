import ssl
import snscrape.modules.twitter as sntwitter

# handle error SSL certification
ssl._create_default_https_context = ssl._create_unverified_context

query = "kominfo lang:id"
tweets = []

for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i > 99:
        break
    tweets.append({"text": tweet.content})

for tweet in tweets:
    print(f"Tweet: {tweet['text']}")
