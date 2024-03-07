import pymongo

# Connection URI for MongoDB running on localhost
uri = "mongodb://localhost:27017/"

# List of database names to create
label = ""
database_names = [
    f"{label}ambience",
    f"{label}eno",
    f"{label}ambience-logs",
    f"{label}ambience-temp"
]

timeout = 5000

try:
    # Connect to MongoDB
    client = pymongo.MongoClient(uri, serverSelectionTimeoutMS=timeout)

    # Iterate over each database name and create it
    for db_name in database_names:
        db = client[db_name]
        # Create the database
        db.command("create", db_name)

        print(f"Database '{db_name}' created successfully.")

except pymongo.errors.ConnectionFailure as e:
    print(f"Failed to connect to MongoDB: {e}")
except pymongo.errors.OperationFailure as e:
    print(f"Error creating database: {e}")
