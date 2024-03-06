import pymongo

# Connection URI for MongoDB running on localhost
uri = "mongodb://root:123@localhost:27017/"

# Credentials for the new user
username = "ambienceUser9"
password = "123"
defaultRole = "ambienceRole"
default = ["read"]  # Should be a list even if only one role is assigned
label = ""
databases_roles = {
    f"{label}admin": ["read"],
    f"{label}ambience": [defaultRole],
    f"{label}ambience-logs": [defaultRole],
    f"{label}ambience-temp": [defaultRole],
    f"{label}eno": [defaultRole],
#    "config": ["read"] Is this needed?
}
timeout = 5000

try:
    # Connect to MongoDB
    client = pymongo.MongoClient(uri, serverSelectionTimeoutMS=timeout)

    # Create the user with roles in multiple databases
    for database, roles in databases_roles.items():

        # Access the admin database (you need administrative privileges to create a user)
        db = client[database]
        
        try: 
            db.command('createUser', username, pwd=password, roles=roles)
            print(f"User '{username}' created successfully with roles: '{roles}' in database '{database}'")
        except pymongo.errors.OperationFailure as e:
            print(f"Error creating user: {e}")
except pymongo.errors.ConnectionFailure as e:
    print(f"Failed to connect to MongoDB: {e}")
