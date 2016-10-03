"""
These negations were collected by Jan from polanyi's chapter and Israel chapter
from The Handbook of Pragmatics 2004 Horn & Ward (eds).  But added to from training set.
@article{wilson2009recognizing,
  title={Recognizing contextual polarity: An exploration of features for phrase-level sentiment analysis},
  author={Wilson, Theresa and Wiebe, Janyce and Hoffmann, Paul},
  journal={Computational linguistics},
  volume={35},
  number={3},
  pages={399--433},
  year={2009},
  publisher={MIT Press}
"""


#load "neg_list" globally for better performance
neg_list = []
with open("valenceshifters.tff") as file:
    for line in file:
        neg_list.append(line.rstrip('\n'))
file.close()



def get_senti_reversed_negation(tweet):
    """look up each lexicon and sum up the sentiment score
    """
    #negation detection window size
    window = 2

    #load tokens
    tokens = tweet.get("tokens")

    #initialize scores
    vice_score = 0
    virtue_score = 0
    pos_score = 0
    neg_score = 0

    #negation switch
    if_neg = -1

    #if a negation in the range of "window", reverse "pos" and "neg"
    for i in range(0,len(tokens)):
        #if tokens[i] in senti_vice.keys(): vice_score = vice_score + 1
        #if tokens[i] in senti_virtue.keys(): virtue_score = virtue_score + 1
        if_neg = -1
        if tokens[i] in senti_negative.keys():
            for j in range(max(0, i - window), i):
                if tokens[j] in neg_list: if_neg = if_neg * (-1)
            if(if_neg == 1):
                pos_score = pos_score + 1
            else:
                neg_score = neg_score + 1
        if tokens[i] in senti_positive.keys():
            for j in range(max(0, i - window), i):
                if tokens[j] in neg_list: if_neg = if_neg * (-1)
            if (if_neg == 1):
                neg_score = neg_score + 1
            else:
                pos_score = pos_score + 1

    #tweet["vice_score"] = vice_score
    #tweet["virtue_score"] = virtue_score
    tweet["pos_score"] = pos_score
    tweet["neg_score"] = neg_score

    return (tweet)


