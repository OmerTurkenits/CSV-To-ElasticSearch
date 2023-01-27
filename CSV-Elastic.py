# Import tools from the elasticsearch API.
from elasticsearch import Elasticsearch, helpers
import csv

# Connect to the elastic search port
es = Elasticsearch(hosts=[{'host': '127.0.0.1', 'port': 9200, 'scheme': 'http'}])

# Read from the csv file and convert it to elasticsearch documents
with open("C:\\Users\\Asus\\Desktop\\flight_data.csv") as file:
    reader = csv.DictReader(file)
    helpers.bulk(es, reader, index='flight_data')

