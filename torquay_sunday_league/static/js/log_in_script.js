document.addEventListener('DOMContentLoaded', function () {
    // This code sets the inputs to empty strings
    document.getElementById('username').value = "";
    document.getElementById('password').value = "";

    // This code makes the eye toggles function to reveal passwords
    const togglePassword = document.querySelector('#togglePassword');
    const password = document.querySelector('#password');

    togglePassword.addEventListener('click', function (e) {
        // toggle the type attribute
        const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
        password.setAttribute('type', type);
        // toggle the eye slash icon
        this.classList.toggle('fa-eye-slash');
        this.classList.toggle('fa-eye');
    });
});