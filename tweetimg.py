import os
import tweepy,time
consumer_key = "okoyctCgGgFkqXtxKMpJb3KMY"
consumer_secret = "vhjjaNiTPe1MDK6aFIxYlGDwBFs8aisVeK0XaQnxWGVlohp4bi"
access_token ="966204621231415296-jHuTj2gLvHi40clUPQMgfb4PLUnbpO6"
access_token_secret ="rN8jDFde2rWpWGkBZSUzv1i0lB9cytJTb46j1nwSieXJq"
 
auth = tweepy.OAuthHandler(okoyctCgGgFkqXtxKMpJb3KMY,vhjjaNiTPe1MDK6aFIxYlGDwBFs8aisVeK0XaQnxWGVlohp4bi)

auth.set_access_token(966204621231415296-jHuTj2gLvHi40clUPQMgfb4PLUnbpO6,rN8jDFde2rWpWGkBZSUzv1i0lB9cytJTb46j1nwSieXJq)
api = tweepy.API(auth)

b=1
a=0

while a<=2 :
	img="/home/ec2017b122/Desktop/img"+str(b)+".jpg"
	cmd="fswebcam -F 3 --fps 20 -r 800x600 "+img
	os.system(cmd)
	print("pic taken")
	api.update_with_media(img,status="nice")
	print("wait for 5 secs")
	time.sleep(5)
	a+=1
	b+=1
	print("success"

