import pymongo

# Connection URI for MongoDB running on localhost
uri = "mongodb://localhost:27017/"

try:
    # Connect to MongoDB
    client = pymongo.MongoClient(uri)

    # Check if the connection was successful
    if client is not None:
        print("Connected successfully to MongoDB")

    # List the available databases
    print("Available databases:")
    print(client.list_database_names())

except pymongo.errors.ConnectionFailure:
    print("Could not connect to MongoDB")
