#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import os

# import auth from heroku
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

# twitter auth
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        img = os.path.abspath('jacket.jpg')
        print(status.user.screen_name, status.text)
        api.update_with_media(img, "@" + status.user.screen_name + " Then I don't need a jacket!", in_reply_to_status_id=status.id)

    # error handling
    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(track=["Pretty much everywhere its gonna be hot", "Pretty much everywhere it's gonna be hot"])

# favorite all replies
# if @reply:
# get @reply tweet id
#   api.create_favorite(id)
