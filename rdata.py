#!/usr/bin/python

import yaml

sfile = "tree.yaml"


try:
    stream = open(sfile)
    data = yaml.load(stream)

except IOError:
    print('File % NOT found',sfile)

#print(data)

def read_yaml_file(d):
    for key, item in d.items():
        print(key,":",item)

read_yaml_file(data)

