#!/usr/bin/env python3

from datetime import datetime
from elasticsearch import Elasticsearch
import time

es = Elasticsearch("http://elasticsearch:9200")
while True:
    print("Waiting for elastic search...")
    if es.ping():
        print("Connected!")
        break
    time.sleep(1)

body = {
    'test': "test",
    'timestamp': datetime.now(),
}
print(es.index(index="test", doc_type='default', body=body))
