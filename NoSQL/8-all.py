#!/usr/bin/env python3


""" function that lists all documents in a collection """
def list_all(mongo_collection):
    """ function that lists all documents in a collection """
    empty_docs = []
    if mongo_collection is not None:
        return (mongo_collection.find())
    else:
        return empty_docs
