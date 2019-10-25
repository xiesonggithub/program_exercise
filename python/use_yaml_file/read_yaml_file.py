#! /usr/bin/python3

import yaml
import os

def get_yaml_data(yaml_file):
    with open(yaml_file,'r') as f:
        file_data = f.read()     #get all the yaml_file
        f.close()
        print(file_data)
        print(type(file_data))   #str

        #convert yaml_data to dict or list
        data = yaml.load(file_data)
        print(data)
        # {'common': {'workers': 3, 'batch_size': 4, 'model': {'arch': 'gan'}}}
        print(type(data))

current_path = os.path.abspath('.')
yaml_path = os.path.join(current_path, 'config.yaml')


get_yaml_data(yaml_path)


