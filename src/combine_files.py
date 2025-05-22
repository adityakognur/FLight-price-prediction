import pandas as pd
import os

input_folder = '../data/raw/'  # Adjust path as needed
output_file = '../data/processed/combined_cleaned_data.csv'

# List all your 12 filenames explicitly or use glob for all CSVs in folder
files = [
    'NYC_PAR.csv', 'NYC_RUH.csv', 'NYC_SVO.csv',
    'PAR_NYC.csv', 'PAR_RUH.csv', 'PAR_SVO.csv',
    'RUH_NYC.csv', 'RUH_PAR.csv', 'RUH_SVO.csv',
    'SVO_NYC.csv', 'SVO_PAR.csv', 'SVO_RUH.csv'
]

# Initialize an empty DataFrame
combined_df = pd.DataFrame()

for file in files:
    file_path = os.path.join(input_folder, file)
    df = pd.read_csv(file_path)
    combined_df = pd.concat([combined_df, df], ignore_index=True)

# Save combined file
combined_df.to_csv(output_file, index=False)
print(f"Combined {len(files)} files with total rows: {len(combined_df)}")
