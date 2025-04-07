import pandas as pd
import glob
import os

def combine_csv_files(directory, output_filename="combined_data.csv"):
    """
    Combines all CSV files in a directory into a single CSV file.

    Args:a
        directory (str): The path to the directory containing the CSV files.
        output_filename (str, optional): The name of the output CSV file. 
            Defaults to "combined_data.csv".
    """
    all_files = glob.glob(os.path.join(directory, "*.csv"))

    all_df = []
    for f in all_files:
        df = pd.read_csv(f)
        file_name = os.path.basename(f)
        df['fileName'] = file_name
        all_df.append(df)

    combined_df = pd.concat(all_df, ignore_index=True)

    combined_df.to_csv(output_filename, index=False)
    print(f"Combined data saved to {output_filename}")

# Example usage:
directory_path = "C:/Users/igoej/Downloads/takeout-20250406T123433Z-001/Takeout/Fit/Daily activity metrics"  # Replace with the actual path
combine_csv_files(directory_path)