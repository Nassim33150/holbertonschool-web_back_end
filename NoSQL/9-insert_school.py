#!/usr/bin/env python3


"""  inserts a new document in a collection based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """  inserts a new document in a collection based on kwargs """
    document = {}
    for key, value in kwargs.items():
        document[key] = value
    result = mongo_collection.insert_one(document)
    document_id = result.inserted_id
    return document_id
