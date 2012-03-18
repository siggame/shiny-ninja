#!/bin/env ruby

require './library.rb'
require './AI.rb'

if ARGV.length < 1
  print "Please enter a host name."
  exit 1
end

connection = Library.createConnection

ai = AI.new(connection)

success = Library.serverConnect(connection, ARGV[0], "19000")
if not success
  $stderr.puts "Unable to connect to server\n"
  exit 1
end

if not Library.serverLogin(connection, ai.username, ai.password)
  exit 1
end

if ARGV.length < 2
  Library.createGame(connection)
else
  Library.joinGame(connection, ARGV[1].to_i, "player")
end
while Library.networkLoop(connection)
  if ai.startTurn
    Library.endTurn(connection)
  else
    Library.getStatus(connection)
  end
end

#Grab the end game state
Library.networkLoop(connection)
#request the log file
Library.networkLoop(connection)

ai.end
exit 0
