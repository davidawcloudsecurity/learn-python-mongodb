import pymongo

# Connection URI for MongoDB running on localhost
uri = "mongodb://localhost:27017/"

# Credentials for the new user
username = "ambienceUser"
password = "123"
roles = ["readWrite"]  # Should be a list even if only one role is assigned
database = "ambience"
rolename ="role-name10"
default = ["listDatabases", "dropCollection", "reIndex", "dropIndex", "createIndex", "createCollection", "listCollections", "listIndexes", "find", "update", "insert", "collMod", "collStats", "reIndex", "indexStats", "planCacheIndexFilter", "enableProfiler", "validate", "remove", "planCacheRead", "planCacheWrite", "bypassDocumentValidation", "enableProfiler", "storageDetails", "validate", "compact"]

try:
    # Connect to MongoDB
    client = pymongo.MongoClient(uri)

    # Access the admin database (you need administrative privileges to create a user)
    admin_db = client[database]

    # Define the role privileges
    privileges = [{
        "resource": {"db": database, "collection": ""},
        "actions": default
    }]

    admin_db.command("createRole", rolename, privileges=privileges, roles=[])
    print("Role '" + rolename + "' created successfully in '" + database + "'")
except pymongo.errors.OperationFailure as e:
    print(f"Error creating role: {e}")
