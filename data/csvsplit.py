import pandas as pd

# Input CSV
in_csv = 'data/all/alltweets.csv'
df_in = pd.read_csv(in_csv)

# Get the number of lines (rows) of input CSV
number_lines = 0
for index, row in df_in.iterrows():
    number_lines += 1
print(f"Num of rows: {number_lines}")

# Size of rows of data to write to the csv
rowsize = 5000

# Loop variable to keep track of CSV numbers
j = 1

# Loop through data, create new CSV file for each set
for i in range(0, number_lines, rowsize):

    df_out = pd.read_csv(in_csv,
          nrows = rowsize,  # number of rows to read at each loop
          skiprows = i+1)     # skip rows that have been read

    # csv to write data to a new file with indexed name. input_1.csv etc.
    out_csv = 'data/subsets/alltweets_subset_' + str(j) + '.csv'

    df_out.to_csv(out_csv,
          index = False,
          header = True,
          mode = 'a',           # append data to csv file
          chunksize = rowsize)  # size of data to append for each loop

    j+=1
    print(f"CSV #{j}.")
print(f"Total amount of CSV files: {j}")
