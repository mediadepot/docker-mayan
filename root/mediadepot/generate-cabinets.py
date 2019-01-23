from mayan_api_client import API
import yaml
import io
import re

#log into mayan edms server
api = API(host='http://localhost', username='admin', password='4HJSmRDVFt')
print api._info

def create_cabinet_rec(cabinet, parent_cabinet_id):
    cabinet_label = cabinet['label']
    #cabinet_id = re.sub('[^A-Za-z0-9]+', '_', cabinet_label.lower())

    cabinet_create_response = None
    if parent_cabinet_id:
        print "creating {0} with parent: {1}".format(cabinet_label, parent_cabinet_id)
        cabinet_create_response = api.cabinets.cabinets.post({'label': cabinet_label, 'parent': parent_cabinet_id})

    else:
        print "creating {0}".format(cabinet_label)
        cabinet_create_response = api.cabinets.cabinets.post({'label': cabinet_label, 'parent': parent_cabinet_id})
        
    if 'cabinets' in cabinet:
        for cabinet_item in cabinet['cabinets']:
            create_cabinet_rec(cabinet_item, str(cabinet_create_response['id']))

def main():

    # https://www.thebalancecareers.com/how-to-organize-your-paperwork-3544878
    # https://www.reddit.com/r/datacurator/comments/a5ouiq/going_digital_with_documents/
    # https://www.reddit.com/r/datacurator/comments/8rd8fr/critique_my_planned_file_structure/


    # Read YAML file and generate cabinet
    with open("cabinet-structure.yaml", 'r') as stream:
        cabinet_structure = yaml.load(stream)
        print cabinet_structure

        for cabinet_item in cabinet_structure['cabinets']:
            create_cabinet_rec(cabinet_item, None)

if __name__ == "__main__":
    main()