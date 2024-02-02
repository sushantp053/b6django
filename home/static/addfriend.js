
function addFriend(id){
    csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    fetch('/addFriend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(
            {
            'id': id
            }
        ),
        credentials: 'same-origin',
        mode: 'same-origin',
        headers: {
            'X-CSRFToken': csrftoken
        }
        })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        document.getElementById('nf_'+id).remove();
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}