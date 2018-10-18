$(window).scroll(function() {
  if($(window).scrollTop() + $(window).height() > $(document).height() - 100) {
    $('.scroll-container').css({'display':'none'})
  }else {
    $('.scroll-container').css({'display':'block'})
  }
});