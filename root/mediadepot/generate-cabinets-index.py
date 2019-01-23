import requests
import yaml
import io
import re


username = 'admin'
password = 'jG22sCfbcd'
api_base = 'http://mayan-edms:8000/api'

r = requests.get('{0}/documents'.format(api_base), auth=(username, password))
r.raise_for_status()
print r.json()

def get_cabinets_rec(current_page):

    r = requests.get('{0}/cabinets'.format(api_base), params={'page':current_page}, auth=(username, password))
    r.raise_for_status()

    resp = r.json()
    results = resp['results']
    if resp['next']:
        return results + get_cabinets_rec(current_page + 1)

    return results

def get_indexes_rec(current_page):

    r = requests.get('{0}/indexes'.format(api_base), params={'page':current_page}, auth=(username, password))
    r.raise_for_status()

    resp = r.json()

    results = resp['results']
    if resp['next']:
        return results + get_cabinets_rec(current_page + 1)

    return results

def upsert_cabinet_index():
    # list all indexes
    indexes = get_indexes_rec(1)

    cabinet_index = next((index for index in indexes if index['label'] == 'Cabinets'), None)

    if not cabinet_index:

        r = requests.post('{0}/indexes'.format(api_base), data={'enabled': 'true', 'label': 'Cabinets', 'document_types': [1]}, auth=(username, password))
        r.raise_for_status()
        print r.json()
        cabinet_index = r.json()['id']

    return cabinet_index



def main():

    # get all cabinets
    all_cabinets = get_cabinets_rec(1)

    # find the cabinet index (or create it if missing)
    cabinet_index = upsert_cabinet_index()



if __name__ == "__main__":
    main()