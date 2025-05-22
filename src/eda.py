import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def perform_eda(input_file: str):
    df = pd.read_csv(input_file)

    print("---- Dataset Info ----")
    print(df.info())
    print("\n---- Summary Statistics ----")
    print(df.describe())

    # Create folder to save plots if it doesn't exist
    reports_dir = os.path.join("..", "reports")
    os.makedirs(reports_dir, exist_ok=True)

    # Histogram of Price
    plt.figure(figsize=(8,5))
    sns.histplot(df['Price'], bins=30, kde=True)
    plt.title('Price Distribution')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(reports_dir, 'price_distribution.png'))
    plt.show()

    # Boxplot Price vs Total stops
    plt.figure(figsize=(8,5))
    sns.boxplot(x='Total_stops_num', y='Price', data=df)
    plt.title('Price vs Number of Stops')
    plt.savefig(os.path.join(reports_dir, 'price_vs_stops.png'))
    plt.show()

    # Scatter plot Duration vs Price
    plt.figure(figsize=(8,5))
    sns.scatterplot(x='Duration_min', y='Price', data=df)
    plt.title('Duration vs Price')
    plt.savefig(os.path.join(reports_dir, 'duration_vs_price.png'))
    plt.show()

if __name__ == "__main__":
    input_file = os.path.join("..", "data", "processed", "processed_flight_data.csv")
    perform_eda(input_file)
