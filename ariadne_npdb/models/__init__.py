import os

import pymongo


class Base(dict):
    def __init__(self, db=None, collection=None):
        self.db = db
        self.collection = collection or os.environ
        self.model_name = self.__class__.__name__.lower()

    @property
    def _root(self):
        return getattr(self.db, self.collection)

    @property
    def model(self):
        return getattr(self._root, self.model_name)

    def connect(self, host, database, auth=None, port=27017, ssl=True):
        mc = pymongo.MongoClient(host, port=port, ssl=ssl)
        self.db = getattr(mc, database)
        if auth:
            self.db.authenticate(auth['username'], auth['password'])

    def save(self, **kwargs):
        if not self.db:
            raise Exception('missing db connection - forget to connect?')
        self.model.insert(kwargs)

    def get_all_ids(self):
        return [i['id'] for i in self.model.find()]
