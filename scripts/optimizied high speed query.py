from pymongo import MongoClient
import time

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27018/")
db = client["product_db"]
collection = db["products"]

# Simulate high-speed read operations
start_time = time.time()

# Perform 100000 queries
for _ in range(10000):
    query = {"Category": "Apparel"}  # Query all documents where Category = Apparel
    results = list(collection.find(query, {"Product Name": 1, "Price": 1}).limit(10))

  # Retrieve 100 results at a time

end_time = time.time()
print(f"Performed 10000 queries in {end_time - start_time:.2f} seconds.")

