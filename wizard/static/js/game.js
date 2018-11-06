var socket = io.connect('http://' + document.domain + ':' + location.port);
        socket.on('connect', function() {
            socket.emit('connect event');
        });

function unRegisterPlayer() {
	url = '/unRegister'
	var xhr = new XMLHttpRequest();
	xhr.open("POST", url, true);
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.onreadystatechange = function () {
	    if (xhr.readyState === 4 && xhr.status === 200) {
	        if (xhr.responseText == "Player Unregistered") {
	        	window.location.href = "/lobby";
	        } 	        
	    }
	};
	//var data = JSON.stringify({"email": "hey@mail.com", "password": "101010"});
	xhr.send();
}


function addUnRegisterListener() {
	document.addEventListener('click', function (event) {
		if (event.target.matches('#unregister')) {
			unRegisterPlayer();
		}

	}, false)};

addUnRegisterListener()