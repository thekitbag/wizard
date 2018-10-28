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
				gamedata['player_list'] = []
				for player in game.player_list:
					gamedata['player_list'].append(player.name)
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

	def getGameById(game_id):		
		game_list = [game for game in Lobby.games if game.game_id == game_id]
		game_obj = game_list[0]
		return game_obj


class Player():

	def __init__(self, name):
		self.name = name
		self.memberid = 0

	def register(self, game):
		if game.status == "Open" and len(game.player_list) < game.entrants:
			game.player_list.append(self)

		if len(game.player_list) == game.entrants:
			game.status = "Full"

class Admin():
	def createNewGame(rounds, entrants):
		game = Game(rounds, entrants)
		Lobby.games.append(game)



