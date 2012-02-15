#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
import structures
import argparse
import runpy
import os.path
import conversions

def insertModel(list, model):
  if model.parent and model.parent not in list:
    insertModel(list, model.parent)
  if model not in list:
    list.append(model)

def parseData(data):
  aspects = data['aspects']
  data['Player'] = structures.Model("Player", data=[structures.Variable("playerName", str, "Player's Name")])
  if 'timer' in aspects:
    import timerAspect
    timerAspect.install(data)
  data['Player'].addData(data['playerData'])
  data['Player'].addFunctions(data['playerFunctions'])
  models = []
  globals = data['globals']
  constants = data['constants']
  animations = []
  gameName = data['gameName']

  for i in data.values():
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

  data = runpy.run_path(args.dataPyPath)

  objects = parseData(data)
  conversions.addModels(data)
  output = args.outDir

  import writers
  w = writers.PythonWriter()
  w.write('templates/python', os.path.join(output, 'python'), objects)
  w = writers.ServerWriter()
  w.write('templates/server', os.path.join(output, 'server'), objects)
  w = writers.CWriter()
  w.write('templates/c', os.path.join(output, 'c'), objects)
  w = writers.JavaWriter()
  w.write('templates/java', os.path.join(output, 'java'), objects)
  w = writers.CSWriter()
  w.write('templates/cs', os.path.join(output, 'cs'), objects)
  w = writers.VisualizerWriter()
  w.write('templates/visualizer', os.path.join(output, 'visualizer'), objects)
  w = writers.VisClientWriter()
  w.write('templates/visclient', os.path.join(output, 'visclient'), objects)
