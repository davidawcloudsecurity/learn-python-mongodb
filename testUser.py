import getpass
import pymongo

# Connection URI for MongoDB running on localhost
uri = "mongodb://root:123@localhost:27017/"

# Credentials for the new user
username = "ambienceUser6"
password = getpass.getpass(prompt="Enter password: ")

# Roles for the new user
roles = [
    {"role": "ambienceRole", "db": "ambience"},
    {"role": "ambienceRole", "db": "eno"},
    {"role": "ambienceRole", "db": "ambience-logs"},
    {"role": "ambienceRole", "db": "ambience-temp"},
    {"role": "read", "db": "config"}
]

try:
    # Connect to MongoDB
    client = pymongo.MongoClient(uri)

    # Access the admin database (you need administrative privileges to create a user)
    db_admin = client.admin

    # Create the user with the specified roles
    db_admin.command('createUser', username, pwd=password, roles=roles)

    print(f"User '{username}' created successfully with roles: {roles}")

except pymongo.errors.OperationFailure as e:
    print(f"Error creating user: {e}")

except pymongo.errors.ConnectionFailure as e:
    print(f"Failed to connect to MongoDB: {e}")
