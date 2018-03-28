# importing the module
import tweepy
 
# personal details
consumer_key = "okoyctCgGgFkqXtxKMpJb3KMY"
consumer_secret = "vhjjaNiTPe1MDK6aFIxYlGDwBFs8aisVeK0XaQnxWGVlohp4bi"
access_token ="966204621231415296-jHuTj2gLvHi40clUPQMgfb4PLUnbpO6"
access_token_secret ="rN8jDFde2rWpWGkBZSUzv1i0lB9cytJTb46j1nwSieXJq"
 
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(okoyctCgGgFkqXtxKMpJb3KMY,vhjjaNiTPe1MDK6aFIxYlGDwBFs8aisVeK0XaQnxWGVlohp4bi)
 
# authentication of access token and secret
auth.set_access_token(966204621231415296-jHuTj2gLvHi40clUPQMgfb4PLUnbpO6,rN8jDFde2rWpWGkBZSUzv1i0lB9cytJTb46j1nwSieXJq)
api = tweepy.API(auth)
 
# update the status
api.update_status(status ="Hello Everyone !")
