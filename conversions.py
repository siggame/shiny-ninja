# -*- coding: iso-8859-1 -*-
import structures

c = {}
cpp = {}
java = {}
csharp = {}
python = {}
server = {}

c['conversions'] = {int:'int', str:'char*', float:'float', bool:'int', chr:'char'}
cpp['conversions'] = {int:'int', str:'string', float:'float', bool:'int', chr:'char'}
java['conversions'] = {int:'int', str:'String', float:'float', bool:'int', chr:'char'}
csharp['conversions'] = {int:'int', str:'string', float:'float', bool:'int', chr:'char'}
python['conversions'] = {int:'c_int', str:'c_char_p', float:'c_float', bool:'c_int', chr:'c_char'}
server['conversions'] = {int:'int', str:'str', float:'float', bool:'int', chr:'char'}

def addModels(data):
  for i in data.values():
      if isinstance(i, structures.Model):
        c['conversions'][i] = '_' + i.name + '*'
        java['conversions'][i] = 'Pointer'
        csharp['conversions'][i] = 'IntPtr'
        python['conversions'][i] = 'c_void_p'
        server['conversions'][i] = 'int'
