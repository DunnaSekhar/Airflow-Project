import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs 


access_key = "m5vYOQ4EeACWW8HCeuGgfoQ4S"
access_secret = "b68uurPBb2NPpwl0oiQcqhVA30zod8RgZOQytqkdBhlYe8pgLC"
consumer_key = "1703056874931998720-KLpwjdnpAP6FKKT0ZhZM2MNwik6IUm"
consumer_secret = "2pBIPE0EkCGvduWjRvr5TyxuOKLUti2FEVHKUvEAmaLWV"

auth = tweepy.OAuthHandler(access_key, access_secret)   
auth.set_access_token(consumer_key, consumer_secret)

api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='@dunna_sekhar7', 
                            # 200 is the maximum allowed count
                            count=200,
                            include_rts = False,
                            # Necessary to keep full_text 
                            # otherwise only the first 140 words are extracted
                            tweet_mode = 'extended'
                            )




list = []
for tweet in tweets:
    text = tweet._json["full_text"]

    refined_tweet = {"user": tweet.user.screen_name,
                    'text' : text,
                    'favorite_count' : tweet.favorite_count,
                    'retweet_count' : tweet.retweet_count,
                    'created_at' : tweet.created_at}
    
    list.append(refined_tweet)

df = pd.DataFrame(list)
df.to_csv('refined_tweets.csv')