# -*- coding: iso-8859-1 -*-
from structures import *

aspects = ['timer']

gameName = "chess"

constants = [
  ]

playerData = [
  ]

playerFunctions = [
  ]

Move = Model('CamelCase',
  data=[ Variable('memberVar', int, 'The initial file location'),
    ],
  functions=[Function('memberFun', [Variable('fileVar', int), Variable('rankVar', int), Variable('typeVar', int) ]) ],
  doc='A chess move',
  )

globals = [
  Variable('turnNumber', int, 'How many turns it has been since the beginning of the game'),
  Variable('playerID', int, 'Player Number; either 0 or 1'),
  Variable('gameNumber', int, 'What number game this is for the server'),
  ]


