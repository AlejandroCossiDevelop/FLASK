let isDarkMode = true;

document.getElementById('cambiarTema').addEventListener('click', function() {
    if (isDarkMode) {
        document.body.style.backgroundImage = "url('../static/img/fondo-blanco.jpg')";
        document.querySelector('.bg-footer').style.backgroundColor = "#f5f5f5e3"; 
        document.querySelector('.navbar').style.backgroundColor = "#f5f5f5e3";
        document.querySelectorAll('.navbar .nav-link').forEach(function(element) {
            element.style.color = '#000000';
        });

        document.querySelectorAll('.modal-content').forEach(function(modal) {
            modal.classList.remove('bg-dark', 'text-white'); 
            modal.classList.add('bg-light', 'text-dark'); 
        });

        document.querySelectorAll('.bg-footer h3, .bg-footer p, .bg-footer a').forEach(function(element) {
            element.style.setProperty('color', '#000000'); 
        });

        this.style.backgroundColor = "transparent";
        this.style.color = "#fff";
        this.innerText = "Cambiar a oscuro";

        document.querySelector('table').classList.remove('table-dark');
        document.querySelector('table').classList.add('table-white');
    } else {
        document.body.style.backgroundImage = "url('../static/img/fondo-negro.jpg')";
        document.querySelector('.bg-footer').style.backgroundColor = ""; 
        document.querySelector('.bg-footer').style.setProperty('color', '#fff'); 
        
        document.querySelectorAll('.navbar .nav-link').forEach(function(element) {
            element.style.color = '#fff';
        });

        document.querySelectorAll('.modal-content').forEach(function(modal) {
            modal.classList.remove('bg-light', 'text-dark');  
            modal.classList.add('bg-dark', 'text-white');     
        });

        document.querySelectorAll('.bg-footer h3, .bg-footer p, .bg-footer a').forEach(function(element) {
            element.style.setProperty('color', '#fff'); 
        });

        this.style.backgroundColor = "transparent"; 
        this.style.color = "#fff";
        this.innerText = "Cambiar a claro"; 

        document.querySelector('table').classList.remove('table-white');
        document.querySelector('table').classList.add('table-dark');
    }

    isDarkMode = !isDarkMode;
});
