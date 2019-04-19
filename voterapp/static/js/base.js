var flashbox = document.getElementsByClassName('flashbox')[0];
var close = document.getElementsByTagName('h6')[0];
close.addEventListener("click", () => {
    flashbox.classList.add('toggle-flashbox');
    setTimeout(() => {
        flashbox.style.display = 'none';
    }, 300);
});
            
window.setTimeout(() => {
    flashbox.classList.add('toggle-flashbox');
    setTimeout(() => {
        flashbox.style.display = 'none';
    }, 300);
}, 5000);
