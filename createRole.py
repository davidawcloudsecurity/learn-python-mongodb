import pymongo

# Connection URI for MongoDB running on localhost
uri = "mongodb://ambienceAdmin:123@localhost:27017/"

# Attributes for a new role
database = "admin"
rolename ="ambienceRole"
default = ["listDatabases", "dropCollection", "reIndex", "dropIndex", "createIndex", "createCollection", "listCollections", "listIndexes", "find", "update", "insert", "collMod", "collStats", "reIndex", "indexStats", "planCacheIndexFilter", "enableProfiler", "validate", "remove", "planCacheRead", "planCacheWrite", "bypassDocumentValidation", "enableProfiler", "storageDetails", "validate", "compact"]
timeout = 5000

try:
    # Connect to MongoDB
    client = pymongo.MongoClient(uri, serverSelectionTimeoutMS=timeout)

    # Access the admin database (you need administrative privileges to create a user)
    db = client[database]

    # Define the role privileges
    actions = [{
        "resource": {"db": database, "collection": ""},
        "actions": default
    }]

    db.command("createRole", rolename, privileges=actions, roles=[])
    print("Role '" + rolename + "' created successfully in '" + database + "'")
except pymongo.errors.OperationFailure as e:
    print(f"Error creating role: {e}")
except pymongo.errors.ConnectionFailure as e:
    print(f"Failed to connect to MongoDB: {e}")
