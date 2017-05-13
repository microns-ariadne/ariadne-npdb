import pymongo


class Base(object):
    def __init__(self, db=None):
        self.db = db

    def connect(self, host, database, auth=None, port=27017, ssl=True):
        mc = pymongo.MongoClient(host, port=port, ssl=ssl)
        self.db = getattr(mc, database)
        if auth:
            self.db.authenticate(auth['username'], auth['password'])
