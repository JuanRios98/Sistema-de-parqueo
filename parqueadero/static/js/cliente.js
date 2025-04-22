function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');



// Código JavaScript para manejar el modal de edición y la creación de clientes

document.addEventListener("DOMContentLoaded", function () {
  const modalElement = document.getElementById("editarModal");
  const modal = new bootstrap.Modal(modalElement, {
    keyboard: false, // Desactivar el cierre del modal al presionar ESC
    backdrop: 'static' // Desactivar el cierre del modal al hacer clic fuera de él
  });

  
  // Modal de editar cliente
  // Escuchar todos los botones de edición
  document.querySelectorAll(".btn-editar").forEach(boton => {
    boton.addEventListener("click", function () {
      const clienteId = this.dataset.id;
      const nombre = this.dataset.nombre;
      const apellido = this.dataset.apellido;
      const tipoPlan = this.dataset.plan;
      const fechaInicio = this.dataset.inicio;
      const fechaFin = this.dataset.fin;

      console.log(clienteId, nombre, apellido);

      document.getElementById("edit-id-view").value = clienteId;
      document.getElementById("edit-id").value = clienteId;
      document.getElementById("edit-nombre").value = nombre;
      document.getElementById("edit-apellido").value = apellido;
      document.getElementById("edit-tipo-plan").value = tipoPlan;
      document.getElementById("edit-inicio").value = fechaInicio;
      document.getElementById("edit-fin").value = fechaFin || '';

      modal.show(); // Mostrar el modal
      setTimeout(() => {
        modalElement.querySelector("#edit-tipo-plan").focus(); // Focalizar el primer campo del modal
      }, 500); // Esperar medio segundo para asegurar que el modal esté completamente visible
    });
  });

  // Manejo del envío del formulario
  document.getElementById("editarForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const clienteId = document.getElementById("edit-id").value;
    const nombre = document.getElementById("edit-nombre").value;
    const apellido = document.getElementById("edit-apellido").value;
    const tipoPlan = document.getElementById("edit-tipo-plan").value;
    const fechaInicio = document.getElementById("edit-inicio").value;
    const fechaFin = document.getElementById("edit-fin").value || null;

    // Verificación de que los campos no estén vacíos
    if (!tipoPlan || !fechaInicio) {
      Swal.fire({
        icon: 'warning',
        title: 'Campos incompletos',
        text: 'Por favor, complete todos los campos requeridos.'
      });
      return;
    }

    fetch(`/cliente/${clienteId}/`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')  // ✅ aquí ya funciona si está definida arriba
      },
      body: JSON.stringify({
        nombre: nombre,
        apellido: apellido,
        tipo_plan: tipoPlan,
        fecha_inicio: fechaInicio,
        fecha_fin: fechaFin
      })
    })
    .then(response => {
      if (!response.ok) throw new Error("Error al actualizar");
      return response.json();
    })
    .then(data => {
      Swal.fire({
        icon: 'success',
        title: 'Cliente actualizado con éxito',
        showConfirmButton: false,
        timer: 2000
      }).then(() => {
        modal.hide(); // Cierra el modal antes de recargar
        location.reload();
      });
    }).catch(error => {
      Swal.fire({
        icon: 'error',
        title: 'Error',
        text: 'Hubo un error al actualizar el cliente.'
      });
      console.error(error);
    });
  });
});


function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (const cookie of cookies) {
      const trimmed = cookie.trim();
      if (trimmed.startsWith(name + '=')) {
        cookieValue = decodeURIComponent(trimmed.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}



document.addEventListener("DOMContentLoaded", function () {
  // Obtener el modal y configurarlo
  const modalElement = document.getElementById("crearModal"); // Asegúrate que este ID esté en el <div class="modal">, no en el form
  const modal = new bootstrap.Modal(modalElement, {
    keyboard: false,
    backdrop: 'static'
  });

  // Manejar el formulario de creación
  document.getElementById("crearForm").addEventListener("submit", function (e) {
    e.preventDefault();
    const nombre = document.getElementById("nuevo-nombre").value;
    const apellido = document.getElementById("nuevo-apellido").value;
    const tipoPlan = document.getElementById("nuevo-tipo-plan").value;
    const fechaInicio = document.getElementById("nuevo-inicio").value;
    const fechaFin = document.getElementById("nuevo-fin").value || null;

    fetch('/cliente/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
      },
      body: JSON.stringify({
        nombre: nombre,
        apellido: apellido,
        tipo_plan: tipoPlan,
        fecha_inicio: fechaInicio,
        fecha_fin: fechaFin
      })
    })
    .then(response => {
      return response.json().then(data => {
        if (!response.ok) throw new Error("Error al crear el cliente");
        return data;
      });
    })
    .then(data => {
      Swal.fire({
        icon: 'success',
        title: 'Cliente creado con éxito',
        showConfirmButton: false,
        timer: 2000
      }).then(() => {
        location.reload();
      });
    })
    .catch(error => {
      Swal.fire({
        icon: 'error',
        title: 'Error al crear el cliente',
        text: error.message || 'Ocurrió un error inesperado'
      });
      console.error(error);
    });
  });
});

// Código para manejar el modal de eliminación de cliente

document.addEventListener("DOMContentLoaded", function () {
  const eliminarBotones = document.querySelectorAll(".eliminar-btn");

  eliminarBotones.forEach(btn => {
    btn.addEventListener("click", function () {
      const clienteId = this.getAttribute("data-id");

      Swal.fire({
        title: '¿Estás seguro de eliminar el cliente seleccionado?',
        text: "¡Esta acción no se puede deshacer!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Sí, eliminar',
        cancelButtonText: 'Cancelar'
      }).then((result) => {
        if (result.isConfirmed) {
          fetch(`/cliente/${clienteId}/`, {
            method: 'DELETE',
            headers: {
              'X-CSRFToken': getCookie('csrftoken')
            }
          })
          .then(response => {
            if (response.status === 204) {
              Swal.fire({
                icon: 'success',
                title: 'Cliente eliminado',
                showConfirmButton: false,
                timer: 2000
              }).then(() => {
                location.reload();
              });
            } else {
              return response.json().then(data => {
                throw new Error(data.message || 'Error al eliminar');
              });
            }
          })
          .catch(error => {
            Swal.fire({
              icon: 'error',
              title: 'Error',
              text: error.message || 'No se pudo eliminar el cliente'
            });
            console.error(error);
          });
        }
      });
    });
  });
});