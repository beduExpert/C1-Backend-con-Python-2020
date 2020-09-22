(function($) {

	"use strict"; // Start of use strict
	
	/* Titles Color */
	$('.intro_text, .simple_stat').each(function(){
		var color = $(this).attr('data-color');
		if (color){
			$(this).find('b').css('color', color);	
		}
	});

	

	/* Section Background */
	$('.image_bck').each(function(){
		var image = $(this).attr('data-image');
		var gradient = $(this).attr('data-gradient');
		var color = $(this).attr('data-color');
		var blend = $(this).attr('data-blend');
		var opacity = $(this).attr('data-opacity');
		var position = $(this).attr('data-position');
		if (image){
			$(this).css('background-image', 'url('+image+')');	
		}
		if (gradient){
			$(this).css('background-image', gradient);	
		}
		if (color){
			$(this).css('background-color', color);	
		}
		if (blend){
			$(this).css('background-blend-mode', blend);	
		}
		if (position){
			$(this).css('background-position', position);	
		}
		if (opacity){
			$(this).css('opacity', opacity);	
		}
	});

	/* Bootstrap */
	$('[data-toggle="tooltip"]').tooltip();
	$('[data-toggle="popover"]').popover();
	
	/* Over */
	$('.over, .head_bck').each(function(){
		var color = $(this).attr('data-color');
		var image = $(this).attr('data-image');
		var opacity = $(this).attr('data-opacity');
		var blend = $(this).attr('data-blend');
		if (color){
			$(this).css('background-color', color);	
		}
		if (image){
			$(this).css('background-image', 'url('+image+')');	
		}
		if (opacity){
			$(this).css('opacity', opacity);	
		}
		if (blend){
			$(this).css('mix-blend-mode', blend);	
		}
	});

	/*Increase-Decrease*/
    $('.increase-qty').on("click", function(e){
    	var qtya = $(this).parents('.add-to-cart').find('.qty').val();
    	var qtyb = qtya * 1 + 1;
    	$(this).parents('.add-to-cart').find('#qty').val(qtyb);
		e.preventDefault();
	});
	$('.decrease-qty').on("click", function(e){
    	var qtya = $(this).parents('.add-to-cart').find('#qty').val();
    	var qtyb = qtya * 1 - 1;
    	if (qtyb < 1) {
            qtyb = 1;
        }
    	$(this).parents('.add-to-cart').find('#qty').val(qtyb);
		e.preventDefault();
	});

	

	/*Sub Menu*/
	$('.sub_cont li').on({
		mouseenter:function(){
			$(this).find('.mega_menu').stop().slideDown('fast');
		},
		mouseleave:function(){
			$(this).find('.mega_menu').stop().slideUp('fast');
		}
	});




	if ($(window).width() > 992) {
		$('.row').each(function(){
			setEqualHeight($(this).find('.bordered_block:not(".col-md-12")'));
			setEqualHeight($(this).find('.block'));
		});
	}

	$('.row').each(function(){
		setEqualHeight($(this).find('.bordered_block:not(".col-md-12")'));
		setEqualHeight($(this).find('.block'));
	});


	$(window).resize(function() {

	    if ($(window).width() > 992) {
			$('.row').each(function(){
				setEqualHeight($(this).find('.bordered_block:not(".col-md-12")'));
				setEqualHeight($(this).find('.block'));

			});

		}
		
		$('.row').each(function(){
			setEqualHeight($(this).find('.bordered_block:not(".col-md-12")'));
			setEqualHeight($(this).find('.block'));
		});
		$('.mid_wrapper').each(function(){
			setEqualHeight($(this).find('.owl-item'));
		});

		if($(".intro_wrapper").length) {
			$('.intro_wrapper').data('owlCarousel').reinit();
		}
		if($(".intro_wrapper_no_auto").length) {
			$('.intro_wrapper_no_auto').data('owlCarousel').reinit();
		}

	});
	
	$( ".date_arrival, .date_departure" ).datepicker();


	/*Wow*/
	new WOW(
		{
	      boxClass:'wow', animateClass: 'animated', offset:0, mobile:true, live:true       
	    }
		).init();
	
	/*Gallery Lightbox*/
	$('.lightbox').magnificPopup({ 
	  type: 'image',
	  gallery:{
	    enabled:true
	  }
	});
	$('.video').magnificPopup({
	  type: 'iframe',
	  iframe: {
		  markup: '<div class="mfp-iframe-scaler">'+
		            '<div class="mfp-close"></div>'+
		            '<iframe class="mfp-iframe" frameborder="0" allowfullscreen></iframe>'+
		          '</div>', // HTML markup of popup, `mfp-close` will be replaced by the close button

		  patterns: {
		    youtube: {
		      index: 'youtube.com/', // String that detects type of video (in this case YouTube). Simply via url.indexOf(index).

		      id: 'v=', // String that splits URL in a two parts, second part should be %id%
		      // Or null - full URL will be returned
		      // Or a function that should return %id%, for example:
		      // id: function(url) { return 'parsed id'; } 

		      src: 'http://www.youtube.com/embed/%id%?autoplay=1' // URL that will be set as a source for iframe. 
		    },
		    vimeo: {
		      index: 'vimeo.com/',
		      id: '/',
		      src: 'http://player.vimeo.com/video/%id%?autoplay=1'
		    },
		    gmaps: {
		      index: '//maps.google.',
		      src: '%id%&output=embed'
		    }

		    // you may add here more sources

		  },

		  srcAction: 'iframe_src', // Templating object key. First part defines CSS selector, second attribute. "iframe_src" means: find "iframe" and set attribute "src".
		}  
	  
	});
	
	/* Lettering */
	if ($(window).width() > 992) {
		$("header .logo a b").lettering();
		$("header .logo span").each(function(){
		 	var min = 0;
		 	var max = 50;
		 	var randomNumber = Math.floor(Math.random()*(max-min+1)+min);
		 	$(this).css('transition-delay', '0.'+randomNumber+'s');
		 });
	}

	/* Anchor Scroll */
	$(window).scroll(function(){
		if ($(window).scrollTop() > 100) {
			$(".logo a").trigger('mouseenter');
			$('body').addClass('open');
			
		}
		else {
			$('body').removeClass('open');
			$(".logo a").trigger('mouseover');
			$('.sub_menu a').removeClass('active')
		}
	});

	/* Menu */
	$('.main_menu').on("click", function(e){
		$(this).parents('header').toggleClass('tm');	
	});

	/* Top Menu Click to Section */
	$('.sub_menu').find('a').on("click", function(e){
		$('.sub_menu').find('a').removeClass('active');
		$(this).addClass('active');
		var anchor = $(this);
		if($(this).parents('header').hasClass('white_bck')){
			$('html, body').stop().animate({
				scrollTop: $(anchor.attr('href')).offset().top-58
			}, 1000);
		}else if($(this).parents('header').hasClass('blck_bck')){
			$('html, body').stop().animate({
				scrollTop: $(anchor.attr('href')).offset().top-58
			}, 1000);
		}else{
			$('html, body').stop().animate({
				scrollTop: $(anchor.attr('href')).offset().top
			}, 1000);
		}
		e.preventDefault();
		$(".main_menu").trigger('click');
	});

	/* Search Hover */
	$('.search_btn').on({
		mouseenter:function(){
			$(this).find('.se_cont').toggleClass('active');
		},mouseleave:function(){
			$(this).find('.se_cont').toggleClass('active');
		}
	});

	/* Btns Hover */
	$('.basket_btn').on({
		mouseenter:function(){
			$(this).find('.bask_cont').toggleClass('active');
		},mouseleave:function(){
			$(this).find('.bask_cont').toggleClass('active');
		}
	});
	 

	/*Scroll Effect*/
	$('.intro_down, .go').on("click", function(e){
		var anchor = $(this);
		$('html, body').stop().animate({
			scrollTop: $(anchor.attr('href')).offset().top
		}, 300);
		e.preventDefault();
	});

	/*OWL Carousel in Intro*/
	$(".intro_wrapper").owlCarousel({
 		navigation : true, responsive: true, responsiveRefreshRate : 200, responsiveBaseElement:window, slideSpeed : 200, addClassActive:true,
		paginationSpeed : 200, rewindSpeed : 200, singleItem:true, autoPlay : true, transitionStyle:"fade",
	    afterAction : function(elem){
	      $('.active .tlt').textillate('start')
	    },
		navigationText:['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>']
	});

	/*OWL Carousel in Intro*/
	$(".intro_wrapper_no_auto").owlCarousel({
 		navigation : true, responsive: true, responsiveRefreshRate : 200, responsiveBaseElement:window, slideSpeed : 200, addClassActive:true,
		paginationSpeed : 200, rewindSpeed : 200, singleItem:true, autoPlay : false, transitionStyle:"fade",
	    afterAction : function(elem){
	      $('.active .tlt').textillate('start')
	    },
		navigationText:['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>']
	});

	$(".mac_wrapper").owlCarousel({
 		navigation : true, responsive: true, responsiveRefreshRate : 200, responsiveBaseElement:window, slideSpeed : 200, addClassActive:true,
		paginationSpeed : 200, rewindSpeed : 200, singleItem:true, autoPlay : true, transitionStyle:"fade",
		navigationText:['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>']
	});
	$(".review_single_wrapper").owlCarousel({
 		navigation : true, responsive: true, responsiveRefreshRate : 200, responsiveBaseElement:window, slideSpeed : 200, addClassActive:true,
		paginationSpeed : 200, rewindSpeed : 200, singleItem:true, autoPlay : true,
		navigationText:['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>']
	});
	$(".mid_wrapper").owlCarousel({
 		navigation : true, responsive: true, responsiveRefreshRate : 200, responsiveBaseElement:window, slideSpeed : 200, addClassActive:true,
		paginationSpeed : 200, rewindSpeed : 200,  autoPlay : true, transitionStyle:"fade", items:3, 
		itemsCustom : [
	        [0, 1],
	        [570, 1],
	        [768, 2],
	        [1024, 2],
	        [1200, 3],
	        [1400, 4]
	    ],
		navigationText:['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>']
	});

	$(".menu_wrapper").owlCarousel({
 		navigation : true, responsive: true, responsiveRefreshRate : 200, responsiveBaseElement:window, slideSpeed : 200, addClassActive:true,
		paginationSpeed : 200, rewindSpeed : 200,  autoPlay : false, transitionStyle:"fade", items:4, 
		 itemsMobile : [570,1], itemsTablet: [768,2], itemsDesktopSmall : [1024,2],
		navigationText:['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>']
	});
	$(".film_wrapper").owlCarousel({
 		navigation : true, responsive: true, responsiveRefreshRate : 200, responsiveBaseElement:window, slideSpeed : 200, addClassActive:true,
		paginationSpeed : 200, rewindSpeed : 200,  autoPlay : true, transitionStyle:"fade", items:6, 
		navigationText:['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>']
	});

	$(".mid_wrapper_two").owlCarousel({
 		navigation : true, responsive: true, responsiveRefreshRate : 200, responsiveBaseElement:window, slideSpeed : 200, addClassActive:true,
		paginationSpeed : 200, rewindSpeed : 200, autoPlay : true, transitionStyle:"fade", items:2, 
		itemsMobile : [479,1], itemsTablet: [768,2], itemsDesktopSmall : [1024,2],
		navigationText:['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>']
	});
	/*OWL Carousel in Partners*/
	$(".partners_wrapper").owlCarousel({
 		navigation : true, responsive: true, responsiveRefreshRate : 200, slideSpeed : 200, paginationSpeed : 200, rewindSpeed : 500,
		addClassActive : true, navigationText:['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],
	});


	

	/*Tabs*/
	$('.tabs .tabs-ul a').on("click", function(e){
		var link = $(this).attr('href');
		$(this).parents('.tabs').find('.tabs-ul li').removeClass('active');
		$(this).parents('li').addClass('active');
		$(this).parents('.tabs').find('.tab-pane').removeClass('active in');
		$(this).parents('.tabs').find(link).addClass('active in');
		e.preventDefault();
	});

	/*Progress Bars*/
	$('.progress-bar').each(function(){
		var percent = $(this).attr('aria-valuenow');
		var color= $(this).attr('data-color');
		$(this).css('width',percent+'%');
		$(this).css('background-color',color);
	});

	
	/* Countdown */
	$('.countdown').each(function(){
		var year = $(this).attr('data-year');
		var month = $(this).attr('data-month');
		var day = $(this).attr('data-day');
		$(this).countdown({until: new Date(year,month-1,day)});

	});

	/*Price Filter*/
	$('#price-filter').slider({
        range: true,
        min: 0,
        max: 999,
        values: [100, 700],
        slide: function(event, ui)
        {
            $('#price-filter-value-1').text(ui.values[0]);
            $('#price-filter-value-2').text(ui.values[1]);
            var min = ui.values[0] / 999 * 90;
            var max = ui.values[1] / 999 * 90;
            $('.min-filter').css('left', min + '%');
            $('.max-filter').css('left', max + '%');
        }
    });

	/*Video Background*/
	if($(".player").length) {
		$(".player").YTPlayer();
	}

  
	
})(jQuery);


$(window).load(function(){

	/*Masonry*/
	$('.masonry').masonry({
		itemSelector: '.masonry-item',
	});

	if ($(window).width() > 992) {
		/* Autoheight Init */
		$('.mid_wrapper').each(function(){
			setEqualHeight($(this).find('.owl-item'));
		});
	}
	$('.mid_wrapper').each(function(){
		setEqualHeight($(this).find('.owl-item'));
	});
	
});

 /*Boxes AutoHeight*/
function setEqualHeight(columns)
{
	var tallestcolumn = 0;
	columns.each(
		function()
		{
			$(this).css('height','auto');
			var currentHeight = $(this).height();
			if(currentHeight > tallestcolumn)
				{
				tallestcolumn = currentHeight;
				}
		}
	);
columns.height(tallestcolumn);
}

