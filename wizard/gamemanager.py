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
		self.active_games = []

	def register(self, game):
		if game.status == "Open" and len(self.active_games) < 1:
			game.player_list.append(self)
			self.active_games.append(game)
			print(self.active_games)
			print(Lobby.games[0].player_list)
			return "Registration successful"
		else: return "Registration failed"
		

		if len(game.player_list) == game.entrants:
			game.status = "Full"

	def getPlayerByName(name):
		print(name)
		print(Lobby.players)
		player_list = [player for player in Lobby.players if player.name == name]
		player_obj = player_list[0]
		return player_obj






class Admin():
	def createNewGame(rounds, entrants):
		game = Game(rounds, entrants)
		Lobby.games.append(game)



