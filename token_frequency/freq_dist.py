# Get Frequency Distribution of 50 most common words with a length greater
# than three characters  in Walt Whitman's 'I Sing the Body Electric'

import requests
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
import io
import csv

def main():
    # get poem text from Poetry DB
    req = requests.get ('http://poetrydb.org/title/I%20Sing%20the%20Body%20Electric/lines,author,title')
    if req.status_code == 200:	# if success
        poems = req.json()	# convert to JSON

        for poem in poems:

            # accumulate lines of poem into lines
            lines = ''
            for line in poem['lines']:
                lines += ' ' + line

            # calculate frquency distribution for words of length > 3
            fdist = FreqDist(word.lower() for word in word_tokenize(lines) if len(word) > 3)

            # ouput to CSV file
            with open ('token_count_LeavesOfGrass.csv', 'w', newline='') as csvfile:
                fieldnames = ['Word', 'Frequency']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for word, count in fdist.most_common(50):
                    writer.writerow({'Word': word, 'Frequency': count})


# main
main ()
