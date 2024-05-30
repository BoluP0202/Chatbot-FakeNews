
import pandas as pd
import numpy as np
import nltk
import re
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize,sent_tokenize
import category_encoders as ce
from sklearn.model_selection import train_test_split
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

load_model = pickle.load(open('LR-Lemm-TFIDF.sav', 'rb'))
load_vector = pickle.load(open('TFIDF.sav', 'rb'))

def load_model(model_file):
    with open(model_file, 'rb') as file:
        model = pickle.load(file)
    return model

def load_vectorizer(vector_file):
    with open(vector_file, 'rb') as file:
        vector = pickle.load(file)
    return vector

def preprocess_text(text):
    lemmatizer = WordNetLemmatizer()
    text = re.sub(r'U.S.', 'usa', text)
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    text = text.split()
    text = [lemmatizer.lemmatize(word) for word in text if not word in stopwords.words('english')]
    text = ' '.join(text)
    return text

def predict_reality(text, model, vector):

    preprocessed_text = preprocess_text(text)
    vectorised_text = vector.transform([preprocessed_text])
    reality = model.predict(vectorised_text)
    return reality[0]

def checker(text):
    model = load_model("LR-Lemm-TFIDF.sav")
    vectorizer = load_vectorizer("TFIDF.sav")
    if len(text) < 30:
        print("that seemes a little short, That's probably not enough to guess accurately. Also while I'll give an answer i can't tell you much about something that isn't an article")
    reality = predict_reality(text, model, vectorizer)
    return reality
    # 1 is_true

negative_responses = ["no", "n", "nope"]
pos_resp =["y", "yes", "yup"]

#done = False
#while not done:
    #message = input("Do you have news")
    #if message.lower() in negative_responses:
        #print("okay")
        #done = True
   #elif message.lower() in pos_resp:
        #news_to_check  = input("Please submit a headline")

        #if checker(news_to_check) == 1:
            #print("This Headlines seems to be legit")
        #else:
            #print("seems pretty sus")