require './library.rb'
require './GameObject.rb'

# This class implements most the code an AI would need to interface with the lower-level game code.
# AIs should extend this class to get a lot of builer-plate code out of the way
# The provided AI class does just that.
class BaseAI
  @initialized = false
  @@iteration = 0
  @connection = nil
% for model in models:
%   if model.type == 'Model':
  @@${lowercase(model.plural)} = []
%   endif
% endfor

  def BaseAI.iteration
    @@iteration
  end

  def startTurn
% for model in models:
%   if model.type == 'Model':
    @@${lowercase(model.plural)} = Library.get${model.name}Count(@connection).times.collect do |i|
      ${model.name}.new Library.get${model.name}(@connection, i)
    end
%   endif
% endfor

    if not @initialized
      @initialized = true
      init
    end
    @@iteration += 1;
    run
  end

% for datum in globals:
  ##${datum.doc}
  def ${datum.name}
    Library.get${capitalize(datum.name)}(@connection)
  end
% endfor
  def initialize(connection)
    @connection = connection
  end
end
