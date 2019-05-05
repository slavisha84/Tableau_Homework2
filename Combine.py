# Import Dependencies
import os
import glob
import pandas as pd

# Initiate file directory path
os.chdir("C:/hw")
ext = 'csv'
all_files = [i for i in glob.glob('*.{}'.format(ext))]

# Combine all files in the all_files list
all_csv = pd.concat([pd.read_csv(f) for f in all_files])

# Export data to excel
all_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')