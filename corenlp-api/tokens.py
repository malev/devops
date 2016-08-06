import os
import sys
import json
import requests
from pymongo import MongoClient

client = MongoClient()
db = client.corenlp

filename = sys.argv[1]
corenlp_url = os.environ.get('CORENLP_URL', 'localhost:8080')

print("Working with {}".format(filename))


def get_tokens(data):
    tokens = []
    r = requests.post(
        "http://{}/api/process".format(corenlp_url),
        data={'txt': data['parsedText'].encode('utf-8')}
    )
    payload = json.loads(r.text)
    for sentence in payload['document']['sentences']['sentence']:
        for token in sentence['tokens']['token']:
            if type(token) == dict:
                token['idTramite'] = data['idTramite']
                token['sentenceId'] = sentence['$']['id']
                token['tokenId'] = token['$']['id']
                del token['$']
                tokens.append(token)
    return tokens


def already_in_db(id_tramite):
    return db.tokens.find_one({'idTramite': id_tramite})


def store_tokens(tokens):
    for token in tokens:
        db.tokens.insert_one(token)


with open(filename) as dfile:
    for element in dfile:
        try:
            data = json.loads(element)
            if not already_in_db(data['idTramite']):
                print("Working on {}".format(data['idTramite']))
                store_tokens(get_tokens(data))
        except Exception, e:
            print("Error in {}. {}".format(data['idTramite'], e.message))
            continue

print("Done!")
