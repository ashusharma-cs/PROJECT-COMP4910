import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

# Load data from CSV file into a Pandas DataFrame
tweets_df = pd.read_csv('alltweets_filtered_labelled.csv')

# Define a function to preprocess the tweet text
def preprocess(text):
    # Remove URLs, user mentions, and non-alphanumeric characters
    text = re.sub(r"http\S+|@\S+|[^A-Za-z0-9 ]+", "", text)
    return text

# Apply the preprocess function to each tweet in the DataFrame
tweets_df['preprocessed'] = tweets_df['rawContent'].apply(preprocess)

# Vectorize the tweets using TfidfVectorizer
vectorizer = TfidfVectorizer(max_df=0.95, min_df=1, stop_words='english', ngram_range=(1, 1))
vectorized_tweets = vectorizer.fit_transform(tweets_df['preprocessed'])

# Extract topics using NMF
n_topics = 250
topic_model = NMF(n_components=n_topics, random_state=1, l1_ratio=0.5)
topic_model.fit(vectorized_tweets)

# Print the top words in each topic
feature_names = vectorizer.get_feature_names_out()
for topic_idx, topic in enumerate(topic_model.components_):
    print("Topic #%d:" % (topic_idx + 1))
    print(", ".join([feature_names[i] for i in topic.argsort()[:-5 - 1:-1]]))
    print()

# Let user choose a topic
selected_topic = int(input("Enter the topic number you want to label (1-250): "))
selected_topic_words = [feature_names[i] for i in topic_model.components_[selected_topic - 1].argsort()[:-5 - 1:-1]]
print(f"Selected topic words: {', '.join(selected_topic_words)}")

# Label entries in the "nmf" column with a value of 1 if they match the selected topic and the "relVirtualCare" column is not empty
for i in range(len(tweets_df)):
    if not pd.isna(tweets_df.at[i, 'relVirtualCare']):
        tweet_text = tweets_df.at[i, 'rawContent']
        if any(topic_word in tweet_text for topic_word in selected_topic_words) and topic_model.transform(vectorizer.transform([tweet_text]))[0][selected_topic - 1] > 0.0:
            tweets_df.at[i, 'nmf'] = 1
        else:
            tweets_df.at[i, 'nmf'] = 0

# Save the modified DataFrame to a new CSV file
tweets_df.to_csv('alltweets_filtered_labelled.csv', index=False)