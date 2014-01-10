import praw
import json
import requests
import tweepy
import time

access_token = '2281115456-IN0iDReAEsoynUjBA5306e7y2dHoEF0JCm6e9wL'
access_token_secret = '4BIXBvl4FKcxbywusogHY75FfStsdBxIvQ1efQ224lDj1'
consumer_key = 'WoQmQDWup7kzA2sG1gRhBg'
consumer_secret = 'rpwi8Q8TWePbPLXXGNpDGERwaDnBQz9MZJuASGORpU'

def strip_title(title):
	if len(title) < 94:
		return title
	else:
		return title[:93] + "..."

def tweet_creator(subreddit_info):
	post_dict = {}
	post_ids = []
	print "[Dogebot] yo i'm dogebot i be gettin those posts from reddit"
	for submission in subreddit_info.get_new(limit=20):
		post_dict[strip_title(submission.title)] = submission.url
		post_ids.append(submission.id)
	print "[Dogebot] such generate short link"
	mini_post_dict = {}
	for post in post_dict:
		post_title = post
		post_link = post_dict[post]   		
		short_link = shorten(post_link)
		mini_post_dict[post_title] = short_link 
	return mini_post_dict, post_ids

def setup_connection_reddit(subreddit):
	print "[Dogebot] very connection  wow very reddit"
	r = praw.Reddit('dogecoinscamwatch'
				'monitoring %s' %(subreddit)) 
	subreddit = r.get_subreddit(subreddit)
	return subreddit

def shorten(url):
	headers = {'content-type': 'application/json'}
	payload = {"longUrl": url}
	url = "https://www.googleapis.com/urlshortener/v1/url"
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	link = json.loads(r.text)['id']
	return link

def duplicate_check(id):
	found = 0
	with open('posted_posts.txt', 'r') as file:
		for line in file:
			if id in line:
				found = 1
	return found

def add_id_to_file(id):
	with open('posted_posts.txt', 'a') as file:
		file.write(str(id) + "\n")

def main():
	subreddit = setup_connection_reddit('dogecoinscamwatch')
	post_dict, post_ids = tweet_creator(subreddit)
	tweeter(post_dict, post_ids)

def tweeter(post_dict, post_ids):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	for post, post_id in zip(post_dict, post_ids):
		found = duplicate_check(post_id)
		if found == 0:
			print "[bot] Posting this link on twitter"
			print post+" "+post_dict[post]+""
			api.update_status(post+" "+post_dict[post]+"")
			add_id_to_file(post_id)
			time.sleep(30)
		else:
			print "[Dogebot] wow very post.. such duplicate" 

if __name__ == '__main__':
	main()
