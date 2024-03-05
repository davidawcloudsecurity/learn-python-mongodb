import pymongo

# Connection URI for MongoDB running on localhost
uri = "mongodb://localhost:27017/"

# Credentials for the new user
label = "" # This will append label to username and database (e.g label = 2_, database = 2_ambience, username = 2_ambienceAdmin)
username = "ambienceBackup"
password = "123"
databases_roles = {
    f"{label}ambience": ["backup", "restore"],
    f"{label}ambience-logs": ["backup", "restore"],
    f"{label}eno": ["backup", "restore"]
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
            db.command('createUser', f"{label}{username}", pwd=password, roles=roles)
            print(f"User '{label}{username}' created successfully with roles: '{roles}' in database '{database}'")
        except pymongo.errors.OperationFailure as e:
            print(f"Error creating user: {e}")
except pymongo.errors.ConnectionFailure as e:
    print(f"Failed to connect to MongoDB: {e}")
