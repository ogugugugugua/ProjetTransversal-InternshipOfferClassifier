#imports

import numpy as np
import pandas as pd
import collections

filepath="../../frontend/dataset/texte.txt"

keywords = {
    "développement": 0,
    "web" : 0,
    "développeur" : 0,
    "machine" : 1,
    "learning" : 1,
    "data" : 1
}

categories = ["Développement", "Machine Learning"]

fileContent = ""
with open(filepath) as file:
    fileContent = file.read()

# count times of appearance of each word
frequency = dict(collections.Counter(fileContent.split()))

dataframe = pd.Series(frequency)
print(dataframe)