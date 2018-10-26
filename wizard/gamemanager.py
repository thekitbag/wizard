class Lobby():
	games = []
	players = []

	def getActiveGames():
		games = []
		for game in Lobby.games:
			if game.status == "Open":
				gamedata = {}
				gamedata['game_id'] = game.game_id
				gamedata['status'] = game.status
				gamedata['entrants']= game.entrants
				gamedata['player_list'] = game.player_list
				games.append(gamedata)
		return games


class Game():
	id_count = 0

	def __init__(self, rounds, entrants):
		self.rounds = rounds
		self.entrants = entrants
		self.status = "Open"
		self.game_id = Game.id_count + 1
		self.player_list = []
		Game.id_count += 1

	def __repr__(self):
		return "Game" + str(self.game_id)

class Player():
	name = ""

def createNewGame(rounds, entrants):
	game = Game(rounds, entrants)
	Lobby.games.append(game)



