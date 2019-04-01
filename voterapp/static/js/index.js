login = document.getElementsByClassName('login')[0];
register = document.getElementsByClassName('register')[0];

login.onclick = function() {
    window.location.href = '/auth/login';
};

register.onclick = function() {
    window.location.href = '/auth/register';
};
