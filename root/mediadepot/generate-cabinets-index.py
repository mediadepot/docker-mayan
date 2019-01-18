from mayan_api_client import API
import yaml
import io
import re

#log into mayan edms server
api = API(host='http://localhost', username='admin', password='WZHdJDcp5d')
print api._info

def get_cabinets_rec(current_page):

    resp = api.cabinets.cabinets.get(page=current_page)
    results = resp['results']
    if resp['next']:
        return results + get_cabinets_rec(current_page + 1)

    return results

def get_indexes_rec(current_page):
    resp = api.document_indexing.indexes.get(page=current_page)
    results = resp['results']
    if resp['next']:
        return results + get_cabinets_rec(current_page + 1)

    return results

def upsert_cabinet_index():
    # list all indexes
    indexes = get_indexes_rec(1)

    cabinet_index = next((index for index in indexes if index['label'] == 'Cabindets'), None)

    if not cabinet_index:
        print api.document_indexing.indexes.post({'enabled': 'true', 'label': 'Cabinedts', 'document_types': '1' })

    return cabinet_index



def main():

    # get all cabinets
    all_cabinets = get_cabinets_rec(1)

    # find the cabinet index (or create it if missing)
    cabinet_index = upsert_cabinet_index()



if __name__ == "__main__":
    main()