function like(postid){
    csrf = document.querySelector('[name=csrfmiddlewaretoken]').value
    fetch("/likePost", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            postid: postid,
        }),
        credentials: "same-origin",
        mode: "same-origin",
        headers: {
            "X-CSRFToken": csrf
        }
    }).then((res) => {
        el = document.getElementById("like_"+postid)
        if(el.style.color == "red"){
            el.style.color = "gray"
        }else{
        el.style.color = "red"
        }
       if(res == 200){
        
       }
})
}
