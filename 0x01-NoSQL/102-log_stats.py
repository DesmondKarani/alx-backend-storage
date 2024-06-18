#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB:

Database: logs
Collection: nginx
Display:
- Number of logs
- Number of logs by method
- Number of logs by status check
- Top 10 IPs
"""
from pymongo import MongoClient


def log_stats():
    """
    Provides statistics about Nginx logs in MongoDB.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Number of logs by method
    pipeline = [
        {"$group": {"_id": "$method", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]
    methods = collection.aggregate(pipeline)
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method['_id']}: {method['count']}")

    # Number of logs by status check
    pipeline = [
        {"$group": {"_id": "$path", "count": {"$sum": 1}}},
        {"$match": {"_id": "/status"}},
        {"$project": {"count": 1, "_id": 0}}
    ]
    status_checks = list(collection.aggregate(pipeline))
    print(f"{status_checks[0]['count']} status check")

    # Top 10 IPs
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = collection.aggregate(pipeline)
    print("IPs:")
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    log_stats()
