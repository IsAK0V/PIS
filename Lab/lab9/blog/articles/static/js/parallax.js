$(document).ready(function(){
    $(window).scroll(function(){
        var scrollTop = $(window).scrollTop();

        $('.circle-1').css('transform', 'translateY(' + (scrollTop * 0.15) + 'px)');
        $('.circle-2').css('transform', 'translateY(' + (scrollTop * 0.25) + 'px)');
        $('.circle-3').css('transform', 'translateY(' + (scrollTop * 0.35) + 'px)');
        $('.circle-4').css('transform', 'translateY(' + (scrollTop * 0.45) + 'px)');
    });
});