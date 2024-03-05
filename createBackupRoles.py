import pymongo

# Connection URI for MongoDB running on localhost
uri = "mongodb://localhost:27017/"

# Attributes for a new role
label = ""
databases = [f"{label}eno", f"{label}ambience", f"{label}ambience-logs", f"{label}ambience-temp"]
rolename ="backup"
default = [
    "listDatabases",
    "listCollections",
    "listIndexes",
    "find",
    "collStats",
    "indexStats",
    "planCacheIndexFilter",
    "planCacheRead",
    "planCacheWrite",
    "storageDetails",
    "validate"
]
timeout = 5000

try:
    # Connect to MongoDB
    client = pymongo.MongoClient(uri, serverSelectionTimeoutMS=timeout)

    for database in databases:
        # Access the database
        db = client[database]

        # Define the role privileges
        actions = [{
            "resource": {"db": database, "collection": ""},
            "actions": default
        }]
        try:
            db.command("createRole", rolename, privileges=actions, roles=[])
            print(f"Role '{rolename}' created successfully in '{database}'")
        except pymongo.errors.OperationFailure as e:
            if "already exists" in str(e):
                print(f"Role '{rolename}' already exists in '{database}'")
            else:
                print(f"Error creating role: {e}")    
except pymongo.errors.ConnectionFailure as e:
    print(f"Failed to connect to MongoDB: {e}")
