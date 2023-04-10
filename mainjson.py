import csv
import json

csvFilePath = 'data.csv'
jsonFilePath = 'relevant_tweets.json'

data = {}

# Read CSV file and create a dictionary
with open(csvFilePath, encoding='utf-8') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        key = rows['key'] # Change 'key' to the column name that contains the unique key for each row
        data[key] = rows

# Write dictionary to JSON file
with open(jsonFilePath, 'w', encoding='utf-8') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))