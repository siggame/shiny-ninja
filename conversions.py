# -*- coding: iso-8859-1 -*-
import structures

c = {int:'int', str:'char*', float:'float', bool:'int', chr:'char'}
cpp = {int:'int', str:'string', float:'float', bool:'int', chr:'char'}
java = {int:'int', str:'String', float:'float', bool:'int', chr:'char'}
cs = {int:'int', str:'string', float:'float', bool:'int', chr:'char'}
python = {int:'c_int', str:'c_char_p', float:'c_float', bool:'c_int', chr:'c_char'}
server = {int:'int', str:'str', float:'float', bool:'int', chr:'char'}

def addModels(data):
  for i in data.values():
      if isinstance(i, structures.Model):
        c[i] = '_' + i.name + '*'
        java[i] = 'Pointer'
        cs[i] = 'IntPtr'
        python[i] = 'c_void_p'
        server[i] = 'int'
