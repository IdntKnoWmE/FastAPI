import pymongo

MONGO_DB = {
    "name": "notes-fastapi",
    "uri": "mongodb://localhost:2717/"
}

# Connect to MongoDB using a mongo client
client = pymongo.MongoClient(MONGO_DB.get("uri"))

# Connect to a database of mongo
mydb_conn = client[MONGO_DB.get("name")]  # Here, notes-fastapi is the DB name
# print(client.list_database_names())
