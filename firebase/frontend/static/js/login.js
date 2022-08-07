function login() {   

    let email = document.getElementById("email");
    let password  = document.getElementById("password");  
    let payload = {
        "email" : email.value,
        "password" : password.value
    }
    console.log(email.value);
    console.log(password.value );
    console.log(payload);

    var request = new XMLHttpRequest();
    request.open('GET','https://8000-addair40-apirest-f10xdgpxpdk.ws-us59.gitpod.io/users/token',true);
    request.setRequestHeader("Authorization", "Basic " + btoa(email.value+":"+password.value));
    request.setRequestHeader('Content-Type', 'application/json');
    request.setRequestHeader('accept', 'application/json');

    request.onload = function(){
        const status = request.status
        json = JSON.parse(request.responseText);

        if (status == 202) {
            getToken(json.token);
            
        }

        else{
            alert(json.detail);
        }
    };
    request.send();
};

function getToken(token){

    var request = new XMLHttpRequest();
    request.open("GET","https://8000-addair40-apirest-f10xdgpxpdk.ws-us59.gitpod.io/users/",true);
    request.setRequestHeader('Authorization', 'Bearer '+token);
    request.setRequestHeader('Content-Type', 'application/json');
    request.setRequestHeader('accept', 'application/json');

    request.onload = function(){

        const status = request.status

        if (status == 202) {
            json = JSON.parse(request.responseText);
            sessionStorage.setItem("token",token);
           
            window.location.replace("/bienvenida.html");
        }

        else{
            alert(json.detail);
        }
    }
    request.send();
}
