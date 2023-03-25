import pandas as pd
import time
import openai
import csv

# ENTER API KEY
openai.api_key = ""

# Define a function to rate input message
def rate_message(message):
    try:
        # Use ChatGPT API to generate a response
        response = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=[ { "role": "user", "content": message }, { "role": "system", "content": "Rate if the message is related to virtual care from 0 (totally irrelevant) to 1 (totally relevant)." } ] )

        # Extract the score from the response
        score = response.choices[0].message.content
        return score
    except Exception as e:
        print(e)
        return e

# ENTER INPUT CSV
# read the CSV file into a pandas dataframe
df = pd.read_csv('all_tweets_subset.csv')
# encoding='cp1252'

t = time.time()
print('Time at start: ',time.ctime(t))

# ENTER OUTPUT CSV
# analyze each row and save results to output CSV file
with open('chatgpt_output.csv', 'w', newline='', encoding='utf-8') as output_file:
    writer = csv.writer(output_file)
    # writer.writerow(['date','likeCount', 'rawContent', 'AiOutput'])
    writer.writerow(['rawContent', 'GPTOutput'])
    for index, row in df.iterrows():
        text = row['rawContent']
        score = rate_message(text)
        writer.writerow([text, score])
        time.sleep(3)  # add a 3-second delay between requests, max 20 requests per min
        # print progress
        print(f"Processed rows {index+1}/{len(df)}")
        
print('Time at finish: ',time.ctime(t))
