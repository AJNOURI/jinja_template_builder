#!/usr/bin/env python

import yaml
import jinja2
import os

# Load variables form yaml file
stream = open("data.yml",'r')
vars = yaml.load(stream)

#print(vars[0])

myloader = jinja2.FileSystemLoader('.')
jenv = jinja2.Environment(loader=myloader,trim_blocks=True,lstrip_blocks=True)
template = jenv.get_template('pe.jj2')

print(vars)
#print(vars['loopback'])
output=template.render(vars)
print(output)

with open('pe-ce.cfg', 'w') as fout:
    fout.write(output)

"""
for router in vars:
    print(template.render(router))

"""
