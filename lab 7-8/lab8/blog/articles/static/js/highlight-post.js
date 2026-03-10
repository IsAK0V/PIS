// Лабораторная работа №8 — jQuery: подсветка поста + эффект логотипа

$(document).ready(function() {

    // ── Подсветка поста при наведении ──────────────────────────────────────
    $('.one-post').hover(
        function(event) {
            // При наведении: opacity .one-post-shadow → 0.1 за 300 мс
            $(event.currentTarget)
                .find('.one-post-shadow')
                .animate({ opacity: '0.1' }, 300);
        },
        function(event) {
            // При уходе курсора: opacity → 0 за 300 мс
            $(event.currentTarget)
                .find('.one-post-shadow')
                .animate({ opacity: '0' }, 300);
        }
    );

    // ── Задание: увеличение логотипа при наведении ─────────────────────────
    // Сохраняем оригинальные размеры после загрузки
    var $logo     = $('.header img');
    var origW     = $logo.width();
    var origH     = $logo.height();

    $logo.hover(
        function() {
            // Ширина +20px, высота пропорционально
            var newW = origW + 20;
            var newH = Math.round(origH * (newW / origW));
            $(this).animate({ width: newW + 'px', height: newH + 'px' }, 300);
        },
        function() {
            // Возврат к исходным размерам
            $(this).animate({ width: origW + 'px', height: origH + 'px' }, 300);
        }
    );

});
