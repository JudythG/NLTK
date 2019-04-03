# Retreive data from STANDS4 Quotes API

import requests
import nltk
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

def main():
    req = requests.get ("http://poetrydb.org/title/Tiresias/lines.json")
    #req = requests.get ("http://poetrydb.org/title/Defrauded I a Butterfly --/lines.json")
    if req.status_code == 200:
        poems = req.json()

        for poem in poems:

            lines = ''
            for line in poem['lines']:
                lines += ' ' + line
            poem_text = nltk.word_tokenize(lines)

            fdist = FreqDist(word.lower() for word in word_tokenize(lines))
            print (fdist.most_common(25))

# main
main ()
