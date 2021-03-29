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

