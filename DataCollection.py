"""
Objective:

Pull off of metrolyrics.com
1. Select an Artist and Pull 30 most popular songs by website
2. Enter each website, pull song text 
3. Filter Lyrics
4. Create text file

ex. Tyga
Pull Songs from: https://www.metrolyrics.com/tyga-lyrics.html
Pull Lyrics from Song 1: https://www.metrolyrics.com/taste-lyrics-tyga.html#/startvideo
Pull Lyrics from Song...
Pull Lyrics from Song 30: https://www.metrolyrics.com/cash-money-lyrics-tyga.html 

5. Repeat for other artists (Manually)

"""
import string
import re
import requests 
import urllib.request 
from bs4 import BeautifulSoup

### OBJECTIVE #1 - Pull 30 Most Popular Songs by Website
def createLyricFile(url, title):
    website_list = pullLyricWebsites(url) #1 
    text = pullLyrics(website_list) #2
    createFile(title, text)

def pullLyricWebsites(url): #1 - Confirmed, requires 4 latest releases for correct index
    response = requests.get(url)

    # Parse the html with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    """
    HTML:
    <tbody>
    <tr> (1 set up for each song)
    <td>
    <a href = lyric website URL
    """
    website_list = [] # create list for websites
    # tbody = soup.find_all('td') # contains text, with website urls following 
    i = 0
    for link in soup.find_all('a'):
        if i >= 18 and i < 43: # 18 index corresponds to first song (mostly)
            website_list.append(link.get('href')) 
        i += 1
    
    return website_list

def pullLyrics(website_list): #2 - In progress 
    print(website_list)
    text = ""

    for i in range(len(website_list)):
        # for loop, process each website address and append text
        response = requests.get(website_list[i])

        # Parse the html with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('p', attrs = {'class', 'verse'}):
            line = str(link)
            line = re.sub('<.+>', '', line)
            for word in line.split():
                word = word.strip(string.punctuation + string.whitespace)
                word = word.lower()
                text += word + ' '
     
    return text 

def createFile(title, text):
    name = title + ".txt"
    my_file = open(name, "w+", encoding = "utf-8")
    my_file.write(text)


### MAIN
def main():
    createLyricFile("https://www.metrolyrics.com/cardi-b-lyrics.html", "Cardi B")

if __name__ == '__main__':
    main()

