from elasticsearch_dsl import Index, Document, Text, Keyword, analyzer, tokenizer
from elasticsearch_dsl.connections import connections
import pandas as pd
from nltk import word_tokenize


text_analyzer = analyzer("text_analyzer", tokenizer="classic", filter=["lowercase","stop"])

class TextDocument(Document):
    text = Text(analyzer=text_analyzer)


def check_and_create_index(es, DOMAIN, index_name, data):
    '''Check if index exists, if not, create it'''
    hosts = []
    hosts.append(DOMAIN)
    connections.create_connection(hosts=hosts)
    if not es.indices.exists(index_name):
        yelp_index = Index("yelp_reviews")
        yelp_index.document(TextDocument)
        yelp_index.create()
        for index, row in data.iterrows():
            text = row["Review"]
            doc = TextDocument(text=text)
            doc.meta.id = index
            doc.save()
        return yelp_index
    else:
        return Index(index_name)

def elastic_search(index_object, data, query: str):
    indexes = []
    query = word_tokenize(query)
    s = index_object.search()
    #build an empty query
    s = s.query()
    #return all the texts up to 500
    s = s[:500]
    #loop through the query_string to add to query in s
    update = {'query': {'bool': {'should': []}}}
    for word in query:
        update["query"]["bool"]["should"].append({"match": {"text": word}})
    s.update_from_dict(update)
    responses = s.execute()
    #add the indexes and return the corresponding rows in dataframe
    for response in responses:
        indexes.append(int(response.meta.id))
    return data.filter(items=indexes, axis=0)
