/* const socket = io.connect('127.0.0.1:5000');
socket.on('connect', (sock) =>{
    console.log(socket.id);
    socket.send('Connected to server');
});

socket.on('log', (data) =>{
    console.log(data);
    
},
);

socket.on('message', (data) =>{
    console.log(data);
    data("Recieved");
});
 */
function loadLog(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            console.log(this.responseText);
            
        }
    };
    xhttp.open("GET", "get-cached-log?t=" + Math.random(), true);
    xhttp.send();
}

function fun(){
    $.ajax('/get-cached-log',{
        type: "GET",
        dataType: "json"
    }).done(function (messages){
        var data = JSON.parse(messages);
        for (var i = 0; i < data.length; i++){
            var message = document.createElement("div");
            message.appendChild(document.createTextNode(data));
            message.className = "log-element";
            var logbox = document.getElementById("log");
            logbox.appendChild(message);
        }
    });
    //setTimeout(fun(), 1000);
}

/* var evtSource = new EventSource("get-cached-log");
evtSource.onmessage = function(e) {
    console.log(e.data);
} */

document.addEventListener('DOMContentLoaded', fun(), false);