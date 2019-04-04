vs = document.getElementsByClassName('vs')[0];
span = document.getElementsByClassName('status')[0];
fontawesome = document.getElementById('vs');

if(vs.innerHTML == 'None'){
    span.style.backgroundColor = 'rgba(219,17,17,1)';
    fontawesome.classList.remove('fa-check');
    fontawesome.classList.add('fa-times');
}

vote = document.getElementsByClassName('vote')[0];

vote.onclick = function(){
    window.location.href = '/vote';
}