from pymongo import MongoClient
import pandas as pd
import time  # Import the time module

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["product_db"]
collection = db["products"]

# Correct file path
remaining_data_path = r"C:\Users\omar.bandeh\Documents\dataset\test_dataset.csv"

# Load the remaining 20% of the dataset
try:
    df = pd.read_csv(remaining_data_path)
    print(f"Dataset loaded successfully with {len(df)} records.")
except FileNotFoundError:
    print(f"File not found: {remaining_data_path}")
    exit()

# Convert data to a list of dictionaries
remaining_data = df.to_dict(orient="records")

# Measure the insertion time
start_time = time.time()  # Start the timer
try:
    result = collection.insert_many(remaining_data)
    end_time = time.time()  # End the timer

    # Calculate the duration
    duration = end_time - start_time
    print(f"Successfully inserted {len(result.inserted_ids)} documents into the collection.")
    print(f"Insertion time: {duration:.2f} seconds.")
except Exception as e:
    print(f"Error during insertion: {e}")


