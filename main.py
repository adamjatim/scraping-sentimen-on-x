import os
from dotenv import load_dotenv # type: ignore
import tweepy # type: ignore

# Muat variabel dari .env
load_dotenv()

# Ambil API Key dari .env
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Autentikasi menggunakan Bearer Token
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Pencarian tweet terbaru
query = "kominfo lang:id"
tweets = client.search_recent_tweets(query=query, max_results=10)

# Tampilkan hasil
for tweet in tweets.data:
    print(f"Tweet: {tweet.text}")
