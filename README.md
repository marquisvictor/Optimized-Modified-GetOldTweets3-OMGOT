# Modified-GetOldTweets3
GetOldTweets-Python is a project written in Python to mine old and backdated tweets, It bypasses some limitations/restrictions of the Twitter API. This Repo houses an improvement fork of the original GetOldTweets Library by [Jefferson Herique](https://github.com/Jefferson-Henrique/GetOldTweets-python). The improvement makes running this package on Windows OS seamless with Python 3.x. 


 ## Details
Before coming here to get backdated timeline tweets, you might have gone to Twitter to create a Developer account, before the sad reality dawns on you that you can not mine tweets older than 7 days, using twitter's rest API, unless you pay and even when you do, you are restricted to a limit of 100 tweets daily. Just how slow would that be if you intend to mine say 10 years worth of textual big data for data analysis. You might have also tried "Googling" some other methods to mine old tweets, you might have seen different sites, libraries or tools you didnt know how to use, and all sorts of confusing information on the web. This modified getoldtweets3 library helps you download backdated-timeline twitter data easily and without hassles from command line, either on windows OS, ubuntu-linux OS, or Mac OS. You only need to have python installed on your machine, yeah. You also need to set the environment variable or install python in such a way that you can call it from the command line. [check here](https://stackoverflow.com/posts/54934172/edit)


## Prerequisites
This packages assumes you are running python version 3.x on your local machine, and that you have already set the python environment variable path, so you can interactively fire up python from command prompt or terminal without getting any error. If you haven't, kindly follow this [stackoverflow answer](https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages) for guidance, [this too](https://stackoverflow.com/posts/54934172/edit). After doing all those, the next major packages you need to install are pyQuery, and Lxml for handling requests and xml/html documents. Easy stuff, just use `pip install pyquery` and `pip install lxml`   


## Components
- When you run this package from command line, it typically returns the following as columns in an output.csv file. It should be noted before hand that the geo attribute returns an empty column. So you use the geographical coordinate as well as the search radius to get a boundary within which you want to retrieve your tweets data. 
  - id (str)
  - permalink (str)
  - username (str)
  - text (str)
  - date (date)
  - retweets (int)
  - favorites (int)
  - mentions (str)
  - hashtags (str)
  - geo (str)


## Command Line Arguments

  - username (str): An optional specific username from a twitter account. Without "@".
  - since (str. "yyyy-mm-dd"): A lower bound date to restrict search.
  - until (str. "yyyy-mm-dd"): An upper bound date to restrist search.
  - querysearch (str): A query text to be matched.
  - toptweets (bool): If True only the Top Tweets will be retrieved.
  - near(str): A reference location area from where tweets were generated.
  - within (str): A distance radius from "near" location (e.g. 15mi).
  - maxtweets (int): The maximum number of tweets to be retrieved. If this number is unsetted or lower than 1 all possible tweets will be retrieved.


## Usage

Clone or download the repo to your local machine, then cd into the downloaded GetOldTweets3 folder, and open up cmd right in that same folder. and run the following codes in the examples below. Feel free to customize, change the parameters/arguments according to the need of your project. 

## Use Cases

**Use case 1 - Get the last 50 top tweets by username:**
```
python GetOldTweets3.py --username "mo4president" --toptweets --maxtweets 50
```

**Use case 2 - Get 500 tweets by the username and bound dates**:
```
python GetOldTweets3.py --username "mo4president" --since 2017-05-10 --until 2019-05-10 --maxtweets 500
```

**Use case 3 - Get tweets by language and keyword search:**
```
python GetOldTweets3.py --querysearch "football" --lang es --maxtweets 100
```

**Use case 4 - Get tweets by querysearch and geo coordinates:**
```
python GetOldTweets3.py --querysearch "BBNaija" --near "6.52, 3.37" --within 40km --maxtweets 100
```

Let me know if you have any issues or concerns running these codes in any way. If you followed the instructions carefully, it works on all OS's CLI.        





                                              BELLA CIAO!!!!!
