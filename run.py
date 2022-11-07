#! /usr/bin/env python3

import os
import requests
import json
text_files = os.listdir("/data/feedback")
# data_dict = {"title":"test","name":"test","date":"test","feedback":"test"} 
data_dict = {} 

for txt in text_files: 
    with open("/data/feedback/"+txt) as fileobj:
        list_of_entries = fileobj.readlines()
        data_dict["title"] = list_of_entries[0].strip()
        data_dict["name"] = list_of_entries[1].strip()
        data_dict["date"] = list_of_entries[2].strip()
        data_dict["feedback"] = list_of_entries[3].strip()
    # print(data_dict)   
    # print(type(data_dict)) 
    # data_dict = json.dumps(data_dict,indent=2)
    # # print(list_of_entries)
    # print(data_dict)
    response = requests.post("http://34.171.26.201/feedback/",json=data_dict)
    print(response.status_code)
    response.raise_for_status()
