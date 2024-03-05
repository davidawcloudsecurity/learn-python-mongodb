import pymongo

# Connection URI for MongoDB running on localhost
uri = "mongodb://localhost:27017/"

# Attributes for new roles
label = ""
databases = [f"{label}eno", f"{label}ambience", f"{label}ambience-logs", f"{label}ambience-temp"]
roles_privileges = {
    "restore": [{"actions": ["insert"], "databases": databases}],
    "backup": [{"actions": ["find", "listCollections"], "databases": databases}]
}
timeout = 5000

try:
    # Connect to MongoDB
    client = pymongo.MongoClient(uri, serverSelectionTimeoutMS=timeout)

    for rolename, privileges in roles_privileges.items():
        for privilege in privileges:
            for database in privilege["databases"]:
                # Access the database
                db = client[database]

                # Define the role privileges
                actions = [{
                    "resource": {"db": database, "collection": ""},
                    "actions": privilege["actions"]
                }]
                try:
                    db.command("createRole", rolename, privileges=actions, roles=[])
                    print(f"Role '{rolename}' created successfully in '{database}'")
                except pymongo.errors.OperationFailure as e:
                    if "already exists" in str(e):
                        print(f"Role '{rolename}' already exists in '{database}'")
                    else:
                        print(f"Error creating role: {e}")    
except pymongo.errors.ConnectionFailure as e:
    print(f"Failed to connect to MongoDB: {e}")
