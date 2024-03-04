import pymongo

# Connection URI for MongoDB running on localhost
uri = "mongodb://localhost:27017/"

# Credentials for the new user
username = "ambienceUser"
password = "123"
default = ["read"]  # Should be a list even if only one role is assigned
databases_roles = {
    "ambience": ["ambienceRole"],
    "ambience-logs": ["ambienceRole"],
    "ambience-temp": ["ambienceRole"],
    "eno": ["ambienceRole"],
    "config": ["read"]
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
