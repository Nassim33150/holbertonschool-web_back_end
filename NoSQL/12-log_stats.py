#!/usr/bin/env python3
""" Import MongoClient """
from pymongo import MongoClient


def get_log_stats():
    """ provides some stats about Nginx logs stored in MongoDB: """
    client = MongoClient('mongodb://localhost:27017')
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {
        method: collection.count_documents({"method": method})
        for method in methods
    }

    status_check_count = collection.count_documents({"method": "GET",
                                                    "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    get_log_stats()
