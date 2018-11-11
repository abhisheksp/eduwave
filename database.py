import json

from pymongo import MongoClient

with open('mongo.json') as f:
    data = json.load(f)
    uri = data['uri']
    port = int(data['port'])
    print('URI: ', uri)
    client = MongoClient(uri)
    db = client.test


def delete_collection():
    db.concentration.delete_many({})


def save_concentration(entry):
    db.concentration.insert_one(entry)


def find_data():
    results = db.concentration.find({})
    for document in results:
        print(document)


if __name__ == '__main__':
    find_data()
