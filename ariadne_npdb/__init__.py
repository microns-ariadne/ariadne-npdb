import pymongo


DB = None


def connect(host, database, auth=None, port=27017, ssl=True):
    mc = pymongo.MongoClient(host, port=port, ssl=ssl)
    db = getattr(mc, database)
    if auth:
        db.authenticate(auth['username'], auth['password'])
    globals()['DB'] = db
