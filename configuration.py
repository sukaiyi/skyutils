import os
import sys
import json
import codecs

path = os.path.dirname(sys.argv[0])
if path:
	os.chdir(os.path.dirname(sys.argv[0]))

file = codecs.open('configuration.json','r','utf-8')
try:
	fileContent = file.read()
	Items = json.loads(fileContent)
finally:
	file.close()