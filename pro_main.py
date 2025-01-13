import os
from dotenv import load_dotenv
import tweepy
from textblob import TextBlob

# Muat variabel dari .env
load_dotenv()

# Ambil variabel dari .env
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Autentikasi ke API Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Fungsi untuk analisis sentimen
def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Mencari tweet tentang "kominfo"
query = "kominfo"
tweets = api.search_tweets(q=query, lang="id", count=100)

# Menyimpan hasil analisis
results = []
for tweet in tweets:
    sentiment = analyze_sentiment(tweet.text)
    results.append({"text": tweet.text, "sentiment": sentiment})

# Tampilkan hasil
for result in results:
    print(f"Tweet: {result['text']}\nSentiment: {result['sentiment']}\n")
