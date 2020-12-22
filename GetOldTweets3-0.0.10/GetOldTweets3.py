#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""To use this script you can pass the following attributes:
       querysearch: a query text to be matched
          username: a username or a list of usernames (comma or space separated)
                    of a specific twitter account(s) (with or without @)
username-from-file: a file with a list of usernames,
             since: a lower bound date in UTC (yyyy-mm-dd)
             until: an upper bound date in UTC (yyyy-mm-dd) (not included)
              near: a reference location area from where tweets were generated
            within: a distance radius from "near" location (e.g. 15mi)
         toptweets: only the tweets provided as top tweets by Twitter (no parameters required)
         maxtweets: the maximum number of tweets to retrieve
              lang: the language of tweets
            output: a filename to export the results (default is "output_got.csv")

Examples:

# Example 1 - Get tweets by query search:
GetOldTweets3 --querysearch "europe refugees" --maxtweets 10

# Example 1 - Get the last 10 top tweets by username:
GetOldTweets3 --username "barackobama" --toptweets --maxtweets 10

# Example 3 - Get tweets by username and bound dates (until date is not included):
GetOldTweets3 --username "barackobama" --since 2015-09-10 --until 2015-09-12 --maxtweets 10

# Example 4 - Get tweets by several usernames:
GetOldTweets3 --username "BarackObama,AngelaMerkeICDU" --usernames-from-file userlist.txt --maxtweets 10

# Example 5 - Get tweets by language:
GetOldTweets3 --querysearch "bitcoin" --lang cn --maxtweets 10 

# Example 6 - Get tweets by place:
GetOldTweets3 --querysearch "bitcoin" --near "Berlin, Germany" --within 25km --maxtweets 10 

# Example 7 - Get tweets by geo coordinates:
GetOldTweets3 --querysearch "museum" --near "55.75, 37.61" --within 40km --maxtweets 10 
"""

import os, sys, re, getopt
import traceback

if sys.version_info[0] < 3:
    raise Exception("Python 2.x is not supported. Please upgrade to 3.x")

import GetOldTweets3 as got

def main(argv):
    if len(argv) == 0:
        print('You must pass some parameters. Use \"-h\" to help.')
        return

    if len(argv) == 1 and argv[0] == '-h':
        print(__doc__)
        return

    try:
        opts, args = getopt.getopt(argv, "", ("querysearch=",
                                              "username=",
                                              "usernames-from-file=",
                                              "since=",
                                              "until=",
                                              "near=",
                                              "within=",
                                              "toptweets",
                                              "maxtweets=",
                                              "lang=",
                                              "output=",
                                              "debug"))

        tweetCriteria = got.manager.TweetCriteria()
        outputFileName = "output_got.csv"

        debug = False
        usernames = set()
        username_files = set()
        for opt, arg in opts:
            if opt == '--querysearch':
                tweetCriteria.querySearch = arg

            elif opt == '--username':
                usernames_ = [u.lstrip('@') for u in re.split(r'[\s,]+', arg) if u]
                usernames_ = [u.lower() for u in usernames_ if u]
                usernames |= set(usernames_)

            elif opt == '--usernames-from-file':
                username_files.add(arg)

            elif opt == '--since':
                tweetCriteria.since = arg

            elif opt == '--until':
                tweetCriteria.until = arg

            elif opt == '--near':
                geocode = arg.split(',')
                try:
                    if len(geocode) != 2:
                        raise
                    lat, lon = geocode[0].strip(), geocode[1].strip()
                    if lat[-1].lower() == 'n':
                        lat = float(lat[:-1])
                    elif lat[-1].lower() == 's':
                        lat = -float(lat[:-1])
                    else:
                        lat = float(lat)

                    if lon[-1].lower() == 'e':
                        lon = float(lon[:-1])
                    elif lon[-1].lower() == 'w':
                        lon = -float(lon[:-1])
                    else:
                        lon = float(lon)
                    if lat < -180 or lat > 180:
                        raise
                    if lon < -90 or lon > 90:
                        raise
                    tweetCriteria.lat = lat
                    tweetCriteria.lon = lon
                except:
                    tweetCriteria.near = arg

            elif opt == '--within':
                tweetCriteria.within = arg

            elif opt == '--toptweets':
                tweetCriteria.topTweets = True

            elif opt == '--maxtweets':
                tweetCriteria.maxTweets = int(arg)

            elif opt == '--lang':
                tweetCriteria.lang = arg

            elif opt == '--output':
                outputFileName = arg

            elif opt == '--debug':
                debug = True

        if debug:
            print(' '.join(sys.argv))
            print("GetOldTweets3", got.__version__)

        if username_files:
            for uf in username_files:
                if not os.path.isfile(uf):
                    raise Exception("File not found: %s"%uf)
                with open(uf) as f:
                    data = f.read()
                    data = re.sub('(?m)#.*?$', '', data)  # remove comments
                    usernames_ = [u.lstrip('@') for u in re.split(r'[\s,]+', data) if u]
                    usernames_ = [u.lower() for u in usernames_ if u]
                    usernames |= set(usernames_)
                    print("Found %i usernames in %s" % (len(usernames_), uf))

        if usernames:
            if len(usernames) > 1:
                tweetCriteria.username = usernames
                if len(usernames)>20 and tweetCriteria.maxTweets > 0:
                    maxtweets_ = (len(usernames) // 20 + (len(usernames)%20>0)) * tweetCriteria.maxTweets
                    print("Warning: due to multiple username batches `maxtweets' set to %i" % maxtweets_)
            else:
                tweetCriteria.username = usernames.pop()
        value = (f"{outputFileName}")
        outputFile = open(outputFileName, "w+", encoding="utf8")
        outputFile.write('date,username,to,replies,retweets,favorites,text,geo,mentions,hashtags,id,permalink\n')

        cnt = 0
        def receiveBuffer(tweets):
            nonlocal cnt

            for t in tweets:
                data = [t.date.strftime("%Y-%m-%d %H:%M:%S"),
                    t.username,
                    t.to or '',
                    t.replies,
                    t.retweets,
                    t.favorites,
                    '"'+t.text.replace('"','""')+'"',
                    t.geo,
                    t.mentions,
                    t.hashtags,
                    t.id,
                    t.permalink]
                data[:] = [i if isinstance(i, str) else str(i) for i in data]
                outputFile.write(','.join(data) + '\n')

            outputFile.flush()
            cnt += len(tweets)

            if sys.stdout.isatty():
                print("\rSaved %i"%cnt, end='', flush=True)
            else:
                print(cnt, end=' ', flush=True)

        print("Downloading tweets...")
        got.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer, debug=debug)

    except getopt.GetoptError as err:
        print('Arguments parser error, try -h')
        print('\t' + str(err))

    except KeyboardInterrupt:
        print("\r\nInterrupted.\r\n")

    except Exception as err:
        print(traceback.format_exc())
        print(str(err))

    finally:
        if "outputFile" in locals():
            outputFile.close()
            print()
            print('Done. Output file generated "%s".' % outputFileName)

            print("Cleaning Tweets...")

            #Cleaning the data
            import pandas as pd
            data_1 = pd.read_csv(value) 
            #Check the tweet content
            data_1.fillna("",inplace=True)
            # Data Cleaning
            #Remove hashtags, links etc
            cleaned_tweets = []
            count = 0
            while count <= (data_1.shape[0])-1:
                val = data_1.text[count]
                remove_links = ' '.join(re.sub(r"http(s)?://((\w+).?){1,}", " ",val).split())
                remove_piclink = re.sub('pic.twitter.com/[A-Za-z0-9]+','',remove_links)
                remove_handles = re.sub(r'@[A-Za-z0-9_]+', '', remove_piclink)
                remove_hashtags = ' '.join(re.sub("#[A-Za-z0-9]+"," ",remove_handles).split())
                remove_dots = re.sub(r'…', '', remove_hashtags)
                cleaned_tweets.append(remove_dots)
                count = count + 1

            data = pd.DataFrame(cleaned_tweets,columns=["Cleaned Tweets"])
            data_1.drop(["text"],axis=1,inplace=True)
            result = pd.concat([data_1,data],1,ignore_index=True)
            result.columns = ['date','username','to','replies','retweets','favorites','geo','mentions','hashtags','id','permalink','text']
            cleaned_name = "Cleaned_" + value
            result.to_csv(cleaned_name,index=False)
            print('Done. Cleaned file generated as "%s".' % cleaned_name)


if __name__ == '__main__':
    main(sys.argv[1:])
