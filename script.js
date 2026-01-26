//! flecha hacia el inicio
// document.getElementById('Flecha').addEventListener('click', function() {
//   window.scrollTo({
//       top: 0,
//       behavior: 'smooth'
//   });
// });

document.addEventListener('DOMContentLoaded', function () {
  const flecha = document.getElementById('Flecha');
  const flechaIcono = document.getElementById('flechaIcono');

  flecha.addEventListener('click', function () {
    if (window.scrollY + window.innerHeight >= document.documentElement.scrollHeight) {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    } else {
      window.scrollTo({
        top: document.documentElement.scrollHeight,
        behavior: 'smooth'
      });
    }
  });

  window.addEventListener('scroll', function () {
    if (window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 50) {
      flechaIcono.innerHTML = "<i class='fas fa-angle-double-up'></i>";
    } else {
      flechaIcono.innerHTML = "<i class='fas fa-angle-double-down'></i>";
    }
  });
});

// !el tema con localStorage
const themeToggle = document.getElementById('themeToggle');
const body = document.body;

// Cargar tema guardado
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'light') {
  body.classList.add('light');
}

// Toggle tema y guardar preferencia
themeToggle.addEventListener('click', function () {
  body.classList.toggle('light');
  const isLight = body.classList.contains('light');
  localStorage.setItem('theme', isLight ? 'light' : 'dark');
});

// Actualizar año en el footer
document.addEventListener('DOMContentLoaded', function () {
  const yearElement = document.getElementById('year');
  if (yearElement) {
    yearElement.textContent = new Date().getFullYear();
  }
});

// Smooth scroll para enlaces internos
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const targetId = this.getAttribute('href');
    if (targetId !== '#') {
      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        // Solo hacer smooth scroll si no es un enlace de navegación principal
        // Los enlaces de navegación ya tienen su propia lógica
      }
    }
  });
});


//!------------seccion

// Función para mostrar la sección correspondiente al hacer clic en el menú
function mostrarSeccion(event) {
  event.preventDefault(); // Evitar que el enlace redirija a otra página
  var seccionId = this.getAttribute('href').substring(1); // Obtener el ID de la sección
  // Ocultar todas las secciones
  document.querySelectorAll('section').forEach(function (seccion) {
    seccion.style.display = 'none';
  });
  // Mostrar la sección seleccionada
  document.getElementById(seccionId).style.display = 'block';
}

// Mostrar la sección correspondiente a Alimentar por defecto al cargar la página
window.onload = function () {
  // Ocultar todas las secciones al cargar la página
  document.querySelectorAll('section').forEach(function (seccion) {
    seccion.style.display = 'none';
  });

  // Mostrar la sección correspondiente según el hashtag en la URL al cargar la página
  var hash = window.location.hash.substring(1); // Obtener el hashtag de la URL
  if (hash && document.getElementById(hash)) {
    document.getElementById(hash).style.display = 'block'; // Mostrar la sección correspondiente al hash
    document.querySelector(`#menu a[href="#${hash}"]`).parentElement.click(); // Simular clic en el elemento del menú correspondiente
  } else {
    document.getElementById('feed').style.display = 'block'; // Mostrar la sección Alimentar por defecto
  }

  // Ocultar las secciones Acerca de, Contenido, y Escribiendo si no están en el hash
  if (!hash || hash !== 'about') {
    document.getElementById('about').style.display = 'none';
  }
  if (!hash || hash !== 'content') {
    document.getElementById('content').style.display = 'none';
  }
  if (!hash || hash !== 'guestbook') {
    document.getElementById('guestbook').style.display = 'none';
  }

  // Agregar evento de clic a todos los elementos <a> del menú
  document.querySelectorAll('#menu a').forEach(function (enlace) {
    enlace.addEventListener('click', mostrarSeccion);
  });

  // Agregar evento de clic al enlace "Ver más"
  document.getElementById('ver-mas').addEventListener('click', function (event) {
    mostrarSeccion.call(this, event);
    document.querySelector('#menu a[href="#about"]').parentElement.click();
  });
};

// ! OTRO DEL MENU
document.querySelectorAll(".nav-item").forEach(item => {
  item.addEventListener("click", function () {
    document.querySelectorAll(".nav-item").forEach(nav => nav.classList.remove("active"));
    this.classList.add("active");
  });
});



// !para la linea de menu
document.addEventListener("DOMContentLoaded", function () {
  const menuItems = document.querySelectorAll("#menu li");
  const underline = document.querySelector(".underline");

  menuItems.forEach(item => {
    item.addEventListener("click", function () {
      menuItems.forEach(item => item.classList.remove("active"));
      this.classList.add("active");

      // Usar offsetLeft para posicionar relativo al contenedor padre
      underline.style.display = "block";
      underline.style.width = this.offsetWidth + "px";
      underline.style.left = this.offsetLeft + "px";
    });
  });

  // Por defecto, activa el primer elemento "Alimentar"
  menuItems[0].click();
});



// ! Reacciones de corazón manejadas por CSS checkbox

// !para el fomulario
document.addEventListener("DOMContentLoaded", function () {
  const commentForm = document.getElementById("commentForm");
  const commentList = document.getElementById("commentList");

  commentForm.addEventListener("submit", function (event) {
    event.preventDefault(); // Evita que se recargue la página al enviar el formulario

    const commentInput = commentForm.querySelector("textarea[name='comment']");
    const commentText = commentInput.value.trim();

    if (commentText) {
      // Crea un nuevo elemento <p> para mostrar el comentario
      const commentElement = document.createElement("p");
      commentElement.textContent = commentText;

      // Agrega el comentario al DOM
      commentList.appendChild(commentElement);

      // Limpia el campo de comentario después de enviar
      commentInput.value = "";
    }
  });
});

// !para la parte de contenido



//!para la actualizacion del año
// Obtiene el elemento con el id "year"
//const yearElement = document.getElementById("year");
// Obtiene el año actual utilizando JavaScript
//const currentYear = new Date().getFullYear();
// Actualiza el contenido del elemento con el año actual
//yearElement.textContent = currentYear;
// Obtiene el elemento con el id "copyrightYear"
//const copyrightYearElement = document.getElementById("copyrightYear");
// Actualiza el contenido del elemento con "Copyright" y el año
// copyrightYearElement.textContent = "Copyright ${currentYear}";

//! ========== EFECTO PARALLAX 3D ==========
document.addEventListener('DOMContentLoaded', function () {
  const parallaxContainer = document.getElementById('parallax-container');
  const parallaxImg = document.getElementById('parallax-img');

  if (parallaxContainer && parallaxImg) {
    // Intensidad del movimiento (ajustar para más o menos efecto)
    const intensity = 20;

    parallaxContainer.addEventListener('mousemove', function (e) {
      const rect = parallaxContainer.getBoundingClientRect();

      // Calcular posición del mouse relativa al centro del contenedor
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      const mouseX = e.clientX - rect.left;
      const mouseY = e.clientY - rect.top;

      // Calcular desplazamiento (-1 a 1)
      const deltaX = (mouseX - centerX) / centerX;
      const deltaY = (mouseY - centerY) / centerY;

      // Aplicar transformación
      const translateX = deltaX * intensity;
      const translateY = deltaY * intensity;
      const rotateY = deltaX * 5; // Rotación sutil en Y
      const rotateX = -deltaY * 5; // Rotación sutil en X

      parallaxImg.style.transform = `
        translate(${translateX}px, ${translateY}px) 
        rotateX(${rotateX}deg) 
        rotateY(${rotateY}deg) 
        scale(1.05)
      `;
    });

    // Resetear cuando el mouse sale
    parallaxContainer.addEventListener('mouseleave', function () {
      parallaxImg.style.transform = 'translate(0, 0) rotateX(0) rotateY(0) scale(1)';
    });
  }
});
