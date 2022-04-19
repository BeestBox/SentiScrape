#Importing the Social Reaper library#
from socialreaper import Twitter
from socialreaper.tools import to_csv

#Defining the Web scraping portion of the application, this function will be called upon later
def Web_Scraper():

#Input of authentication tokens to connect to twitter API
    auth_pass = Twitter(app_key=="",app_secret== "",oauth_token== "", oauth_token_secret="") 

#Asks for user input in order to gauge a hashtag parameter
    hashtag=input("What hashtag would you like to extract from?")         

#This extracts the tweets and extracts it to a csv file
    twt_para = auth_pass.search("#"+hashtag, count=500,  exclude_replies=True, include_retweets=False)
    
    to_csv(list(twt_para), filename= "hashtag.csv")

#Function is called 
Web_Scraper()
