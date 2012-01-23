class Move:
  def __init__(self, game, id, fromFile, fromRank, toFile, toRank, promoteType):
    self.game = game
    self.id = id
    self.fromFile = fromFile
    self.fromRank = fromRank
    self.toFile = toFile
    self.toRank = toRank
    self.promoteType = promoteType

  def toList(self):
    value = [
      self.id,
      self.fromFile,
      self.fromRank,
      self.toFile,
      self.toRank,
      self.promoteType,
      ]
    return value

  def nextTurn(self):
    pass



class Piece:
  def __init__(self, game, id, owner, file, rank, hasMoved, type):
    self.game = game
    self.id = id
    self.owner = owner
    self.file = file
    self.rank = rank
    self.hasMoved = hasMoved
    self.type = type

  def toList(self):
    value = [
      self.id,
      self.owner,
      self.file,
      self.rank,
      self.hasMoved,
      self.type,
      ]
    return value

  def nextTurn(self):
    pass

  def move(self, file, rank, type):
    pass



