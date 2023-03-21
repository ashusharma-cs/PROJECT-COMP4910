import numpy as np
import pandas as pd
import re as re
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.interpolate import make_interp_spline

import spacy
nlp = spacy.load("en_core_web_lg")

df=pd.read_csv('phrase_based/alltweets_filtered_labelled.csv')

tweet_content=df['rawContent'].array
# labelled_tweets=df.loc[df.relVirtualCare>=0.5, ['rawContent']].to_numpy().reshape(-1)
# rel_score=df['relVirtualCare'].array

for i, text in enumerate(tweet_content):
  tweet_content[i] = re.sub(r'(@\w+|\bhttps?:\S+)\s*', '', text)

# for i, text in enumerate(labelled_tweets):
#   labelled_tweets[i] = re.sub(r'(@\w+|\bhttps?:\S+)\s*', '', text)

tweet_content.reshape(-1)
phrase="virtual care"
# threshold=[0,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5]
threshold=0.3

relevant_tweets=[]
irrelevant_tweets=[]
# scores = {}
i = 0
for tweet in tweet_content:
  doc1=nlp(tweet)
  doc2=nlp(phrase)
  similarity_score=doc1.similarity(doc2)
          
  if(similarity_score>=threshold):
    relevant_tweets.append(tweet)
    # scores[tweet] = "1"
    df.loc[i, 'candidate'] = '1'
  else:
    irrelevant_tweets.append(tweet)
    # scores[tweet] = "0"
    df.loc[i, 'candidate'] = '0'
  i += 1

df.to_csv('phrase_based/alltweets_filtered_labelled.csv', index=False)

# df = pd.DataFrame.from_dict(scores.items())
# df.columns = ['rawContent','phrase-based']
# df.to_csv('phrase_scores.csv')
# tweets={}
# for count,tweet in enumerate(tweet_content):
#   tweets[tweet]=rel_score[count]

# true_positive=0
# false_positive=0
# true_negative=0
# false_negative=0

# for tweet in tweet_content: 
#   if(tweet in relevant_tweets):
#     if(tweets[tweet]>=0.5):
#       true_positive+=1
#     else:
#       false_positive+=1 
#   else:
#     if(tweets[tweet]==0):
#       true_negative+=1
#     else:
#       false_negative+=1
          
            


