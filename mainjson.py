import csv
import json
import re
import logging

input_file = "alltweets_filtered.csv"
output_file = "alltweets_filtered_keyword_relevant.json"

# Regular expressions for matching keywords related to virtual care
virtual_care_keywords = [
    "telemedicine", "telehealth", "remote healthcare",
    "virtual visits", "video visits", "digital health",
    "e-health", "virtual care", "virtual medicine",
    "virtual health", "telemonitoring", "teleconsultation",
    "virtual care", "virtual", "online"
    # please add more keywords based on topic extraction
]

# Regular expressions for matching keywords to exclude
exclude_keywords = [
    "dose", "vaccine"
]

# Prompt user for whether to exclude keywords or not
# response = input("Would you like to exclude any keywords? (y/n): ")
response = "n"
if response.lower() == "y":
    exclude_keywords.extend(virtual_care_keywords) # Add virtual care keywords to exclude list
    keywords = "|".join(exclude_keywords)
    exclude_pattern = re.compile(keywords, re.IGNORECASE)
else:
    exclude_pattern = None

# Compile a regular expression pattern for matching the keywords
virtual_care_pattern = re.compile("|".join(virtual_care_keywords), re.IGNORECASE)

with open(input_file, 'r', encoding='utf-8') as input_csv_file, \
        open(output_file, 'w', newline='', encoding='utf-8') as output_json_file:
        reader = csv.DictReader(input_csv_file)
        data = []
        i = 0
        for row in reader:
                tweet = row['rawContent']
                if (virtual_care_pattern.search(tweet)
                        and (not exclude_pattern or not exclude_pattern.search(tweet))):
                        data.append(row)
                i += 1        
                print(i)
        # print(data)
        # output_json_file.write(json.dumps(data, indent=4))
        json.dump(data, output_json_file, indent=4)
    