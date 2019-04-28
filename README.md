# NLTK
Exploring NLTK at the suggestion of my Python 2 professor, Eric Darsow

Exploring NLTK. Each main file maps to a functionality within NLTK.

## Token Frequency
Text input from an API, the Poetry DB.
Uses NLTK's Text and word_tokenize functions. Counts unique tokens within the code.
Sorts tokens by highest to lowest count. Outputs each token with coresponding
count and percentake (that token's count / number all tokens).
### Files:
token_freq.py - code file

## Fequency Distribution
Text input from an API, the Poetry DB. 
Uses NLTK's word_tokenize and FreqDist to count unique tokens within the poem.
Outputs token and frequency of 50 most frequent, sorted on frequency, to a CSV file. 
### Files:
freq_dist.py - code file
token_count_LeavesOfGrass.csv - output file
