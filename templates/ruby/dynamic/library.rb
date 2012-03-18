# -*-ruby-*-

require 'ffi'

module Library
  extend FFI::Library
  ffi_lib 'client'
  #commands
  attach_function 'createConnection', [], :pointer
  attach_function 'serverConnect', [:pointer, :string, :string], :int
  attach_function 'serverLogin', [:pointer, :string, :string], :int
  attach_function 'createGame', [:pointer], :int
  attach_function 'joinGame', [:pointer, :int, :string], :int
  attach_function 'endTurn', [:pointer], :void
  attach_function 'getStatus', [:pointer], :void
  attach_function 'networkLoop', [:pointer], :int

  #Functions
%for model in models:
%  for func in model.functions:
  attach_function '${lowercase(model.name)}${capitalize(func.name)}', [${conversions[model]}\
%    for arg in func.arguments:
, \
${conversions[arg.type]}\
%    endfor
], :int

%  endfor
%endfor

# accessors

#Globals
%for datum in globals:
  attach_function 'get${capitalize(datum.name)}', [:pointer], ${conversions[datum.type]}
%endfor

%for model in models:
%   if model.type == 'Model':
  attach_function 'get${model.name}', [:pointer, :int], :pointer
  attach_function 'get${model.name}Count', [:pointer], :int

%   endif
%endfor

# getters

#Data
%for model in models:
%  for datum in model.data:
%    if not isinstance(datum.type, Model):
  attach_function '${lowercase(model.name)}Get${capitalize(datum.name)}', [:pointer], ${conversions[datum.type]}
%    else:
  attach_function '${lowercase(model.name)}Get${capitalize(datum.name)}', [:pointer], :int
%    endif

%  endfor
%endfor


#Properties
%for model in models:
%  for prop in model.properties:
  attach_function '${lowercase(model.name)}${capitalize(prop.name)}', [${conversions[model]}\
%    for arg in prop.arguments:
, \
${conversions[arg.type]}\
%  endfor
], :int

% endfor
%endfor
end
