
#load "neg_list" globally for better performance
neg_list = []
with open("negation_list") as file:
    for line in file:
        neg_list.append(line.rstrip('\n'))
file.close()



def get_senti_reversed_negation(tweet):
    """look up each lexicon and sum up the sentiment score
    """
    #negation detection window
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
        if tokens[i] in senti_vice.keys(): vice_score = vice_score + 1
        if tokens[i] in senti_virtue.keys(): virtue_score = virtue_score + 1
        if tokens[i] in senti_negative.keys():
            for j in range(max(0, i - window), i):
                if tokens[i] in neg_list: if_neg = if_neg * (-1)
            if(if_neg == 1):
                pos_score = pos_score + 1
            else:
                neg_score = neg_score + 1
        if tokens[i] in senti_positive.keys():
            for j in range(max(0, i - window), i):
                if tokens[i] in neg_list: if_neg = if_neg * (-1)
            if (if_neg == 1):
                neg_score = neg_score + 1
            else:
                pos_score = pos_score + 1

    tweet["vice_score"] = vice_score
    tweet["virtue_score"] = virtue_score
    tweet["pos_score"] = pos_score
    tweet["neg_score"] = neg_score

    return (tweet)


