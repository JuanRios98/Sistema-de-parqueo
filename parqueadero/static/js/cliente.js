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
      const tipoPlan = this.dataset.plan;
      const fechaInicio = this.dataset.inicio;
      const fechaFin = this.dataset.fin;

     document.getElementById("edit-id-view").value = clienteId;

      document.getElementById("edit-id").value = clienteId;
      document.getElementById("edit-tipo-plan").value = tipoPlan;
      document.getElementById("edit-inicio").value = fechaInicio;
      document.getElementById("edit-fin").value = fechaFin || '';

      // const modal = new bootstrap.Modal(document.getElementById("editarModal"));
      // modal.show();
      // modalElement.focus(); // Focalizar el modal al abrirlo

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
    const tipoPlan = document.getElementById("edit-tipo-plan").value;
    const fechaInicio = document.getElementById("edit-inicio").value;
    const fechaFin = document.getElementById("edit-fin").value || null;

    // Verificación de que los campos no estén vacíos
    if (!tipoPlan || !fechaInicio) {
      alert('Por favor, complete todos los campos');
      return;
    }

    fetch(`/cliente/${clienteId}/`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')  // ✅ aquí ya funciona si está definida arriba
      },
      body: JSON.stringify({
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
      alert('Cliente actualizado con éxito');
      location.reload();
    })
    .catch(error => {
      alert('Hubo un error al actualizar el cliente');
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
  document.getElementById("crearForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const tipoPlan = document.getElementById("nuevo-tipo-plan").value;
    const fechaInicio = document.getElementById("nuevo-inicio").value;
    const fechaFin = document.getElementById("nuevo-fin").value || null;

    console.log("Datos del formulario:", tipoPlan, fechaInicio, fechaFin);

    fetch('/cliente/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')  // ✅ aquí ya funciona si está definida arriba
      },
      body: JSON.stringify({
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
      alert('✅ Cliente creado con éxito');
      location.reload();
    })
    .catch(error => {
      alert('🚨 Error al crear el cliente');
      console.error(error);
    });
  });
});