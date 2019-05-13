var parties = ['BJP', 'INC', 'JDS', 'BSP', 'CPI', 'AAP', 'IND', 'NOTA'];
var cast = document.getElementById('cast');
var candidates = [];
var voted = null;
var setvotelink = '';

for (let i = 0; i < parties.length; i += 1) {
    let canddiv = document.getElementById(`${String(i + 1)}`);
    if (canddiv == null || canddiv == undefined) {
        continue;
    }
    candidates.push({ ob: canddiv, index: i });
}
for (let candidate of candidates) {
    candidate.ob.children[1].src = 'static/images/' + parties[candidate.index] + '.png';
    candidate.ob.children[2].innerHTML = parties[candidate.index];
}

for (let j = 0; j < candidates.length; j++) {
    candidates[j].ob.addEventListener("click", () => {
        console.log(j + ' was clicked!');
        selectCandidate(candidates[j].index, j);
    });
}

function selectCandidate(index, cand_index) {
    if (voted == null) {
        voted = index + 1;
        candidates[cand_index].ob.children[4].style.display = 'block';
        candidates[cand_index].ob.style.borderColor = 'rgb(18, 187, 116)';

        fetch(`/vote/fetch/${voted}`).then((res) => {
            res.json().then((body) => {
            setvotelink = `vote/${body.cand_id}`;
                cast.href = setvotelink;
            });
        });
    }
    else {
        pre = document.getElementById(voted);
        pre.children[4].style.display = 'none';
        pre.style.borderColor = 'rgb(17,17,17)';
        candidates[cand_index].ob.children[4].style.display = 'block';
        candidates[cand_index].ob.style.borderColor = 'rgb(18, 187, 116)';
        voted = index + 1;

        fetch(`/vote/fetch/${voted}`).then((res) => {
            res.json().then((body) => {
                setvotelink = `vote/${body.cand_id}`;
                cast.href = setvotelink;
            });
        });
    }
}
