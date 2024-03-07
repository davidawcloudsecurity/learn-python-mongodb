import getpass
import pymongo

# Connection URI for MongoDB running on localhost
uri = "mongodb://root:123@localhost:27017/"

# Credentials for the new user
username = input("Enter the username: ")
password = getpass.getpass(prompt="Enter password: ")
database = "ambience"
roleName = "ambienceRole"
label = ""

# Roles for the new user
roles = [
    {"role": f"{roleName}", "db": f"{label}ambience"},
    {"role": f"{roleName}", "db": f"{label}eno"},
    {"role": f"{roleName}", "db": f"{label}ambience-logs"},
    {"role": f"{roleName}", "db": f"{label}ambience-temp"}
#    {"role": "read", "db": "config"}
]

try:
    # Connect to MongoDB
    client = pymongo.MongoClient(uri)

    # Access the admin database (you need administrative privileges to create a user)
    db = client[database]

    # Create the user with the specified roles
    db.command('createUser', username, pwd=password, roles=roles)

    print(f"User '{username}' created successfully with roles: {roles}")

except pymongo.errors.OperationFailure as e:
    print(f"Error creating user: {e}")

except pymongo.errors.ConnectionFailure as e:
    print(f"Failed to connect to MongoDB: {e}")
