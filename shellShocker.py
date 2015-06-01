import feedparser
import twitter

# Twitter API Values
api = twitter.Api(consumer_key='Paste Consumer Key Here',
		  consumer_secret='Paste Consumer Secret Here',
		  access_token_key='Paste Access Token Key Here',
		  access_token_secret='Paste Access Token Secret Here')

# parseURL() takes a url to an RSS feed and parses the information and returns a dictionary 
# that will be the tweet
def parseRSS(url):
	rss = feedparser.parse(url)

	rss_entry = {
    	'title': rss['entries'][0]['title'],
	'url':	 rss['entries'][0]['id'],
        'date':  rss['entries'][0]['published']
	}
	
	# Write the Date-Time Published to file to make sure no duplicate tweets
	# Only use this the first time the script is run, then comment it out.
	# text_file = open("date_time_rss.txt", "w")
	# text_file.write(rss_entry['date'])
	# text_file.close()
  
	return rss_entry
	
# checkDateTime() takes a date/time of an rss post and if it is newer than the most
# recent tweet, it will return true. Otherwise, it will return false
def checkDateTime(date):
	date_file = open("date_time_rss.txt","r")
	date2 = date_file.readline()	

	if date2 != date:
		return True
	else:
		return False

# makeTweet() takes a parsed RSS feed and constructs a tweet
def makeTweet(info):
	tweet = ''
	tweet += info['title']
	tweet += ' - '
	tweet += info['url']

	return tweet

# Replace URL with the feed you would like to parse
url = 'http://www.newegg.com/Product/RSS.aspx?Submit=ShellShocker'

info = parseRSS(url)

if checkDateTime(info['date']) == True:
	text_file = open("date_time_rss.txt", "w")
        text_file.write(info['date'])
        text_file.close()
	api.PostUpdate(makeTweet(info))
