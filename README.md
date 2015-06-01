# ShellShocker
ShellShocker parses a RSS feed from newegg.com that publishes their 'shell shocker' deals that go on 5 times a day. When a new deal is published, this script sends a tweet from @NeweggShocker with the deal and a link to it. ShellShocker is written in python, and set to run via cron at 12AM, 10AM, 1PM, 3PM, 6PM. All times are pacific time. 

To see it working follow @NeweggShocker

## Dependencies
Shellshocker requires two python packages to run.
- [Python-Twitter](https://code.google.com/p/python-twitter/)
- [FeedParser](https://pythonhosted.org/feedparser/)

```
pip install python-twitter
pip install feedparser
```

## Running for the first time
To use shellshocker you need to create your own twitter app. This is done by visiting the [Twitter Apps](https://apps.twitter.com/) page and creating a new app. Once you create a twitter app you will be able to get four different keys.
- Consumer Key
- Consumer Secret
- Access Token Key
- Access Token Secret

Paste these four keys into the respective variable name found in shellshocker.py

You can verify that your script is authenticated with the following:
```
api = twitter.Api(consumer_key='Paste Consumer Key Here',
                  consumer_secret='Paste Consumer Secret Here',
                  access_token_key='Paste Access Token Key Here',
                  access_token_secret='Paste Access Token Secret Here')

print api.VerifyCredentials()
```

### Important
ShellShocker uses a date-time stored in a text file to make sure it is not posting duplicates. When the script is run for the first time it creates a date_time_rss.txt file in the same location as the shellshocker.py script. It is very important to not delete that file.

When running ShellShocker the first time, you will need to uncomment the code block found in the parseRSS() function. The lines that should be uncommented are 23, 24, & 25.

## Functions & Description
- parseURL() takes a url to an RSS feed and parses the information and returns a dictionary that will be the tweet.
- checkDateTime() takes a date/time of an rss post and if it is newer than the most recent tweet, it will return true. Otherwise, it will return false.
- makeTweet() takes a parsed RSS feed and constructs a tweet.

