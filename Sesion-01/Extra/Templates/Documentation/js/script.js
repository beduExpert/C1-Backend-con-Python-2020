$(function(){
	SyntaxHighlighter.all();
	$('.left_menu').find('a').on("click", function(e){
	  $('.left_menu').find('a').removeClass('active');
	  $(this).addClass('active');
      var anchor = $(this);
      $('html, body').stop().animate({
         scrollTop: $(anchor.attr('href')).offset().top -30
      }, 700);
      e.preventDefault();
    });
});
