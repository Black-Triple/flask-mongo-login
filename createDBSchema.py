from server import mongo_db


def create_mongodb_schema():
    mongo_db.db.create_collection('users')
    mongo_db.db.create_collection('blacklist_tokens')
    mongo_db.db.blacklist_tokens.create_index("createdAt", expireAfterSeconds=86400)
