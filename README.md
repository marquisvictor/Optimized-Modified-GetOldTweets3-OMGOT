# Optimized-Modified-GetOldTweets3-OMGOT
GetOldTweets-Python is a project written in Python to mine old and backdated tweets, It bypasses some limitations/restrictions of the Twitter API. This Repo houses an improvement fork of the original GetOldTweets Library by [Jefferson Herique](https://github.com/Jefferson-Henrique/GetOldTweets-python). The improvement makes running this package on Windows OS seamless with Python 3.x. 


 ## Details
 
This tool was built out of the need to eliminate the barriers that the Twitter API imposes so as to help researchers, businesses and organizations get all the tweets data they need for various analysis in their different line of operations, with ease and from command line, meaning no prior extensive programming knowledge is required. 
BigTweet provides a means of getting old/backdated twitter data for analysis, bypassing the rate limits and restrictions from twitter API, giving you unlimited tweet textual data along with some other metadata such as; dates and time information, likes, retweets, replies, and tweet geolocation.


## Operating system
OMGOT was tested on Ubuntu distribution of the Linux operating system and on Windows 7, 8, 10.



## Command Line Arguments

This package was optimized to work efficiently and seamlessly on both Windows Command prompt (CMD), and on UNIX Terminal. Below are some command line arguments which is by no means exhaustive. run `python cli.py --help` in terminal to get the full argument options.


  - username (**str**): An optional specific username from a twitter account. Without "@".
  - since (**str. "yyyy-mm-dd"**): A lower bound date to restrict search.
  - until **(str. "yyyy-mm-dd"**): An upper bound date to restrist search.
  - search (**str**): A query text to be matched.
  - near(**str**): A reference location area from where tweets were generated
  - csv: Write as a .csv file
  - json: Write as a .json file
  - count: Display the number of tweets scraped at the end of the session
  - year: Filter a tweet before a specified year


## Usage - Very Important to Understand.

1. Clone or download the repo to your local machine.
2. Unzip it.
3. cd to the unzipped Optimized-Modified-GetOldTweets3-OMGOT-master folder
4. cd again to the GetOldTweets3-0.0.10 folder inside unzipped Optimized-Modified-GetOldTweets3-OMGOT-master folder, and fire up command prompt or terminal right there. 
5. then run the codes in the examples below. 

Please Feel free to customize, change the parameters/arguments as used in the examples below according to the needs of your project. 

## Use Cases

**Use case 1 - Get all the tweets by a user:**

```
python cli.py --username "irekponorVictor"
``` 

**Use case 2 - Get all tweets tweeted from a user since 2015-12-20 20:30:15**:
```
python cli.py --username "irekponorVictor" --since "2015-12-20 20:30:15
```

**Use case 3 - Get all tweets tweeted from a user from January 2019 - December 2019 and save in a csv file**:
```
python cli.py --username "irekponorvictor" --since "2019-01-01" --until "2019-12-31" -o user.csv --csv
```

**Use case 4 - Get tweets from a radius of 1km around a place in Lagos, Nigeria and export them to a csv**
```
python cli.py -g="6.465422, 3.406448, 1km" -o Lagos.csv --csv
```

**Use case 5 - Get every tweet containing the word "governance" from every where**
```
python cli.py -s governance
```
---

I've added my local enviroment dependencies in a requirements.txt file, so if any body has issues with the dependencies or environments, do a ```pip install -r requirements.txt```.

If you have any question, or need extra help, you are welcome to connect with me on any of my social media below:

#### [connect with me on linkedIn](https://www.linkedin.com/in/veirekponor/).
#### [Twitter](https://twitter.com/IrekponorVictor).
#### [Read my latest write-ups on medium](https://medium.com/@IrekponorVictor).
