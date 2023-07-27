document.addEventListener('DOMContentLoaded', function() {
    const togglePassword = document.querySelector('#togglePassword');
    const toggleConfirmPassword = document.querySelector('#toggleConfirmPassword');
    const password = document.querySelector('#password');
    const confirmPassword = document.querySelector('#confirm_password');

    togglePassword.addEventListener('click', function (e) {
        // toggle the type attribute
        const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
        password.setAttribute('type', type);
        // toggle the eye slash icon
        this.classList.toggle('fa-eye-slash');
        this.classList.toggle('fa-eye');
    });

    toggleConfirmPassword.addEventListener('click', function (e) {
        // toggle the type attribute
        const confirmType = confirmPassword.getAttribute('type') === 'password' ? 'text' : 'password';
        confirmPassword.setAttribute('type', confirmType);
        // toggle the eye slash icon
        this.classList.toggle('fa-eye-slash');
        this.classList.toggle('fa-eye');
    });
});