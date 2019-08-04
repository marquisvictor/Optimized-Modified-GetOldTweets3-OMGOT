# GetOldTweets3
A Python 3 library and a corresponding command line utility for accessing old tweets.

![Python 3x](https://img.shields.io/badge/python-3.x-blue.svg)
[![Build Status](https://travis-ci.org/Mottl/GetOldTweets3.svg?branch=master)](https://travis-ci.org/Mottl/GetOldTweets3)
[![pypi](https://img.shields.io/pypi/v/GetOldTweets3.svg)](https://pypi.org/project/GetOldTweets3/)
[![Downloads](https://pepy.tech/badge/getoldtweets3)](https://pepy.tech/project/getoldtweets3)

GetOldTweets3 is an improvement fork of the original Jefferson Henrique's [GetOldTweets-python](https://github.com/Jefferson-Henrique/GetOldTweets-python). It fixes known issues and adds features such as counting retweets, searching over multiple users accounts, etc. GetOldTweets3 supports only Python 3.

## Details
Twitter Official API has the bother limitation of time constraints, you can't get older tweets than a week. Some tools provide access to older tweets but in the most of them you have to spend some money before.
I was searching other tools to do this job but I didn't found it, so after analyze how Twitter Search through browser works I understand its flow. Basically when you enter on Twitter page a scroll loader starts, if you scroll down you start to get more and more tweets, all through calls to a JSON provider. After mimic we get the best advantage of Twitter Search on browsers, it can search the deepest oldest tweets.

## Installation
Use `pip install GetOldTweets3`  
or `pip install -e git+https://github.com/Mottl/GetOldTweets3#egg=GetOldTweets3`

## Command line utility
**GetOldTweets3:** exports tweets to a specified csv file ("output_got.csv" by default).

### Examples
**Get help:**
``` bash
GetOldTweets3 -h
``` 

**Example 1 - Get tweets by query search:**
```bash
GetOldTweets3 --querysearch "europe refugees" --maxtweets 10
```

**Example 1 - Get the last 10 top tweets by username:**
```bash
GetOldTweets3 --username "barackobama" --toptweets --maxtweets 10
```

**Example 3 - Get tweets by the username and bound dates** (until date is not included):
```bash
GetOldTweets3 --username "barackobama" --since 2015-09-10 --until 2015-09-12 --maxtweets 10
```

**Example 4 - Get tweets by several usernames:**
```bash
GetOldTweets3 --username "BarackObama,AngelaMerkeICDU" --usernames-from-file userlist.txt --maxtweets 10
```
(check https://github.com/Mottl/influencers for some prepared lists of usernames)

**Example 5 - Get tweets by language:**
```bash
GetOldTweets3 --querysearch "bitcoin" --lang cn --maxtweets 10
```

**Example 6 - Get tweets by place:**
```bash
GetOldTweets3 --querysearch "bitcoin" --near "Berlin, Germany" --within 25km --maxtweets 10
```

**Example 7 - Get tweets by geo coordinates:**
```bash
GetOldTweets3 --querysearch "museum" --near "55.75, 37.61" --within 40km --maxtweets 10
```

## Python classes
- **Tweet:** Model class that describes a specific tweet.
  - id (str)
  - permalink (str)
  - username (str)
  - to (str)
  - text (str)
  - date (datetime) in UTC
  - retweets (int)
  - favorites (int)
  - mentions (str)
  - hashtags (str)
  - geo (str)

- **TweetManager:** A manager class to help getting tweets in **Tweet**'s model.
  - getTweets (**TwitterCriteria**): Return the list of tweets retrieved by using an instance of **TwitterCriteria**. 

- **TwitterCriteria:** A collection of search parameters to be used together with **TweetManager**.
  - setUsername (str or iterable): An optional specific username(s) from a twitter account (with or without "@").
  - setSince (str. "yyyy-mm-dd"): A lower bound date (UTC) to restrict search.
  - setUntil (str. "yyyy-mm-dd"): An upper bound date (not included) to restrict search.
  - setQuerySearch (str): A query text to be matched.
  - setTopTweets (bool): If True only the Top Tweets will be retrieved.
  - setNear(str): A reference location area from where tweets were generated.
  - setWithin (str): A distance radius from "near" location (e.g. 15mi).
  - setMaxTweets (int): The maximum number of tweets to be retrieved. If this number is unsetted or lower than 1 all possible tweets will be retrieved.
  
### Examples
**Get tweets by username(s):**
``` python
import GetOldTweets3 as got

tweetCriteria = got.manager.TweetCriteria().setUsername("barackobama whitehouse")\
                                           .setMaxTweets(2)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
print(tweet.text)
```

**Get tweets by query search:**
``` python
tweetCriteria = got.manager.TweetCriteria().setQuerySearch('europe refugees')\
                                           .setSince("2015-05-01")\
                                           .setUntil("2015-09-30")\
                                           .setMaxTweets(1)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
print(tweet.text)
```

**Get tweets by username and bound dates:**
``` python
tweetCriteria = got.manager.TweetCriteria().setUsername("barackobama")\
                                           .setSince("2015-09-10")\
                                           .setUntil("2016-01-01")\
                                           .setMaxTweets(1)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
print(tweet.text)
```

**Get the last 10 top tweets by username:**
``` python
tweetCriteria = got.manager.TweetCriteria().setUsername("barackobama")\
                                           .setTopTweets(True)\
                                           .setMaxTweets(10)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
print(tweet.text)
```
