var foldBtns = document.getElementsByClassName("fold-button");

for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(event) {
        event.preventDefault();

        var post = event.target.parentElement;

        if (post.className == "one-post folded") {
            post.className = "one-post";
            event.target.innerHTML = "свернуть";
        } else {
            post.className = "one-post folded";
            event.target.innerHTML = "развернуть";
        }
    });
}