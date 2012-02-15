from mako.template import Template
from mako import exceptions

import structures
import conversions
import util
import os.path, os

class MakoWriter(object):
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
    try:
      template = Template(filename=infile)
      output = open(outfile, 'w')
      output.write(template.render(**data))
      output.close()
    except:
      print(exceptions.text_error_template().render())


class Writer(object):
  module = None
  writers = {}

  def getLocalData(self):
    data = {}
    data['conversions'] = getattr(conversions, self.module)
    data['capitalize'] = util.capitalize
    data['lowercase'] = util.lowercase
    data['Model'] = structures.Model
    return data

  def write(self, source, dest, objects):
    data = self.getLocalData()
    data.update(objects)

    for dir, writer in self.writers.items():
      s = os.path.join(source, dir)
      writer.write(s, dest, data)

class PythonWriter(Writer):
  module = 'python'
  writers = { '.' : MakoWriter() }

class ServerWriter(Writer):
  module = 'server'
  writers = { '.' : MakoWriter() }
