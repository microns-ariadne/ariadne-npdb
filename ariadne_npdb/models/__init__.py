import os

import ariadne_npdb


class Base(dict):
    def __init__(self, db=None, collection='phys'):
        self._db = db
        self.collection = collection
        self.model_name = self.__class__.__name__.lower()

    @property
    def db(self):
        return self._db or ariadne_npdb.DB

    @property
    def _root(self):
        return getattr(self.db, self.collection)

    @property
    def model(self):
        return getattr(self._root, self.model_name)

    def save(self, **kwargs):
        if not self.db:
            raise Exception('missing db connection - forget to connect?')
        self.model.insert(kwargs)

    def get_all_ids(self):
        return [i['id'] for i in self.model.find()]

    def find(self, *args, **kwargs):
        return self.model.find(*args, **kwargs)

    def find_one(self, *args, **kwargs):
        return self.model.find_one(*args, **kwargs)
