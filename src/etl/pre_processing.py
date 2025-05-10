import pandas as pd
import os

def preprocess_data(input_path='data.csv', output_path='data_nextday.csv'):
    # Load data
    df = pd.read_csv(input_path)

    # Shift demand column
    df['demand_next_day'] = df['demand'].shift(-24)

    # Drop NaN rows (last 24 rows)
    df = df.dropna(subset=['demand_next_day'])

    # Save processed data
    df.to_csv(output_path, index=False)
    print(f"[✔] Preprocessed data saved to '{output_path}'")

if __name__ == "__main__":
    preprocess_data()

