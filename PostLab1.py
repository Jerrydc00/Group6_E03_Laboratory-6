from pymongo import MongoClient
import pprint
import re
from tabulate import tabulate
import sys

def format_customer_data(customer):
    return {k: v for k, v in customer.items() if not isinstance(v, dict)}

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    client = MongoClient("mongodb://localhost:27017/")
    db = client["chinook"]
    customers_collection = db["customers"]

print("\n=== First document in the customers collection ===")
    doc1 = customers_collection.find_one()
    formatted_doc = format_customer_data(doc1)
    print(tabulate([formatted_doc.values()], headers=formatted_doc.keys(), tablefmt='grid'))
    
    print("\n=== All documents in the customers collection ===")
    all_customers = []
    headers = None
    for doc in customers_collection.find():
        formatted_doc = format_customer_data(doc)
        if not headers:
            headers = formatted_doc.keys()
        all_customers.append(formatted_doc.values())
    print(tabulate(all_customers, headers=headers, tablefmt='grid'))print("\n=== First document in the customers collection ===")
    doc1 = customers_collection.find_one()
    formatted_doc = format_customer_data(doc1)
    print(tabulate([formatted_doc.values()], headers=formatted_doc.keys(), tablefmt='grid'))
    
    print("\n=== All documents in the customers collection ===")
    all_customers = []
    headers = None
    for doc in customers_collection.find():
        formatted_doc = format_customer_data(doc)
        if not headers:
            headers = formatted_doc.keys()
        all_customers.append(formatted_doc.values())
    print(tabulate(all_customers, headers=headers, tablefmt='grid'))
