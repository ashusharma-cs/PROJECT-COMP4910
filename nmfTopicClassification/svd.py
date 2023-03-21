import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

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

# Apply SVD to the vectorized tweets
n_components = 250
svd_model = TruncatedSVD(n_components=n_components, algorithm='randomized', random_state=1)
svd_model.fit(vectorized_tweets)

# Print the top words in each topic
feature_names = vectorizer.get_feature_names_out()
for topic_idx, topic in enumerate(svd_model.components_):
    print("Topic #%d:" % (topic_idx + 1))
    print(", ".join([feature_names[i] for i in topic.argsort()[:-5 - 1:-1]]))
    print()

# Let user choose a topic
selected_topic = int(input("Enter the topic number you want to label (1-250): "))
selected_topic_words = [feature_names[i] for i in svd_model.components_[selected_topic - 1].argsort()[:-5 - 1:-1]]
print(f"Selected topic words: {', '.join(selected_topic_words)}")

# Label entries in the "svd" column with a value of 1 if they match the selected topic and the "relVirtualCare" column is not empty
for i in range(len(tweets_df)):
    if not pd.isna(tweets_df.at[i, 'relVirtualCare']):
        tweet_text = tweets_df.at[i, 'rawContent']
        if any(topic_word in tweet_text for topic_word in selected_topic_words) and svd_model.transform(vectorizer.transform([tweet_text]))[0][selected_topic - 1] > 0.0:
            tweets_df.at[i, 'svd'] = 1
        else:
            tweets_df.at[i, 'svd'] = 0

# Save the modified DataFrame to a new CSV file
tweets_df.to_csv('alltweets_filtered_labelled.csv', index=False)
