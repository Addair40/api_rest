function putCliente(){
 
    let id_cliente = document.getElementById("id_cliente");
    let nombre = document.getElementById("nombre");
    let email = document.getElementById("email");

    let payload = {
        "id_cliente": id_cliente.value,
        "nombre": nombre.value,
        "email": email.value
    }

    console.log("id_cliente: " + id_cliente.value);
    console.log("nombre: " + nombre.value);
    console.log("email: " + email.value);

    var request = new XMLHttpRequest();
    request.open('PUT', 'https://8000-addair40-apirest-f10xdgpxpdk.ws-us53.gitpod.io/clientes/'+id_cliente, true);
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
            window.location.replace("/get_clientes.html");
        }
    };

    request.send(JSON.stringify(payload));

};
