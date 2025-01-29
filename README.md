# Local Database Optimization

## **Project Overview**

This project focuses on optimizing query performance in a MongoDB database under constrained environments. The goal is to explore techniques such as indexing, schema optimization, query adjustments, and replication to improve database performance while maintaining resource efficiency.

## **Features**

- **Dataset Import**: Load an 80% training dataset into MongoDB.
- **High-Speed Operations**: Measure insertion and query performance with a 20% testing dataset.
- **Optimizations**:
  - Indexing (single-field and compound).
  - Schema adjustments to reduce document size.
  - Query optimizations to limit unnecessary fields.
  - Replication for distributing read operations.
- **Performance Analysis**: Compare query times before and after applying optimizations.

## **Project Structure**

```
local-database-optimization/
├── datasets/
│   ├── main_dataset.csv         # 80% training data
│   ├── test_dataset.csv         # 20% testing data
├── scripts/
│   ├── import_main_dataset.py   # Imports main dataset into MongoDB
│   ├── high_speed_input.py      # Measures insertion performance
│   ├── high_speed_output.py     # Measures query performance
│   ├── indexing_script.py       # Adds indexes to improve query time
│   ├── schema_optimization_script.py # Demonstrates schema adjustments
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
```

## **Setup Instructions**

### **1. Prerequisites**

- Install [MongoDB](https://www.mongodb.com/docs/manual/installation/).
- Install Docker
- Install Python 3.12 or higher.
- Install required Python libraries such as pandas, pymongo:
  ```bash
  pip install -r requirements.txt
  ```

### **2. MongoDB Setup**

1. Start your MongoDB server:
   ```bash
   mongod
   ```
2. Create a database called `product_db`.

### **3. Import the Dataset**

1. Run the script to import the main dataset:
   ```bash
   python scripts/import_main_dataset.py
   ```
2. Verify the imported data:
   ```bash
   mongosh
   use product_db
   db.products.find().limit(5)
   ```

### **4. Test High-Speed Operations**

1. Measure insertion time for the 20% dataset:
   ```bash
   python scripts/high_speed_input.py
   ```
2. Measure query performance:
   ```bash
   python scripts/high_speed_query.py
   ```

### **5. Install Docker**

          Install and run MongoDB image with 512 RAM size and 1 CPU core:

             docker run -d --name mongodb --memory=512m --cpus=1 -p 27018:27017 mongo

### **6. Run High Speed query in docker Container:**

   Test the query time in a constrained environment using the high_speed_query script.


### **7. Apply Optimizations**

- Add Indexes through script below or MongoDB Compass GUI:

  ```bash
  python scripts/indexing_script.py
  ```

- Adjust Schema:

  - Remove datasets fields that are not necessary. You can manually delete the fields or use the script;
    ```bash
      python scripts/schema_optimization_script.py
    ```

Query Optimization: 

   - Modify the query to limit the returned fields
        results = list(collection.find(query, {"\_id": 0, "Product ID": 1, "Product Name": 1}).limit(10))

Replication(optional): 
Replication ensures data redundancy and improves read performance by distributing queries across multiple nodes. 
Follow these steps to set up a replica set in MongoDB:
    
    Start MongoDB with Replication Enabled:
        mongod --replSet rs0 --bind_ip localhost

Initiate the Replica Set:
        mongosh
        rs.initiate()

Add Secondary Nodes (if applicable):
        rs.add("localhost:27018")

Check the Replica Set Status:
        rs.status()

Modify the Query Script to Read from Secondaries:
        client = MongoClient("mongodb://localhost:27017,localhost:27018/?replicaSet=rs0&readPreference=secondary")

Measure Query Performance:
        Run the high-speed query script and compare performance before and after replication.
    

## **Results**

| **Condition**             | **Query Time (s)** |
| ------------------------- | ------------------ |
| Unconstrained Environment | 13.70              |
| Constrained Environment   | 60.62              |
| Add Indexes               | 27.44              |
| Schema Optimization       | 23.81              |
| Optimized Query           | 17.86              |
| Replication               | 25.66              |

## **Future Optimizations**

- **Sharding**: Distribute data across multiple nodes for horizontal scaling.

- **Monitoring**: Leverage tools like `mongostat` and `mongotop` for performance tracking.

## **Repository Access**

- URL: [GitHub Repository Link](https://github.com/obandeh/local-database-optimization)


## **License**

This project is licensed under the MIT License. See the LICENSE file for more details.

