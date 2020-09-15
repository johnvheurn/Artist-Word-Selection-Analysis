"""

I want to generate a histogram of what words Tyga uses in his songs

"""
import string
import re

import plotly.graph_objects as go

### process file to generate word histogram

def process_file(filename):
    hist = {}
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist
 
def process_line(line, hist):
    line = line.replace('-', ' ')
    for word in line.split():
        hist[word] = hist.get(word, 0) + 1

### Sort by most common

def most_common(hist): # Takes dictionary, returns entire list 
    t = []
    for key, value in hist.items():
        t.append((value, key))
        t.sort(reverse=True)
    return t

def printMostCommon(hist, artist):
    print("Artist: ", artist)
    print("Total Words:" , total_words(hist))

    t = most_common(hist)
    print('The most common words are:')
    rank = 1
    for freq, word in t[:50]:
        print(rank, word, freq, sep='\t')
        rank += 1
    return    

def total_words(hist):
    return sum(hist.values())

### Enter word, identify what artist uses it the most

def wordCompare(words, artists, hist):
    """
    word: word to compare, based on percentage 
    artist: list of artists
    hist: list of dictionary variables corresponding to artist
    """
    # create list of tuple (artist, percentage_word_used)
    comp = []
    perc = 0
    for i in range(len(artists)):
        for j in range(len(words)):
            if hist[i].get(words[j]) == None:
                perc += 0
            else:
                perc += hist[i].get(words[j]) 
        perc /= total_words(hist[i])
        perc *= 100
        element = (artists[i], perc)
        comp.append(element)
        perc = 0
    
    comp.sort(key = lambda x: x[1], reverse = True)

    rank = 1
    col1 = []
    col2 = []
    for i in range(len(artists)):
        col1.append(comp[i][0])
        col2.append(comp[i][1])

    word_print = "["
    for i in range(len(words)):
        word_print += words[i] 
        if not i == len(words)-1:
            word_print += ", "
    word_print += "]"

    fig = go.Figure(data = [go.Table(header = dict(values = ['Artist', "Words (%): {}".format(word_print)]),
                            cells = dict(values = [col1, col2]))])
    fig.show()
    return  
    
    # print 

### MAIN
def main():

    # List of artist files, process to read
    artists = ['2-Chainz', '6IX9INE', '50 Cent', 'A Boogie Wit Da Hoodie', 'Ace Hood',  #5 - GOOD
        'Asap Rocky', 'Childish Gambino', 'Dr. Dre', 'Drake', 'Eminem',                 #10 - GOOD
        'French Montana', 'G-Eazy', 'Gucci Mane', 'Jay Z', 'Kanye West',                #15 - GOOD
        'Kendrick Lamar', 'Kid Cudi', 'Kodak Black', 'Lil Wayne', 'Logic',              #20 - GOOD
        'Ludacris', 'Mac Miller', 'Nicki Minaj', 'Post Malone', 'Rae Sremmurd',         #25 - GOOD
        'Rick Ross', 'Snoop Dogg', 'T.I', 'Tupac', 'Tyga',                              #30 - GOOD
        'Doja Cat', 'Cardi B']                              

    # Process data, return list of dictionaries for each artist
    
    hist = []
    for i in range(len(artists)):
        hist.append(process_file("artists/" + artists[i] + ".txt"))

    
    words = ['money']
    wordCompare(words, artists, hist)
    

    printMostCommon(hist[1], artists[1])

if __name__ == '__main__':
    main()


 


