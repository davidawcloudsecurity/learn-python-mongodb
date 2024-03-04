import pymongo

# Connection URI for MongoDB running on localhost
uri = "mongodb://localhost:27017/"

# Credentials for the new user
username = "ambienceUser2"
password = "your_password"
default = ["read"]  # Should be a list even if only one role is assigned
database = "admin"


try:
    # Connect to MongoDB
    client = pymongo.MongoClient(uri)

    # Access the admin database (you need administrative privileges to create a user)
    db = client[database]

    # Create the user
    db.command('createUser', username, pwd=password, roles=default)

    print(f"User '{username}' created successfully with role: '{default}'")

except pymongo.errors.OperationFailure as e:
    print(f"Error creating user: {e}")