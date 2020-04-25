from server import mongo_db


def check_blacklist_token(token):
    blacklist_tokens = mongo_db.db.blacklist_tokens
    resp = blacklist_tokens.find_one({'token': token})
    if resp:
        return True
    else:
        return False
