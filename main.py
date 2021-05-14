#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 13:11:52 2021

@author: Henry Chuks
"""
import streamlit as st
import classify_text as ct
import pandas as pd
import converting_data as cd
import pickle
# =============================================================================
# import os
# import sys
# =============================================================================

header = st.beta_container()
dataset = st.beta_container()
user_testing = st.beta_container()
model_testing = st.beta_container()

with open("RandomFC.pk1","rb") as f:
    classifier = pickle.load(f)

with header:
    st.title("Text mining model deployment - Streamlit application")
    st.markdown('**What is Text Classification?**')
    st .write('''
             Text classification also known as text tagging or text categorization is\n \
             the process of categorizing text into organized groups. By using Natural Language Processing (NLP),\n \
             text classifiers can automatically analyze text and then assign a set of pre-defined tags or categories based on its content.
             ''')
    st.write('''
             This project is about the email classification, a model that classifies messages into spam or inbox. It takes a particular
             message or each message in a dataset and checks if it contains spam trigger word for each word in a list of spam trigger words.
             The model flags any message as **spam** if does contain any of the spam trigger word or classifies it as **inbox** if it doesn't
             '''
            )
    
with user_testing:
    st.header('User testing of the model')
    st.write('''
             Here is to test the model, the model workability
             ''')
    sender, receiver = st.beta_columns(2)
    sender.subheader("Sender")
    message = sender.text_area('Compose message here:')
    receiver.subheader("Receiver")
    if st.button('Send'):
        receiver.write(message)
        result = ct.classify(message)
        receiver.success(result)
    

with dataset:
    st.header('Overview of the train data')
    st.write('''
             The dataset below shows a small sample of what the train data looks like. It contains only two columns, the message and the
             class. The data was gotten from https://archive.ics.uci.edu/ml/datasets.php. This data will undergo through some text cleaning
             and transformation via count vectorizer and tfidf. Basically what this means is converting the messages into a language the computer 
             understands. Machine learning models don't understand the English language. They work with only numbers. 
             ''')
    dataset = pd.read_csv('train_data.csv')
    st.write(dataset.head())
    
with model_testing:
    st.header('Model testing with data')
    st.write('Here is to upload any test data and show prediction result')
    file = st.file_uploader("Upload Data File", type='csv')
    show_file = st.empty()
    
    if not file:
        show_file.info("Please Upload a data file: {}".format(''.join("csv")))
        
    content = file.getvalue()
    df = pd.read_csv(file)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df.dropna(axis=0)
    st.dataframe(df.head(10))
    st.write('''
             A small sample of your test data is shown above, in general your test data contains {} columns and {} rows. Click the
             **predict** button below to get the results of your test data
             '''.format(df.shape[1], df.shape[0]))
    var = cd.convert_data(df)
    st.write('Transfromed dataset shape: {}'.format(var.shape))
    if st.button("Predict"):
        prediction = classifier.predict(var)
        prediction = prediction.map({0:"Spam", 1:"Inbox"})
        st.write("Your test data results are")
        st.success(prediction)
        
    