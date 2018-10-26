class Lobby():
	games = []
	players = []

class Game():
	def __init__(self, rounds, entrants):
		self.rounds = rounds
		self.entrants = entrants

class Player():
	name = ""

def createNewGame(rounds, entrants):
	game = Game(rounds, entrants)
	Lobby.games.append(game)



