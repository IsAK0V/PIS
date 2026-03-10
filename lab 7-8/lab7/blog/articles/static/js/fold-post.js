// Лабораторная работа №7 — сворачивание постов
// Задание: реализация через CSS-классы (элегантный вариант)

var foldBtns = document.getElementsByClassName('fold-button');

for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener('click', function(e) {
        // Структура: .fold-button → .post-managment → .one-post
        var onePost = e.target.parentElement.parentElement;

        if (onePost.className.indexOf('folded') !== -1) {
            // Уже свёрнут — разворачиваем
            onePost.className = 'one-post';
            e.target.innerHTML = 'Свернуть';
        } else {
            // Разворочен — сворачиваем
            onePost.className = 'one-post folded';
            e.target.innerHTML = 'Развернуть';
        }
        // CSS делает остальное:
        // .one-post.folded .article-info { display: none; }
        // .one-post.folded .article-text { display: none; }
    });
}
