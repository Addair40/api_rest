function getClientes(){
    var query = window.location.search.substring(1);
    console.log("Query: " + query)

    //Conectar con el backend
    var request = new XMLHttpRequest();
    username= sessionStorage.getItem("username");
    password= sessionStorage.getItem("password");

    console.log("Username: " + username);
    console.log("Password: " + password);

    request.open('GET', 'http://127.0.0.1:8000/clientes/', true);
    request.setRequestHeader("Accept", "application/json");

    request.onload = () => {
        const response = request.response.responseText;
        const json = JSON.parse(response);
        console.log("Response " + response);
        console.log("Json " +  json);

        var tbody = document.getElementById("tbody_clientes");

        for(let row=0; row<json.length; row++){
            var tr = document.createElement('tr');
            var id_clientes = document.createElement('td');
            var nombre = document.createElement('td');
            var email = document.createElement('td');

            id_clientes.innerHTML = json[i].id_clientes;
            nombre.innerHTML = json[i].nombre;
            email.innerHTML = json[i].emil;

            tr.appendChild(id_clientes);
            tr.appendChild(nombre);
            tr.appendChild(email);

            tbody.appendChild(tr);

        }
    
    };
    request.send();
};
