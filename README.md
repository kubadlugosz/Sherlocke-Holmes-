# Sherlocke-Holmes-
"""
Basic Sentiment Analysis

The goal of this project is to familiarize ourselves with the processing of text files using Python (without importing specialized libraries for text parsing) and to practice working with Python data types, such as strings, lists, sets, dictionaries, and files.


We want to analyze the sentiment of the text on the sentence level. That is, we want to classify each sentence in this text as having either positive, neutral, or negative sentiment. The following three sentences illustrate each sentiment type. For example,

I am so excited about my new car. (Positive sentiment)

I feel tired and moody today. (Negative sentiment)

There is parked car on the street. (Neutral sentiment)

To aid us in deciding which words carry positive, neutral, or negative sentiment, we will consult the two files  positivesentimentwords.txt and negativesentimentwords.txt. Each of these files contains a list of words that are generally associated with positive/negative sentiment.

The classification of each sentence as being positive, neutral, or negative is based on the following assessment. If more words in a sentence carry the positive sentiment than negative, we will classify that sentence as having a positive sentiment. If the number of positive and negative words in a sentence is equal, we will classify that sentence as neutral. Otherwise, the sentence is classified as having a negative sentiment.

Upon completion, this code should print sentence counts for each sentiment type:

Positive:
Negative:
Neutral :
#total words around 4300
#negative=1500
#positive=600
#neutral=2200


"""
