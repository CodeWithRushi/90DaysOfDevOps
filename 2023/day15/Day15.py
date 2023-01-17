import yaml
import json


dictionary={
    "aws":{
        "name":"EC2",
        "type":"pay per hour",
        "instances":500,
        "count": 500
        },
     "GCP":{
        "name":"COMPUTE ENGINE",
        "type":"pay per hour",
        "instances":500,
        "count": 500
        },
      "AZURE":{
        "name":"VM",
        "type":"pay per hour",
        "instances":500,
        "count": 500
        }
    }

'''
json_obj=json.dumps(dictionary,indent=5)
with open("services.json","w") as jsfile:
    jsfile.write(json_obj)
with open("services.json","r") as jsfile2:
    json_data=json.loads(jsfile2.read())

for key,value in json_data.items():
    print("\n",key,"   ",value.get('name'))
'''

with open("services.yaml","w") as ym:
    yaml.dump(dictionary,ym)
with open("services.yaml","r") as ymread:
    data=yaml.safe_load(ymread)
with open("services.json","w") as yml_json:
    json_data=yml_json.write(json.dumps(data))

yml_Data=data
yml_json_data=json_data