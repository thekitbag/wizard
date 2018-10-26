function createElement(type, className, id){
	a = document.createElement(type);
	a.setAttribute("class", className);
	a.setAttribute("id", id);
	return a
}

function attatchElement(element, target){
	return document.getElementById(target).appendChild(element);
}

function registerPlayer(id) {
	var url = '/registerPlayer';
	var data = {'id': id};

	fetch(url, {
	  method: 'POST', 
	  body: JSON.stringify(data), 
	  headers:{
	    'Content-Type': 'application/json'
	  }
	}).then(res => res.json())
	.then(response => console.log('Success:', JSON.stringify(response)))
	.catch(error => console.error('Error:', error));	
}



function addGamesToList(gamedata){
	var number_of_games = gamedata.length
	for (var i = 0; i < number_of_games; i++) {
		var gameid = i+1		
		var game = createElement("div", "game-row", "game"+gameid)
		attatchElement(game,"games-list");			
		for (var j = 0; j < 4; j++){
			keys = ["game_id", "entrants", "player_list", "status"]
			titles = 	["ID", "Size", "Players", "Status"]					
			var game_info_entry = createElement("div", "game-info-entry", "game"+gameid+"box"+j);
			var infotitle = createElement("div", "title", "game"+gameid+"title"+titles[j]);
			var infovalue = createElement("div", "value", "game"+gameid+"value"+titles[j]);
			attatchElement(game_info_entry, "game"+gameid)
			game_info_entry.appendChild(infotitle);
			game_info_entry.appendChild(infovalue);
			infotitle.innerHTML = titles[j]
			infovalue.innerHTML = gamedata[i][keys[j]]			
		}		
		var regbutton = createElement("div", "btn reg", "reg"+gameid);
		regbutton.innerHTML = "Register";		
		attatchElement(regbutton, "game"+gameid);		
	}	
}




fetch("/lobbydata")
  .then(function(response) {
    return response.json();    
  })
  .then(function(myJson) {
    console.log(myJson);
    addGamesToList(myJson);
    document.addEventListener('click', function (event) {

	if (event.target.matches('.reg')) {
		var id = event.target.parentElement.id[4];
		registerPlayer(id)
	}

}, false);
  });






