
window.onload = function() {
    var foldBtns = document.getElementsByClassName("fold-button");

    for (var i = 0; i < foldBtns.length; i++) {
        foldBtns[i].onclick = function(event) {
            if (!event) {
                event = window.event;
            }

            if (event.preventDefault) {
                event.preventDefault();
            } else {
                event.returnValue = false;
            }

            var post = this.parentNode;

            if (post.className == "one-post folded") {
                post.className = "one-post";
                this.innerHTML = "свернуть";
            } else {
                post.className = "one-post folded";
                this.innerHTML = "развернуть";
            }

            return false;
        };
    }
};