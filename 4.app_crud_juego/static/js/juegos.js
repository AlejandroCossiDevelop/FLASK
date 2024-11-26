// Modal de edicion de juego
const modalEditarJuego = document.getElementById('modalEditarJuego');
if (modalEditarJuego) {
    modalEditarJuego.addEventListener('show.bs.modal', function (event) {
        const button = event.relatedTarget; 
        const id = button.getAttribute('data-id');
        const nombre = button.getAttribute('data-nombre');
        const descripcion = button.getAttribute('data-descripcion');
        const precioCompra = button.getAttribute('data-preciocompra');
        const precioVenta = button.getAttribute('data-precioventa'); 
        const stock = button.getAttribute('data-stock'); 

        // Llenar los campos del formulario de edicion
        document.getElementById('editId').value = id;
        document.getElementById('editNombre').value = nombre;
        document.getElementById('editDescripcion').value = descripcion;
        document.getElementById('editPrecioCompra').value = precioCompra;
        document.getElementById('editPrecioVenta').value = precioVenta; 
        document.getElementById('editStock').value = stock; 
    });
}

// Modal de detalles del juego
document.addEventListener("DOMContentLoaded", function () {
    const detalleButtons = document.querySelectorAll(".btn-detalles");

    detalleButtons.forEach(button => {
        button.addEventListener("click", function () {
            const juegoId = this.dataset.id;

            // Llamada a la API para obtener los detalles del juego
            fetch(`/juegos/${juegoId}`)
                .then(response => response.json())
                .then(data => {
                    // Actualizar el contenido del modal con los datos del juego
                    document.getElementById("detalleNombre").innerText = data.nombre;
                    document.getElementById("detalleDescripcion").innerText = data.descripcion;
                    document.getElementById("detallePrecioCompra").innerText = `$${data.precioCompra}`;
                    document.getElementById("detallePrecioVenta").innerText = `$${data.precioVenta}`; 
                    document.getElementById("detalleStock").innerText = data.stock; 
                    
                    // Mostrar el modal de detalles
                    const detalleModal = new bootstrap.Modal(document.getElementById('modalDetallesJuego'));
                    detalleModal.show();
                })
                .catch(error => {
                    console.error("Error al obtener detalles:", error);
                });
        });
    });
});
