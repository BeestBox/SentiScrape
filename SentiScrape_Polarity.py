from textblob import TextBlob
import csv
from textblob.sentiments import NaiveBayesAnalyzer

#The file that textblob is going to manipulate
myfile = open(r"C:\Users\JDog\Desktop\SentiScrape Code\cleantwt.csv", "r")

#This loop runs through the csv file line by line
while myfile:
    line  = myfile.readline()
    if line == "":
        break
    #This sets the values which we use within our If statement 
    Positive = TextBlob(line).sentiment
    Senti_Score = TextBlob(line).polarity
    #Anything with a polarity of over 0.5 is classified as positive, this loop checks if it is above 0.5 and if so prints to the terminal and to the doc
    if Senti_Score >= 0.5:
        print (Senti_Score, Positive, line)
        with open('positive.csv', 'w', newline='') as extract_positive:
            extract_positive.write(line)

    
       
    
    
