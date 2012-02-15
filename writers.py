from mako.template import Template
from mako import exceptions

import structures
import conversions
import util
import os.path, os
import shutil

class MakoWriter(object):
  def write(self, source, dest, data):
    for dir, subdirs, files in os.walk(source):
      #duplicate the source directory structure in the dest
      outdir = dir.replace(source, dest, 1)
      os.makedirs(outdir, exist_ok=True)
      for i in files:
        infile = os.path.join(dir, i)
        template = Template(i)
        i = template.render(**data)
        outfile = os.path.join(outdir, i)
        self.writeFile(infile, outfile, data)


  def writeFile(self, infile, outfile, data):
    try:
      template = Template(filename=infile)
      output = open(outfile, 'w')
      output.write(template.render(**data))
      output.close()
    except:
      print(exceptions.text_error_template().render())

class StaticWriter(object):
  def write(self, source, dest, data):
    for dir, subdirs, files in os.walk(source):
      #duplicate the source directory structure in the dest
      outdir = dir.replace(source, dest, 1)
      os.makedirs(outdir, exist_ok=True)
      for i in files:
        infile = os.path.join(dir, i)
        outfile = os.path.join(outdir, i)
        self.writeFile(infile, outfile, data)


  def writeFile(self, infile, outfile, data):
    shutil.copy2(infile, outfile)

class IterWriter(object):
  def __init__(self, writer, item, list):
    self.writer = writer
    self.item = item
    self.list = list
  def write(self, source, dest, data):
    for i in data[self.list]:
      data[self.item] = i
      self.writer.write(source, dest, data)



class ModuleWriter(object):
  module = None
  writers = { 'dynamic' : MakoWriter(),
              'model' : IterWriter(MakoWriter(), 'model', 'models'),
              'static' : StaticWriter()
              }

  def getLocalData(self):
    data = {}
    data['conversions'] = getattr(conversions, self.module)
    data['capitalize'] = util.capitalize
    data['lowercase'] = util.lowercase
    data['Model'] = structures.Model
    data['dashify'] = util.dashify
    data['depends'] = util.depends
    return data

  def write(self, source, dest, data):
    data.update(self.getLocalData())

    for dir, writer in self.writers.items():
      s = os.path.join(source, dir)
      if os.path.isdir(s):
        writer.write(s, dest, data)

class PythonWriter(ModuleWriter):
  module = 'python'

class ServerWriter(ModuleWriter):
  module = 'server'

class CWriter(ModuleWriter):
  module = 'c'

class CppWriter(ModuleWriter):
  module = 'c'

class JavaWriter(ModuleWriter):
  module = 'java'
class CSharpWriter(ModuleWriter):
  module = 'csharp'


class VisualizerWriter(ModuleWriter):
  module = 'c'

class VisClientWriter(CWriter):
  pass

