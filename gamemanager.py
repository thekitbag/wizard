class Lobby():
	games = []
	players = []

class Game():
	id_count = 0
	def __init__(self, rounds, entrants):
		self.rounds = rounds
		self.entrants = entrants
		self.game_id = Game.id_count + 1
		Game.id_count += 1

class Player():
	name = ""

def createNewGame(rounds, entrants):
	game = Game(rounds, entrants)
	Lobby.games.append(game)



