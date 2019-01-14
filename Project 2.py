"""
Basic Sentiment Analysis

The goal of this project is to familiarize ourselves with the processing of text files using Python (without importing specialized libraries for text parsing) and to practice working with Python data types, such as strings, lists, sets, dictionaries, and files.

Download the text of the ebook The Hound of the Baskervilles by A. Conan Doyle from our course website, along with two files: positivesentimentwords.txt and negativesentimentwords.txt.

We want to analyze the sentiment of the text on the sentence level. That is, we want to classify each sentence in this text as having either positive, neutral, or negative sentiment. The following three sentences illustrate each sentiment type. For example,

I am so excited about my new car. (Positive sentiment)

I feel tired and moody today. (Negative sentiment)

There is parked car on the street. (Neutral sentiment)

To aid us in deciding which words carry positive, neutral, or negative sentiment, we will consult the two files  positivesentimentwords.txt and negativesentimentwords.txt. Each of these files contains a list of words that are generally associated with positive/negative sentiment.

The classification of each sentence as being positive, neutral, or negative is based on the following assessment. If more words in a sentence carry the positive sentiment than negative, we will classify that sentence as having a positive sentiment. If the number of positive and negative words in a sentence is equal, we will classify that sentence as neutral. Otherwise, the sentence is classified as having a negative sentiment.

Upon completion, your code should print sentence counts for each sentiment type:

Positive:
Negative:
Neutral :
#total words around 4300
#negative=1500
#positive=600
#neutral=2200
#pcnt=0
ncsnt=0
necnt=0
P=[]
N=[]
Ne=[]
S=[a,b,c,d,e,f]
if len(set(P).intersection(set(S)))>len(set(N).intersection(set(S))):
    pcnt+=1
elif len(set(P).intersection(set(S)))<len(set(N).intersection(set(S))):
  ncnt +=1

"""

def text_file(text,positive,negative):
    pcnt = 0
    ncnt = 0
    neut_cnt = 0
    P=[]
    N=[]
    with open(text,'r',errors='ignore') as f:
        text = f.read()
        text = text.replace("\n",' ')
        text = text.replace('?','.')
        text = text.replace('!', '.')
        text = text.replace(':', '')
        text = text.replace('-', '')
        text = text.replace('(', '')
        text = text.replace(')', '')
        text = text.replace(',','')
        text = text.lower()
    with open(positive,"r") as f1:
        for i in f1:
            i=i.replace("\n","")
            P.append(i)
    with open(negative, "r") as f2:
        for i in f2:
                i = i.replace("\n", "")
                N.append(i)

    sentences=text.split(".")

    for sentence in sentences:
        words = sentence.split(" ")
        words = set(words)
        positive_words = set(P)
        negative_words = (set(N))

        if len(positive_words.intersection(words)) > len(negative_words.intersection(words)):
           pcnt+= 1


        elif len(positive_words.intersection(words)) < len(negative_words.intersection(words)):
             ncnt+= 1
        else:
             neut_cnt+= 1
    print("Positive Words: ",pcnt)
    print("Negative Words : ",ncnt)
    print("Nuetral Words: ", neut_cnt)
def main():
    negative = "negativesentimentwords.txt"
    text = 'thehoundofthebaskervilles.txt'
    positive = "positivesentimentwords.txt"
    text_file(text,positive,negative)

main()
