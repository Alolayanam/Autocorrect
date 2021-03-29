import sys
import re
from collections import Counter
import numpy as np
import pandas as pd

# Open and read a text file
def read_data(file_name):
    words = []
    with open(file_name, "r") as f:
        content = f.read().lower()
    words = re.findall('\w+', content)
    return words

# Convert 'Words.txt' to a Python set to eliminate duplicates
word_l = read_data('shakespeare.txt')
vocab = set(word_l)
print(f"The first twenty words in the text are: \n{word_l[0:20]}")
print(f"There are {len(vocab)} words in the text." + '\n')


# get the word count of a given corpus, and the word count of a specific word
def count_data(word_l):
    word_count_dictionary = {}
    for word in word_l:
        if word not in word_count_dictionary:
            word_count_dictionary[word] = 1
        else:
            word_count_dictionary[word] += 1
    return word_count_dictionary

word_count_dictionary = count_data(word_l)

print(f"There are {len(word_count_dictionary)} key values pairs")
print(f"The count for the word 'long' is {word_count_dictionary.get('long', 0)}" + '\n')


# compute the probability of a word appears randomly from a given corpus, by using word count
# this will return a dictionary of keys and value of a probability in which a word will occur
def compute_probs(word_count_dictionary):
    total_prob = {}
    M = np.sum(list(word_count_dictionary.values()))
    for word, C in word_count_dictionary.items():
        total_prob[word] = float(C) / M
    return total_prob

total_prob = compute_probs(word_count_dictionary)
print(f"Length of probability is {len(total_prob)}")
print(f"Probability of ('long') is {total_prob['long']:.4f}" + '\n')


