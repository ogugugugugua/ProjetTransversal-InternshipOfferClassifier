from joblib import load
import numpy as np
import pandas as pd
import os

def predict(text: str) -> dict:
    clf = load(os.path.join(os.path.dirname(__file__), "model_mnb.joblib"))
    probabilities = clf.predict_proba([text])
    classes = clf.classes_
    result_probability = pd.DataFrame({'label': classes, 'probability': probabilities[0]}, columns=["label", "probability"])
    labels_dict = result_probability.to_dict()

    return labels_dict