function onTelegramAuth(user) {
    axios.post('/auth/callback', user);
    const text = document.querySelector('.button_info');
    text.innerHTML = 'Позвать пить пиво &#127866';
    
    const buttons = document.querySelectorAll('.find_button');
    for (let i = 0; i < buttons.length; i++) {
        buttons[i].style.backgroundColor = '#00FF7F';
        buttons[i].style.pointerEvents = "auto";
    }

    const button = document.querySelector('.invite_button');
    button.style.outlineColor = '#00FF7F';
    button.style.pointerEvents = "auto";
}

function onNotify() {
    axios.get('/notify');
}

function showAdditionalInfo() {
    const additional_info = document.querySelector('.additional_info');
    const button = document.querySelector('.invite_button');
    if (additional_info.offsetParent ===  null) 
        additional_info.style.display = 'block';
    else 
        additional_info.style.display = 'none';
}

const users = new Array;
function getUser(user_id) {
    const button = document.querySelector('.user'+user_id);
    if (users.includes(user_id)) {
        users.splice(users.indexOf(user_id), 1);
        button.style.backgroundColor = 'white';
        button.style.color = 'black';
    }
    else {
        users.push(user_id);
        button.style.backgroundColor = '#00FF7F';
        button.style.color = 'white';
    }

}

function returnUsers() {
    const reason = document.querySelector('.reason-of-meeting').value;
    const time = document.querySelector('.time-of-the-meeting').value;
    const address = document.querySelector('.meeting-place').value;
    axios.post('/notify/certain_users', {'users':users,
                                         'reason':reason,
                                         'time':time,
                                         'address':address});

    const status_info = document.getElementById('sending-status');
    status_info.style.display = 'inline-block';
}
