import pymongo

# Connection URI for MongoDB running on localhost
uri = "mongodb://localhost:27017/"

# Credentials for the new user
username = "ambienceBackup"
password = "123"

# Databases where backup and restore operations are allowed
databases = ["ambience"]

# Define custom roles for mongodump and mongorestore
mongodump_role = {
    "role": "mongodumpRole",
    "privileges": [
        {"resource": {"db": db, "collection": ""}, "actions": ["find", "listCollections"]}
        for db in databases
    ],
    "roles": []
}

mongorestore_role = {
    "role": "mongorestoreRole",
    "privileges": [
        {"resource": {"db": db, "collection": ""}, "actions": ["insert"]}
        for db in databases
    ],
    "roles": []
}

try:
    # Connect to MongoDB
    client = pymongo.MongoClient(uri)

    # Access the admin database (you need administrative privileges to create a user)
    db = client.ambience

    # Create custom roles
    db.command("createRole", mongodump_role)
    db.command("createRole", mongorestore_role)

    # Create the user with custom roles
    db.command("createUser", username, pwd=password, roles=["mongodumpRole", "mongorestoreRole"])

    print(f"User '{username}' created successfully with custom roles for mongodump and mongorestore.")

except pymongo.errors.OperationFailure as e:
    print(f"Error creating user or roles: {e}")
except pymongo.errors.ConnectionFailure as e:
    print(f"Failed to connect to MongoDB: {e}")
