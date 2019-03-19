import yaml
import io
import re
import requests
import os


username = 'admin'
password = 'jG22sCfbcd'
api_base = 'http://mayan-edms:8000/api'

r = requests.get('{0}/documents'.format(api_base), auth=(username, password))
r.raise_for_status()
print r.json()

def create_cabinet_rec(cabinet, parent_cabinet_id):
    cabinet_label = cabinet['label']
    #cabinet_id = re.sub('[^A-Za-z0-9]+', '_', cabinet_label.lower())

    cabinet_create_response = None
    if parent_cabinet_id:
        print "creating {0} with parent: {1}".format(cabinet_label, parent_cabinet_id)
        r = requests.post('{0}/cabinets/'.format(api_base), data={'label': cabinet_label, 'parent': parent_cabinet_id}, auth=(username, password))
        r.raise_for_status()
        cabinet_create_response = r.json()

    else:
        print "creating {0}".format(cabinet_label)
        r = requests.post('{0}/cabinets/'.format(api_base), data={'label': cabinet_label}, auth=(username, password))
        r.raise_for_status()
        cabinet_create_response = r.json()

    if 'cabinets' in cabinet:
        for cabinet_item in cabinet['cabinets']:
            create_cabinet_rec(cabinet_item, cabinet_create_response['id'])

def main():

    # https://www.thebalancecareers.com/how-to-organize-your-paperwork-3544878
    # https://www.reddit.com/r/datacurator/comments/a5ouiq/going_digital_with_documents/
    # https://www.reddit.com/r/datacurator/comments/8rd8fr/critique_my_planned_file_structure/


    # Read YAML file and generate cabinet
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "cabinet-structure.yaml"), 'r') as stream:
        cabinet_structure = yaml.load(stream)
        print cabinet_structure

        for cabinet_item in cabinet_structure['cabinets']:
            create_cabinet_rec(cabinet_item, None)

if __name__ == "__main__":
    main()