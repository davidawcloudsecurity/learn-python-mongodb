import pymongo

# Connection URI for MongoDB running on localhost
uri = "mongodb://localhost:27017/"

# Credentials for the new user
username = "ambienceUser"
password = "your_password"
roles = ["readWrite"]  # Should be a list even if only one role is assigned

try:
    # Connect to MongoDB
    client = pymongo.MongoClient(uri)

    # Access the admin database (you need administrative privileges to create a user)
    admin_db = client.admin

    # Create the user
    admin_db.command('createUser', username, pwd=password, roles=roles)

    print(f"User '{username}' created successfully.")

except pymongo.errors.OperationFailure as e:
    print(f"Error creating user: {e}")
