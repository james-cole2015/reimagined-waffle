
import tweepy
import logging
import time





consumer_key = "xxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxx"
access_token = "xxxxxxxxxxx"
access_secret = "xxxxxxxxxxx"
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth)

