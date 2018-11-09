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

	def getGameData(game_id):
		game = Game.getGameById(game_id)
		gamedata = {}
		gamedata['game_id'] = game.game_id
		gamedata['status'] = game.status
		gamedata['entrants']= game.entrants
		gamedata['player_list'] = []
		for player in game.player_list:
			gamedata['player_list'].append(player.name)
		print(gamedata)
		return gamedata


class Player():
	current_member_id = 0
	def __init__(self, name):
		self.name = name
		self.memberid = Player.current_member_id + 1
		self.active_games = []
		Lobby.players.append(self)
		Player.current_member_id += 1

	def __repr__(self):
		return "player obj, name: " + self.name + ", memberID: " + str(self.memberid)

	def register(self, game):
		if game.status == "Open" and len(self.active_games) < 1:
			game.player_list.append(self)
			self.active_games.append(game)

			if len(game.player_list) == game.entrants:
				game.status = "Full"

			return "Registration successful"
		else: return "Registration failed"		

	def unRegister(self, game):		
		game.player_list.remove(self)
		self.active_games.remove(game)
		return self.active_games

	def getPlayerByName(name):
		player_list = [player for player in Lobby.players if player.name == name]
		if len(player_list) > 0:
			player_obj = player_list[0]
			return player_obj
		else: return "No Player with this name"

	def getOtherEntrants(user, game):
		players = []
		print(game.player_list)
		for player in game.player_list:
			if player.name != user.name:
				players.append(player.name)
		return players







class Admin():
	def createNewGame(rounds, entrants):
		game = Game(rounds, entrants)
		Lobby.games.append(game)



