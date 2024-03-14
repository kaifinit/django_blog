(function () {

	'use strict'


	AOS.init({
		duration: 800,
		easing: 'slide',
		once: true
	});

	var preloader = function() {

		var loader = document.querySelector('.loader');
		var overlay = document.getElementById('overlayer');

		function fadeOut(el) {
			el.style.opacity = 1;
			(function fade() {
				if ((el.style.opacity -= .1) < 0) {
					el.style.display = "none";
				} else {
					requestAnimationFrame(fade);
				}
			})();
		};

		setTimeout(function() {
			fadeOut(loader);
			fadeOut(overlay);
		}, 200);
	};
	preloader();

	var tinyslider = function() {

		var slider = document.querySelectorAll('.features-slider');
		var postSlider = document.querySelectorAll('.post-slider');
		var testimonialSlider = document.querySelectorAll('.testimonial-slider');
		
		
		
		if ( slider.length> 0 ) {
			var tnsSlider = tns({
				container: '.features-slider',
				mode: 'carousel',
				speed: 700,
				items: 3,
				// center: true,
				gutter: 30,
				loop: false,
				edgePadding: 80,
				controlsPosition: 'bottom',
				// navPosition: 'bottom',
				nav: false,
				// autoplay: true,
				// autoplayButtonOutput: false,
				controlsContainer: '#features-slider-nav',
				responsive: {
					0: {
						items: 1
					},
					700: {
						items: 2
					},
					900: {
						items: 3
					}
				}
			});
		}

		if ( postSlider.length> 0 ) {
			var tnsPostSlider = tns({
				container: '.post-slider',
				mode: 'carousel',
				speed: 700,
				items: 3,
				// center: true,
				gutter: 30,
				loop: true,
				edgePadding: 10,
				controlsPosition: 'bottom',
				navPosition: 'bottom',
				nav: true,
				autoplay: true,
				autoplayButtonOutput: false,
				controlsContainer: '#post-slider-nav',
				responsive: {
					0: {
						items: 1
					},
					700: {
						items: 2
					},
					900: {
						items: 3
					}
				}
			});
		}

		if ( testimonialSlider.length> 0 ) {
			var tnsTestimonialSlider = tns({
				container: '.testimonial-slider',
				mode: 'carousel',
				speed: 700,
				items: 1,
				// center: true,
				gutter: 30,
				loop: true,
				edgePadding: 10,
				controlsPosition: 'bottom',
				navPosition: 'bottom',
				nav: true,
				autoplay: true,
				autoplayButtonOutput: false,
				controlsContainer: '#testimonial-slider-nav',
				controls: false,
				responsive: {
					0: {
						items: 1
					},
					700: {
						items: 1
					},
					900: {
						items: 1
					}
				}
			});
		}

		
	}
	tinyslider();

	var lightboxVideo = GLightbox({
		selector: '.glightbox'
	});


})()