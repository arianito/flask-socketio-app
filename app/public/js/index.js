//
// Created by Aryan Alikhani
//

(function(funcName, baseObj) {
    funcName = funcName || "docReady";
    baseObj = baseObj || window;
    var readyList = [];
    var readyFired = false;
    var readyEventHandlersInstalled = false;
    function ready() {
        if (!readyFired) {
            readyFired = true;
            for (var i = 0; i < readyList.length; i++) {
                readyList[i].fn.call(window, readyList[i].ctx);
            }
            readyList = [];
        }
    }

    function readyStateChange() {
        if ( document.readyState === "complete" ) {
            ready();
        }
    }
    baseObj[funcName] = function(callback, context) {
        if (typeof callback !== "function") {
            throw new TypeError("callback for docReady(fn) must be a function");
        }
        if (readyFired) {
            setTimeout(function() {callback(context);}, 1);
            return;
        } else {
            readyList.push({fn: callback, ctx: context});
        }
        if (document.readyState === "complete") {
            setTimeout(ready, 1);
        } else if (!readyEventHandlersInstalled) {
            if (document.addEventListener) {
                document.addEventListener("DOMContentLoaded", ready, false);
                window.addEventListener("load", ready, false);
            } else {
                document.attachEvent("onreadystatechange", readyStateChange);
                window.attachEvent("onload", ready);
            }
            readyEventHandlersInstalled = true;
        }
    }
})("docReady", window);



docReady(function () {

    const socket = io('http://localhost:5000/');


    socket.on('connect', function () {
        document.getElementById("hello").innerText = "Connected.";
    });



    socket.on('finger-detected', function () {
        document.getElementById("hello").innerText = "Finger detected";
    });

    socket.on('reply-to-someone', function (data) {
        document.getElementById("data").innerText = data;
        console.log(data);
    });

    socket.on('disconnect', function () {
        document.getElementById("hello").innerText = "Disconnected."
    });

    setInterval(function () {
        socket.emit('update');
    }, 80);
});