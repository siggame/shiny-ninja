#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
import structures
import argparse
from util import *

def import_file(full_path_to_module):
  try:
    import os
    module_dir, module_file = os.path.split(full_path_to_module)
    module_name, module_ext = os.path.splitext(module_file)
    save_cwd = os.getcwd()
    os.chdir(module_dir)
    module_obj = __import__(module_name)
    module_obj.__file__ = full_path_to_module
    globals()[module_name] = module_obj
    os.chdir(save_cwd)
  except:
    raise ImportError

def insertModel(list, model):
  if model.parent and model.parent not in list:
    insertModel(list, model.parent)
  if model not in list:
    list.append(model)

def parseData():
  aspects = data.aspects
  data.Player = structures.Model("Player", data=[structures.Variable("playerName", str, "Player's Name")])
  if 'timer' in aspects:
    import timerAspect
    timerAspect.install(data)
  data.Player.addData(data.playerData)
  data.Player.addFunctions(data.playerFunctions)
  models = []
  globals = data.globals
  constants = data.constants
  animations = []
  gameName = data.gameName

  for i in members(data):
    if isinstance(i, structures.Model):
      insertModel(models, i)
    elif isinstance(i, structures.Animation):
      animations.append(i)
  return {'models':models, 'globals':globals, 'constants':constants, 'animations':animations, 'aspects':aspects, 'gameName':gameName}



if __name__ == '__main__':

  parser = argparse.ArgumentParser(description='Run The Codegen To Automatically Generate Some Codez')
  parser.add_argument('-d', '--data', dest='dataPyPath', default='./data.py', help='The Path To data.py')
  parser.add_argument('-o', '--output', dest='outDir', default='./output', help='The output of the codegen.')

  args = parser.parse_args()

  import_file(args.dataPyPath);

  objects = parseData()

  import writers
  w = writers.PythonWriter()
  w.write('templates/python', 'output/python', objects)
  w = writers.ServerWriter()
  w.write('templates/server', 'output/server', objects)
  w = writers.CWriter()
  w.write('templates/c', 'output/c', objects)
