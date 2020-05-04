from flask import Flask, render_template
from db_connector import DBConnector
from utils import abs_path
import os
import json

app = Flask(__name__)

def categories():
    
    con = DBConnector(abs_path('databases/offer_classification.db'))
    return con.fetch_categories()

def offers():
    
    con = DBConnector(abs_path('databases/offer_classification.db'))
    return con.fetch_offers()

def fileDict():
    
    path = '.\static\offers'
    result = {}
    
    for r, d, f in os.walk(path):
        for file in f:
            id = r.split('\\')[-1]
            result[int(id)] = file

    return result

@app.route('/')
def server():
    
    return render_template('index.html', categories = categories(), offers = offers(), fileDict = fileDict())

if __name__ == '__main__':
    app.run()
