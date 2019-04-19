var quotes = [
    {name: 'Bernard Baruch', quote: 'Vote for the man who promises the least, he\'ll be the least disappointing.'},
    {name: 'Paul Wellstone', quote: 'The only way to change is to vote. People are responsible.'},
    {name: 'Louis L\'Amour', quote: 'To make democracy work, we must be a nation of participants, not simply observers. One who does not vote has no right to complain.'},
    {name: 'John Quincy Adams', quote: 'Always vote for principle, though you may vote alone, and you will cherish the sweetest reflection that your vote is never lost.'}
];
var count = 1;
let quote = document.getElementById('quote');
let name = document.getElementById('name');

quote.innerHTML = quotes[0].quote;
name.innerHTML = '&hyphen; ' + quotes[0].name;

var a = setInterval(changeQuote, 5000);

function changeQuote(){
    if(count > 3){
        count = 0;
    }
    quote.innerHTML = quotes[count].quote;
    name.innerHTML = '&hyphen; ' + quotes[count].name;
    count += 1;
}

flashbox = document.getElementsByClassName('flashbox')[0];
close = document.getElementsByTagName('h6')[0];
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
