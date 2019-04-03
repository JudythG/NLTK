# Retreive data from STANDS4 Quotes API

# How make tokens in all_tokens lowercase (so "the" equals "The")?

import requests
import nltk

def code_dump():
    poems = req.json()
    all_tokens = set('')
    for poem in poems:
        #print ("Title: " + poem['title'])
    
        text_base = ''
        for line in poem['lines']:
            text_base += ' ' + line
        tokens = nltk.word_tokenize(text_base)
        text = nltk.Text(tokens)
        all_tokens = all_tokens.union( set(text) )

    freq_list = []
    for token in all_tokens:
        d = {'token': token, 'poems': []}

def main():
    req = requests.get ("http://poetrydb.org/title/Tiresias/lines.json")
    req = requests.get ("http://poetrydb.org/title/Defrauded I a Butterfly --/lines.json")
    if req.status_code == 200:
        poems = req.json()

        for poem in poems:

            lines = ''
            for line in poem['lines']:
                lines += ' ' + line
            poem_text = nltk.word_tokenize(lines)
            poem_tokens = nltk.Text(poem_text)

            print (poem)
            #freq_list = []
            for token in sorted(set(poem_tokens)):
                tok_count = poem_text.count (token)
                tok_percent = tok_count / len(poem_text)
                print (token + "\t" + str(tok_count) + '\t' + str(tok_percent))
                #freq = {'token': token, 'frequency': poem_text.count (token)}
                #freq_list.append (freq)

# main
main ()
