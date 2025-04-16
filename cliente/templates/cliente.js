document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".bi-pencil-square").forEach(boton => {
      boton.addEventListener("click", function () {
        // Obtener los datos del cliente desde los atributos data-* del ícono
        const clienteId = this.dataset.id;
        const tipoPlan = this.dataset.plan;
        const fechaInicio = this.dataset.inicio;
        const fechaFin = this.dataset.fin;
  
        // Cargar los datos en el formulario del modal
        document.getElementById("edit-id").value = clienteId;  // El ID se guarda en un campo oculto
        document.getElementById("edit-tipo-plan").value = tipoPlan;
        document.getElementById("edit-inicio").value = fechaInicio;
        document.getElementById("edit-fin").value = fechaFin || '';  // Si fecha_fin es indefinido, dejarlo vacío
  
        // Mostrar el modal
        const modal = new bootstrap.Modal(document.getElementById("editarModal"));
        modal.show();
      });
    });
  
    // Al enviar el formulario, hacer una solicitud PUT
    document.getElementById("editarForm").addEventListener("submit", function (e) {
      e.preventDefault();  // Evitar el comportamiento por defecto del formulario
  
      const clienteId = document.getElementById("edit-id").value;
      const tipoPlan = document.getElementById("edit-tipo-plan").value;
      const fechaInicio = document.getElementById("edit-inicio").value;
      const fechaFin = document.getElementById("edit-fin").value || null;
  
      // Enviar una solicitud PUT a la API
      fetch(`/api/clientes/${clienteId}/`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          tipo_plan: tipoPlan,
          fecha_inicio: fechaInicio,
          fecha_fin: fechaFin
        })
      })
      .then(response => response.json())
      .then(data => {
        if (data) {
          alert('Cliente actualizado con éxito');
          location.reload(); // Recargar la página para reflejar los cambios
        }
      })
      .catch(error => {
        alert('Hubo un error al actualizar el cliente');
        console.error(error);
      });
    });
  });