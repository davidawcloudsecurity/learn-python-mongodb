import pymongo

# Connection URI for MongoDB running on localhost
uri = "mongodb://localhost:27017/"

# Credentials for the new user
username = "ambienceUser"
password = "123"
default = ["ambienceRole"]  # Should be a list even if only one role is assigned
database = ""
timeout = 5000

try:
    # Connect to MongoDB
    client = pymongo.MongoClient(uri, serverSelectionTimeoutMS=timeout)

    # Access the admin database (you need administrative privileges to create a user)
    db = client[database]

    # Create the user
    db.command('createUser', username, pwd=password, roles=default)

    print(f"User '{username}' created successfully with role: '{default}' in '{database}'")

except pymongo.errors.OperationFailure as e:
    print(f"Error creating user: {e}")
except pymongo.errors.ConnectionFailure as e:
    print(f"Failed to connect to MongoDB: {e}")
