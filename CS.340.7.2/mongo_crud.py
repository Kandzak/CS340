import pymongo

class MongoCRUD:
    def __init__(self, database_name, collection_name):
        self.client = pymongo.MongoClient(f"mongodb://aacuser:SNHU1234@localhost:32642/{database_name}")
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def retrieve_all(self):
        return list(self.collection.find({}))
# Create an instance of the MongoCRUD class for the specific database and collection
db_interface = MongoCRUD("grazioso_salvare_db", "austin_animal_outcomes")

# Retrieve all records from the database collection
all_data = db_interface.retrieve_all()

    # Additional CRUD methods here
