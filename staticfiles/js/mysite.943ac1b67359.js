$(window).scroll(function() {
  if($(window).scrollTop() + $(window).height() > $(document).height() - 100) {
    $('.scroll-container').css({'display':'none'});
    $('#myBtnTop').css({'display':'block'});
  }else {
    $('.scroll-container').css({'display':'block'});
    $('#myBtnTop').css({'display':'none'});
  }
});
function goTopFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}