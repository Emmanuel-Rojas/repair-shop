document.getElementById('cliente-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const nombre = document.getElementById('nombre').value;
    const direccion = document.getElementById('direccion').value;
    const telefono = document.getElementById('telefono').value;
    const email = document.getElementById('email').value;

    const response = await fetch('http://localhost:8000/api/clientes/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        mode: 'cors',
        body: JSON.stringify({
            nombre: nombre,
            direccion: direccion,
            telefono: telefono,
            email: email
        })
    });

    if (response.ok) {
        alert('Cliente añadido exitosamente');
        fetchClientes();
    } else {
        alert('Error al añadir cliente');
    }
});

async function fetchClientes() {
    const response = await fetch('http://localhost:8000/api/clientes/');
    const clientes = await response.json();
    const clientesList = document.getElementById('clientes-list');
    clientesList.innerHTML = '';
    clientes.forEach(cliente => {
        const li = document.createElement('li');
        li.textContent = `${cliente.nombre} - ${cliente.direccion}`;
        clientesList.appendChild(li);
    });
}

// Cargar clientes al cargar la página
fetchClientes();
