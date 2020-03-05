from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import SnowballStemmer

french_stemmer = SnowballStemmer('french')

class StemmedCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        analyzer = super(StemmedCountVectorizer, self).build_analyzer()
        return lambda doc: ([french_stemmer.stem(w) for w in analyzer(doc)])