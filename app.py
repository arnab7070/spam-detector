from flask import Flask, jsonify, request
import json
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


app = Flask(__name__)

# Load the model and vocabulary
try:
    loaded_model = pickle.load(open('model.pkl', 'rb'))
    loaded_vocabulary = pickle.load(open('vocabulary.pkl', 'rb'))
    
    # Initialize the vectorizer with the loaded vocabulary
    vectorizer = TfidfVectorizer(vocabulary=loaded_vocabulary)
    
    # Manually set idf_ to 1.0 for all terms
    vectorizer.idf_ = np.ones(len(loaded_vocabulary))
except Exception as e:
    print(f"Error loading model/vocabulary: {e}")

def predict(comment):
    try:
        # Transform the input text using the vectorizer
        new_comment = vectorizer.transform([comment])
        # Predict using the loaded model
        prediction = loaded_model.predict(new_comment)
        return "Spam" if prediction[0] == 1 else "Not spam"
    except Exception as e:
        return f"Unexpected Error: {str(e)}"

@app.route('/')
def home():
    return 'Spam Detection Server is Running!'

@app.route('/predict', methods=['POST'])
def predict_api():
    try:
        data = request.get_json()
        comment = data.get('comment', '')
        result = predict(comment)
        return jsonify({'result': result})
    except Exception as e:
        app.logger.error(f"Error in predict_api: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500