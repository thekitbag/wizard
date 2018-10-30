from flask import session, render_template, request, redirect, url_for, json
from wizard import app, db
from .models import User
from .forms import SignupForm, LoginForm, GameForm
from .gamemanager import Lobby, Player, Admin, Game

@app.route("/")
def index():
  if 'email' not in session:
    return render_template("index.html") 
  else: 
    return redirect(url_for('lobby', name=session.get('name')))

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
  if 'email' in session:
    return redirect(url_for('lobby', name=session.get('name')))

  form = SignupForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()

      session['email'] = newuser.email
      session['name'] = newuser.firstname
      return redirect(url_for('lobby', name=session.get('name')))

  elif request.method == "GET":
    return render_template('signup.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
  if 'email' in session:
    return redirect(url_for('lobby', name=session.get('name')))

  form = LoginForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template("login.html", form=form)
    else:
      email = form.email.data 
      password = form.password.data 

      user = User.query.filter_by(email=email).first()
      if user is not None and user.check_password(password):
        session['email'] = form.email.data
        session['name'] = user.firstname
        return redirect(url_for('lobby', name=session.get('name')))
      else:
        return redirect(url_for('login'))

  elif request.method == 'GET':
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
  session.pop('email', None)
  session.pop('name', None)
  return redirect(url_for('index'))

@app.route("/lobby", methods=["GET", "POST"])
def lobby():  
  	return render_template('lobby.html', name=session.get('name'))

@app.route("/adminlogin", methods=["GET", "POST"])
def adminlogin():

  form = LoginForm()

  if request.method == 'GET':
    return render_template('admin.html', form=form)

  elif request.method == 'POST':
    return redirect(url_for('createGame'))

@app.route("/creategame", methods=["GET", "POST"])
def createGame():
  form = GameForm()

  if request.method == "GET":
    return render_template('gamemanager.html', form=form)

  elif request.method == "POST":
    entrants = int(form.entrants.data)
    rounds = int(form.rounds.data)
    Admin.createNewGame(rounds, entrants)
    return "Game Created"

@app.route("/game", methods=["GET"])
def game():
  return render_template('game.html')

@app.route("/lobbydata", methods=["GET"])
def returnLobbyData():
  data = Lobby.getActiveGames()
  return json.dumps(data)

@app.route("/registerPlayer", methods=["GET", "POST"])
def registerPlayer():
  data = request.json
  game_id = int(data['id'])
  name = session['name']
  game = Game.getGameById(game_id)
  #find player object, if it exists, check active games
  #if it doesnt exist create it
  #if register play return



