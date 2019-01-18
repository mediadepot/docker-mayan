from mayan_api_client import API
import yaml
import io
import re

#log into mayan edms server
api = API(host='http://localhost', username='admin', password='password')
print api._info