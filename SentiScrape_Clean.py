import csv
import pandas as pd
from unidecode import unidecode

#Define the cleaning function
def twitter_clean():

#This opens the Coventry csv file and defines the name of the newly created csv file which the cleaned tweets will be placed
    with open(r"C:\Users\JDog\Desktop\SentiScrape Code\Coventry.csv", newline='', encoding='utf-8') as old, open('cleantwt.csv', 'w', newline='') as new:
        reader = csv.reader(old)
        writer = csv.writer(new)


#List of unwanted characters
        hashtag = '#'
        border = '['
        border_close = ']'
        symbol = '@'
        link = 'https://'
        end = "|'"
        hypo = "'"
    
#The map function makes the code run through all the code and uses the unidecode to remove any unwanted unicode characters        
        for row in reader:
            row = str(row)

            #Replaces the pre-defined parameters with nothing, essentially removing the unwanted symbols
            new_row = str.replace(row, hashtag,'').replace(symbol, '').replace(border,'').replace(border_close,'').replace(link,'').replace(hypo,'')

            #The data is placed in the lower case to allow for easy management
            new_row = new_row.lower()
            
            #writes to the new file making sure it is decoded into ASCII
            writer.writerow(map(unidecode, new_row.split('\n')))
            
            
#calling the function
twitter_clean()













