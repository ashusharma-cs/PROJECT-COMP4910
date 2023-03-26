import pandas as pd
import time
import openai
import csv

# ENTER API KEY
openai.api_key = ""

# EDIT PROMPT
# Define a function to rate input message
def rate_message(message):
    try:
        # Use ChatGPT API to generate a response
        response = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=[ { "role": "user", "content": message }, { "role": "system", "content": "ENTER PROMPT HERE. Example: Rate if the message is related to virtual care from 0 (totally irrelevant) to 1 (totally relevant)." } ] )

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
    writer.writerow(['rawContent', 'relVirtualCare', 'GPTOutput'])
    # writer.writerow(['rawContent', 'relVirtualCare', 'GPTScore', 'GPTOutput'])
    for index, row in df.iterrows():
        text = row['rawContent']
        relVirtualCare = int(row['relVirtualCare'])
        
        # If you ask in your prompt for ChatGPT to include a number score (0, 1, 0.5, etc)
        # And ask it to format the response so that the score is always included first
        
        # Create GPTScore row -> writer.writerow(['rawContent', 'relVirtualCare', 'GPTScore', 'GPTOutput'])
        # Extract it with gptscore
        # gptscore = int(re.findall(r'^\d+', gptoutput)[0])
        # Output to CSV -> writer.writerow([text, relVirtualCare, gptscore, gptoutput])
        
        gptoutput = rate_message(text)
        writer.writerow([text, relVirtualCare, gptoutput])
        # writer.writerow([text, relVirtualCare, gptscore, gptoutput])
        
        time.sleep(3)  # add a 3-second delay between requests, max 20 requests per min
        print(f"Processed rows {index+1}/{len(df)}")
        
print('Time at finish: ',time.ctime(t))
