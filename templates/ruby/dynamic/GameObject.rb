require './library.rb'
require './ExistentialError.rb'


class GameObject
  def initialize(ptr)
    @ptr = ptr
    @iteration = BaseAI.iteration
  end
end

% for model in models:

#\
#${model.doc}
%   if model.parent:
class ${model.name} < ${model.parent.name}
%   else:
class ${model.name} < GameObject
%   endif
  def initialize(ptr)
    @ptr = ptr
    @iteration = BaseAI.iteration

    @id = Library.${lowercase(model.name)}GetId(ptr)
  end

%   if model.type == 'Model':
  def validify
    if @iteration == BaseAI.iteration
      return True
    end
    for i in BaseAI.${lowercase(model.plural)}
      if i.id == @id
        @ptr = i.ptr
        @iteration = BaseAI.iteration
        return True
      end
    end
    raise ExistentialError.new()
  end
%   endif
%  for func in model.functions + model.properties:
  #\
#${func.doc}
  def ${func.name}(\
%    for arg in func.arguments:
%     if func.arguments[0] is not arg:
, \
%     endif
${arg.name}\
%    endfor
)
    validify
%    for arg in func.arguments:
%      if isinstance(arg.type, Model):
    if not ${arg.name}.kind_of ${arg.type.name}
      raise TypeError.new '${arg.name} should be of [${arg.type.name}]'
    end
    ${arg.name}.validify
%      endif
%    endfor
    Library.${lowercase(model.name)}${capitalize(func.name)}(@ptr\
%    for arg in func.arguments:
%      if not isinstance(arg.type, Model):
, ${arg.name}\
%      else:
, ${arg.name}.ptr\
%      endif
%    endfor
)
    end

%  endfor
%  for datum in model.data:
  #\
#${datum.doc}
  def ${datum.name}
    validify
    return Library.${lowercase(model.name)}Get${capitalize(datum.name)}(@ptr)
  end

%  endfor
end

% endfor
