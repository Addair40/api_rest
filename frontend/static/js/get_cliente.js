function getCliente(){
    var id_cliente = window.location.search.substring(1);
    console.log("id_cliente: " + id_cliente);

    const request = new XMLHttpRequest();
    request.open("GET", "https://8000-addair40-apirest-f10xdgpxpdk.ws-us53.gitpod.io/clientes/"+id_cliente,true);
    request.setRequestHeader("Accept", "application/json");

    request.onload = () =>{
        const response = request.responseText;
        const json = JSON.parse(response);
        const status = request.status;

        console.log("Response " + response);
        console.log("Json " +  json);
        console.log("Status: " + status);

        if(status == 200){

        let nombre = document.getElementById("nombre");
        let email = document.getElementById("email");

        nombre.value = json.nombre;
        email.value = json.email;
        }
        else if(status == 404){
            let nombre = document.getElementById("nombre");
            let email = document.getElementById("email");
            nombre.value = "None";
            email.value = "None";
            alert("Cliente no encontrado");
        }
    };
    request.send();
};
