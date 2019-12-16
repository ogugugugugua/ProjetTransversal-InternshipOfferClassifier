from flask import Flask, request, jsonify
from classifier import SimpleClassifier

app = Flask(__name__)
classifier = SimpleClassifier()

@app.route("/", methods = ["POST"])
def predict():
  json_data = request.json
  text = json_data['text']
  return classifier.predict(text)

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')