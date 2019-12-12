#imports

import numpy as np
import pandas as pd
import collections
import re


class SimpleClassifier:
    def preprocess(self, text):
        return text.lower()

    def predict(self, text):

        text = self.preprocess(text)
        words=re.findall("[\w']+", text)

        # count times of appearance of each word
        frequency = dict(collections.Counter(words))

        dataframe = pd.DataFrame(frequency.items(), columns=["word", "n_appear"])

        # Nettoyage

        stopwords = set()
        stopwords_path = "stopWordsFR.txt"
        with open(stopwords_path) as file:
            for word in file:
                stopwords.add(word[:-1])

        dataframe['word'] = dataframe['word'].astype(str)

        filtered_df = dataframe[~dataframe["word"].isin(stopwords)]

        # Attribution des catégories

        from collections import defaultdict

        keywords = {
            "développement": 0,
            "web" : 0,
            "développeur" : 0,
            "machine" : 1,
            "learning" : 1,
            "data" : 1
        }

        categories = {
            "Developpement",
            "Machine Learning"
        }

        keyword_df = pd.DataFrame(keywords.items(), columns=["word", "category"])
        categories_df = pd.DataFrame(categories, columns=["label"])

        in_text_kw_df = keyword_df.merge(filtered_df, left_on='word', right_on='word')
        cat_count = in_text_kw_df.groupby(['category']).sum()



        categories_df['n_appear'] = cat_count['n_appear']
        categories_df['exponential'] = np.exp(categories_df['n_appear'])
        exp_sum = np.sum(categories_df['exponential'])
        if exp_sum != 0: 
            categories_df['probability'] = categories_df['exponential'] / exp_sum
        else:
            categories_df['probability'] = 1 / categories_df.shape[0]

        # Prepare dataframe for JSON export

        json_df = categories_df[['label', 'probability']]
        json_df = json_df.fillna(0)

        result = json_df.to_json(orient='records')
        
        return result