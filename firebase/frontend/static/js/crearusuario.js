function crearUsuario(){
    let email = document.getElementById("email");
    let password = document.getElementById("password");

    let payload = {
        "email": email.value,
        "password": password.value
    }

    console.log("email: " + email.value);
    console.log("password: " + password.value);

    var request = new XMLHttpRequest();
    request.open('POST', 'https://8000-addair40-apirest-f10xdgpxpdk.ws-us54.gitpod.io/users/', true);
    request.setRequestHeader("Content-Type","application/json");
    request.setRequestHeader("Accept","application/json");

    request.onload = () =>{
        const response = request.responseText;
        const json = JSON.parse(response);
        const status = request.status;

        console.log("Response " + response);
        console.log("Json " +  json);
        console.log("Status: " + status);

        if(status == 200){
            alert(json.message);
            window.location.replace("/index.html");
        }
    };

    request.send(JSON.stringify(payload));

};
