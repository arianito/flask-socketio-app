var socket = io('http://localhost:5000/');

socket.on('connect', function(){
    document.getElementById("hello").innerText = "Connected.";
});

socket.on('reply-to-someone', function(data){
    document.getElementById("data").innerText = data;
    console.log(data);
});


socket.on('disconnect', function(){
    document.getElementById("hello").innerText = "Disconnected."
});


setInterval(function () {
    socket.emit('update');
}, 100);