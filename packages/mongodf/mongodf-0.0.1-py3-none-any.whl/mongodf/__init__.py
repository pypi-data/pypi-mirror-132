__version__ = "0.0.1"

from .column import Column
from .filter import Filter
from .dataframe import DataFrame


def from_mongo(mongo, database, collection):

    _db = mongo.get_database(database)
    _coll = _db.get_collection(collection)

    # compute the colums of the data
    _columns = list(_coll.aggregate([
        {"$project": {
            "data": {"$objectToArray": "$$ROOT"}
        }},
        {"$project": {"data": "$data.k"}},
        {"$unwind": "$data"},
        {"$group": {
            "_id": None,
            "keys": {"$addToSet": "$data"}
        }}
    ]))[0]["keys"]

    mf = DataFrame(mongo, _db, _coll, _columns)
    mf._filter = Filter(mf, {})
    return mf
