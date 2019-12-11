# -*- coding: UTF-8 -*-

import numpy as np
import collections
import json


def softmax(x):
    """
    Compute the softmax function for each row of the input x.
    Arguments:
    x -- A N dimensional vector or M x N dimensional numpy matrix.
    Return:
    x -- You are allowed to modify x in-place
    """
    orig_shape = x.shape

    if len(x.shape) > 1:
        # Matrix
        exp_minmax = lambda x: np.exp(x - np.max(x))
        denom = lambda x: 1.0 / np.sum(x)
        x = np.apply_along_axis(exp_minmax, 1, x)
        denominator = np.apply_along_axis(denom, 1, x)

        if len(denominator.shape) == 1:
            denominator = denominator.reshape((denominator.shape[0], 1))

        x = x * denominator
    else:
        # Vector
        x_max = np.max(x)
        x = x - x_max
        numerator = np.exp(x)
        denominator = 1.0 / np.sum(numerator)
        x = numerator.dot(denominator)

    assert x.shape == orig_shape
    return x


def findCategory(filePath, stopWordsPath, categoriesPath):
    # get the text file content
    fileContent = ""
    with open(filePath) as file:
        fileContent = file.read()

    # count times of appearance of each word
    frequency = dict(collections.Counter(fileContent.split()))
    print(frequency)
    
    # filter out stop words
    stopwords = set()
    with open(stopWordsPath) as file:
        for word in file:
            stopwords.add(word[:-1])

    for word in stopwords:
        frequency.pop(word, None)

    # get the times of appearance of each word
    values = list(frequency.values())
    # count the possibility of each word by using softmax
    softmaxValues = softmax(np.array(values))

    # translate to softmax probability
    for i, k in enumerate(frequency):
        frequency[k] = softmaxValues[i]


    # sort by most frequent words
    frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    # get the whole default categories
    categories = []
    with open(categoriesPath) as file:
        for category in file:
            categories.append(category[:-1])

    # determine category
    for (word, percentage) in frequency:
        if word in categories:
            # we got the category by finding the most possible word in the list of category
            print(word, " : ", percentage)
            #return word


if __name__ == "__main__":
    findCategory("../../frontend/dataset/texte.txt", "stopWordsFR.txt", "categories.txt")
