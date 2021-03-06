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


# make a list of split words
# (deletion function) return all possible words result from deleting one character from a given word
def letter_delete(word, verbose=False):
    letter_delete = []
    split_letter = []
    split_letter = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    letter_delete = [L + R[1:] for L, R in split_letter if R]
    if verbose: print(f"input word : {word}, \nsplit_letter = {split_letter}, \nletter_delete = {letter_delete}")
    return letter_delete

delete_word_letter = letter_delete(word="car", verbose=True)
print('\n')


# (switch function) return all possible words of switching two letter from a given word
def letter_switch(word, verbose=False):
    letter_switch = []
    split_letter = []

    def f(L, R):
        return L[:-1] + R[0] + L[-1] + R[1:]

    split_letter = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    letter_switch = [f(L, R) for L, R in split_letter if L and R]
    if verbose: print(f"Input word : {word} \nsplit_letter = {split_letter} \nswitch_l = {letter_switch}")
    return letter_switch

switch_word_letter = letter_switch(word="teh", verbose=True)
print('\n')


# (replace function) return all possible words with one replaced letter from a given word
def letter_replace(word, verbose=False):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    replace_letter = []
    split_letter = []
    split_letter = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    replace_set = [L + C + R[1:] for L, R in split_letter if R for C in alphabet if C is not R[0]]
    replace_letter = sorted(list(replace_set))

    if verbose: print(f"Input word : {word} \nsplit_letter = {split_letter} \nreplace_letter {replace_letter}")
    return replace_letter

replace_letter = letter_replace(word='car', verbose=True)
print('\n')


# (insertion function) return all possible words with a letter inserted from a given word at each character
def letter_insert(word, verbose=False):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    insert_letter = []
    split_letter = []
    split_letter = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    insert_letter = [L + C + R for L, R in split_letter for C in alphabet]
    if verbose: print(f"Input word : {word} \nsplit_letter = {split_letter} \ninsert_letter = {insert_letter}")
    return insert_letter

insert_letter = letter_insert(word='be', verbose=True)
print('\n')


# (editing function) return all possible edits, consisting of insert, delete, replace and switch
def one_letter_edit(word, allow_switches=True):
    edit_one_set = set()
    edit_one_set = edit_one_set | set(letter_delete(word)) | set(letter_insert(word)) | set(letter_replace(word))
    if allow_switches:
        edit_one_set |= set(letter_switch(word))
    return edit_one_set

tmp_word = "be"
tmp_edit_one_set = one_letter_edit(tmp_word)
tmp_edit_one_l = sorted(list(tmp_edit_one_set))

print(f"input word : {tmp_word} \nThe result of editing one letter: \n{tmp_edit_one_l}\n")
print(f"The type of the returned object should be a set {type(tmp_edit_one_set)}")
print(f"Number of outputs from editing one letter on word('be') is {len(one_letter_edit('be'))}")
      
      
# return all the possible edits on a single word, and get two edits modification
def two_letters_edit(word, allow_switches = True):
    edit_two_set = set()
    one_letter =  one_letter_edit(word, allow_switches)
    for word in one_letter:
        edit_two_set |= one_letter_edit(word,allow_switches)
    return edit_two_set

tmp_edit_two_set = two_letters_edit("b")
tmp_edit_two_l = sorted(list(tmp_edit_two_set))
print(f"Number of strings with edit distance of two: {len(tmp_edit_two_l)}")
print(f"First 20 strings {tmp_edit_two_l[:20]}")
print(f"Last 20 strings {tmp_edit_two_l[-20:]}")
print(f"Number of strings that are 2 edit distances from 'be' is {len(two_letters_edit('be'))}")

