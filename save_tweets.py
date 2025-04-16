import csv

tweets = ["This is a tweet", "Another tweet here", "Digital addiction is real!"]

with open('tweets.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Tweet"])  # Header
    for tweet in tweets:
        writer.writerow([tweet])
