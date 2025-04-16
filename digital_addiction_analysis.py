import tweepy
import time

# Replace these with your actual bearer token
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAL1w0gEAAAAAvE9HcelxDhS2EVgJ89J5Jm%2BlQ%2FY%3DdZam6xRcAWNC30zyn92yf7Cv43iu6GUJ61QQki6184YmFeblO6'

# Set up the client
client = tweepy.Client(bearer_token=bearer_token)

# Define the query
query = "digital addiction"

try:
    tweets = client.search_recent_tweets(query=query, max_results=10)

    if tweets.data:
        for tweet in tweets.data:
            print(f"Tweet: {tweet.text}\n")
    else:
        print("No tweets found for the given query.")

except tweepy.TooManyRequests as e:
    print("⏳ Rate limit reached. Waiting for 15 minutes before retrying...")
    time.sleep(15 * 60)  # Wait 15 minutes
    # Optionally retry the request here if you want

except Exception as e:
    print("Something went wrong:", e)

