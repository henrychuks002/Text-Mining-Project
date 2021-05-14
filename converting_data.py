#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 21:39:32 2021

@author: Henry Chuks
"""

import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


def text_cleaning(text):
    remove_punctuation = [char for char in text if char not in string.punctuation] #removing punctuation from each message
    remove_punctuation = ''.join(remove_punctuation) #joins each word back to make a sentence
    return [word for word in remove_punctuation.split() if word.lower() not in stopwords.words('english')] #eliminate english stop words

def convert_data(data):
    x = data['message']
    
    vectorizer = CountVectorizer(analyzer=text_cleaning).fit(x) #Vectorizing and counting words for each sample
    vector = vectorizer.transform(x)

    tfidf = TfidfTransformer().fit(vector) #TF-IDF Term Frequency Inverse Document Frequency, to find out the most important words in a sample
    X = tfidf.transform(vector)
    return X

def target(data):
    y = data['Class']
    
    y = y.map({'Spam':0, 'Inbox':1}) #label encoding, encoding the target feature
    return y
