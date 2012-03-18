require './BaseAI.rb'
require './GameObject.rb'

class AI <BaseAI
  """The class implementing gameplay logic."""
  def username
    "Shell AI"
  end

  def password
    return "password"
  end

  ##This function is called once, before your first turn
  def init
  end

  ##This function is called once, after your last turn
  def end
  end

  ##This function is called each time it is your turn
  ##Return true to end your turn, return false to ask the server for updated information
  def run
    1
  end
end
