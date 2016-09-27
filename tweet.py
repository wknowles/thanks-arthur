#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
from secrets import *

# twitter auth
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.user.screen_name, status.text)
        api.update_status(".@" + status.user.screen_name + " Then I don't need a jacket!", in_reply_to_status_id=status.id)

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
