# -*- coding: iso-8859-1 -*-
from mako.template import Template
from mako import exceptions
import glob

import structures
import conversions
import util

def write(data):
  data['conversions'] = conversions.c
  data['cppconversions'] = conversions.cpp
  data['capitalize'] = util.capitalize
  data['lowercase'] = util.lowercase
  data['dashify'] = util.dashify
  data['depends'] = util.depends
  data['Model'] = structures.Model
  for file in glob.glob('templates/visclient/files/*.txt'):
    writeFile(file[26:-4], data) #file[18:-4] should strip the templates/c/files/ and .txt
  for model in data['models']:
    data['model'] = model
    writeModel(data)

def writeFile(name, data):
  try:
    template = Template(filename='templates/visclient/files/%s.txt' % name)
    output = file('output/visclient/%s' % name, 'w')
    output.write(template.render(**data))
    output.close()
  except:
    print exceptions.text_error_template().render()

def writeModel(data):
  try:
    template = Template(filename='templates/visclient/model.h.txt')
    output = file('output/visclient/%s.h' % data['model'].name, 'w')
    output.write(template.render(**data))
    output.close()
    template = Template(filename='templates/visclient/model.cpp.txt')
    output = file('output/visclient/%s.cpp' % data['model'].name, 'w')
    output.write(template.render(**data))
    output.close()
  except:
    print exceptions.text_error_template().render()
