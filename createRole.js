var conn = new Mongo();

var db = conn.getDB("ambience");

// Edit on the right to change the username
let ambienceBackupSubject = "ambienceBackup";
let ambienceAdminSubject = "ambienceAdmin";
let ambienceUserSubject = "ambienceUser";

// Create the role in db: ambience
try {

db.createRole(
 {
   role: "ambienceRole",
   privileges: [
     {
       resource: { db: "ambience", collection: "" },
       actions: ["listDatabases", "dropCollection", "reIndex", "dropIndex", "createIndex", "createCollection", "listCollections", "listIndexes", "find", "update", "insert", "collMod", "collStats", "reIndex", "indexStats", "planCacheIndexFilter", "enableProfiler", "validate", "remove", "planCacheRead", "planCacheWrite", "bypassDocumentValidation", "enableProfiler", "storageDetails", "validate", "compact"]
     }
   ],
   roles: []
 });
 print("ambienceRole created in DB ambience successfully");
} catch (e) {
  print("Error creating ambienceRole in DB ambience:", e);
}

db = conn.getDB("eno");

try {

db.createRole(
 {
   role: "ambienceRole",
   privileges: [
     {
       resource: { db: "eno", collection: "" },
       actions: ["listDatabases", "dropCollection", "reIndex", "dropIndex", "createIndex", "createCollection", "listCollections", "listIndexes", "find", "update", "insert", "collMod", "collStats", "reIndex", "indexStats", "planCacheIndexFilter", "enableProfiler", "validate", "remove", "planCacheRead", "planCacheWrite", "bypassDocumentValidation", "enableProfiler", "storageDetails", "validate", "compact" ]
     }
   ],
   roles: []
 });
 print("ambienceRole created in DB eno successfully");
} catch (e) {
  print("Error creating ambienceRole in DB eno:", e);
}

db = conn.getDB("ambience-logs");

try {

db.createRole(
 {
   role: "ambienceRole",
   privileges: [
     {
       resource: { db: "ambience-logs", collection: "" },
       actions: ["listDatabases", "dropCollection", "reIndex", "dropIndex", "createIndex", "createCollection", "listCollections", "listIndexes", "find", "update", "insert", "collMod", "collStats", "reIndex", "indexStats", "planCacheIndexFilter", "enableProfiler", "validate", "remove", "planCacheRead", "planCacheWrite", "bypassDocumentValidation", "enableProfiler", "storageDetails", "validate", "compact" ]
     }
   ],
   roles: []
 });

 print("ambienceRole created in DB ambience-logs successfully");
} catch (e) {
  print("Error creating ambienceRole in DB ambience-logs:", e);
}

db = conn.getDB("ambience-temp");

try {

db.createRole(
 {
   role: "ambienceRole",
   privileges: [
     {
       resource: { db: "ambience-temp", collection: "" },
       actions: ["listDatabases", "dropCollection", "reIndex", "dropIndex", "createIndex", "createCollection", "listCollections", "listIndexes", "find", "update", "insert", "collMod", "collStats", "reIndex", "indexStats", "planCacheIndexFilter", "enableProfiler", "validate", "remove", "planCacheRead", "planCacheWrite", "bypassDocumentValidation", "enableProfiler", "storageDetails", "validate", "compact" ]
     }
   ],
   roles: []
 });

 print("ambienceRole created in DB ambience-temp successfully");
} catch (e) {
  print("Error creating ambienceRole in DB ambience-temp:", e);
}

db = conn.getDB("admin");

// Create the role in db: admin
try {
db.createRole(
 {
   role: "ambienceRole",
   privileges: [
     {
       resource: { db: "admin", collection: "" },
       actions: ["listDatabases", "dropCollection", "reIndex", "dropIndex", "createIndex", "createCollection", "listCollections", "listIndexes", "find", "update", "insert", "collMod", "collStats", "reIndex", "indexStats", "planCacheIndexFilter", "enableProfiler", "validate", "remove", "planCacheRead", "planCacheWrite", "bypassDocumentValidation", "enableProfiler", "storageDetails", "validate", "compact"]
     }
   ],
   roles: []
 });

 print("ambienceRole created in DB admin successfully");
} catch (e) {
  print("Error creating ambienceRole in DB admin:", e);
}

try {
  print(`Creating user: ${ambienceUserSubject}`)
db.createUser(
 {
   user: ambienceUserSubject,
   pwd:  passwordPrompt(),
   roles: [ { role: "ambienceRole", db: "admin" }, { role: "ambienceRole", db: "ambience" }, { role: "ambienceRole", db: "eno" }, { role: "ambienceRole", db: "ambience-logs" }, { role: "ambienceRole", db: "ambience-temp" },
            { role: "read", db: "config" } ]
 }
);
 print(`${ambienceUserSubject} created in DB admin, ambience, eno, ambience-logs, config successfully`);
} catch (e) {
  print(`Error creating ${ambienceUserSubject} in DB admin, ambience, eno, ambience-logs, config:`, e);
}

try {
  print(`Creating user: ${ambienceAdminSubject}`)
db.createUser(
 {
   user: ambienceAdminSubject,
   pwd:  passwordPrompt(),
   roles: [ { role: "dbOwner", db: "admin" }, { role: "dbOwner", db: "ambience" }, { role: "dbOwner", db: "eno" }, { role: "dbOwner", db: "config" }, { role: "dbOwner", db: "ambience-logs" }, { role: "dbOwner", db: "ambience-temp" } ]
//   roles: ["dbOwner"]

 }
);
 print(`${ambienceAdminSubject} created in DB admin successfully`);
} catch (e) {
  print(`Error creating ${ambienceAdminSubject} in DB admin:`, e);
}

try {
  print(`Creating user: ${ambienceBackupSubject}`);
db.createUser(
 {
   user: ambienceBackupSubject,
   pwd:  passwordPrompt(),
   roles: ["backup", "restore" ]
 }
);
  print(`${ambienceBackupSubject} created in DB admin successfully`);
} catch (e) {
  print(`Error creating ${ambienceBackupSubject} in DB admin:`, e);
}