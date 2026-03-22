$(document).ready(function(){
    $('.logo-image').hover(function(){
        $(this).animate({
            width: '280px'
        }, 300);
    }, function(){
        $(this).animate({
            width: '260px'
        }, 300);
    });
});