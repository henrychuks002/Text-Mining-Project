#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 15:34:41 2021

@author: Henry Chuks
"""

def classify(text):
    with open('Word.txt', 'r') as f:
        spam_words = f.read()
    if str(text).isupper():
        return "You've got one new spam mail"
    else:
        if any(word in text.lower().split() for word in spam_words.lower().split(', ')):
            return "You've got one new Spam mail"
        else:
            return "You have one new message"