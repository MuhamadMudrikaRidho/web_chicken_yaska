(function ($) {
  "use strict";

  //preloader
  $(window).on('load', function () {
    $("#rts__preloader").delay(0).fadeOut(1000);
  })
  $(window).on('load', function () {
    $("#weiboo-load").delay(0).fadeOut(1000);
  })

  // Common-slider
  var swiper = new Swiper(".rts-cmmnSlider", {
    slidesPerView: 4,
    spaceBetween: 30,
    slidesPerGroup: 1,
    speed: 1500,
    loop: true,
    loopFillGroupWithBlank: true,
    centeredSlides: false,
    breakpoints: {
      1200: {
        slidesPerView: 4,
      },
      900: {
        slidesPerView: 3,
      },
      768: {
        slidesPerView: 3,
      },
      580: {
        slidesPerView: 2,
      },
      0: {
        slidesPerView: 1,
      }
    },
    autoplay: {
      delay: 2500,
      disableOnInteraction: false
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    pagination: {
      el: ".swiper-pag",
      clickable: true,
    }
  });
  // Common-slider-over
  var swiper = new Swiper(".rts-cmmnSlider-over", {
    slidesPerView: 4,
    spaceBetween: 30,
    slidesPerGroup: 2,
    speed: 1500,
    loop: true,
    loopFillGroupWithBlank: true,
    centeredSlides: false,
    breakpoints: {
      1600: {
        slidesPerView: 4,
      },
      1300: {
        slidesPerView: 4,
      },
      1220: {
        slidesPerView: 4,
      },
      1200: {
        slidesPerView: 3,
      },
      900: {
        slidesPerView: 3,
      },
      768: {
        slidesPerView: 2,
      },
      633: {
        slidesPerView: 2,
      },
      500: {
        slidesPerView: 1,
      },
      0: {
        slidesPerView: 1,
      }
    },
    autoplay: {
      delay: 2500,
      disableOnInteraction: true
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    pagination: {
      el: ".swiper-pag",
      clickable: true,
    }
  });
  // Common-slider-over
  var swiper = new Swiper(".rts-cmmnSlider-over2", {
    slidesPerView: 4,
    spaceBetween: 30,
    slidesPerGroup: 1,
    speed: 1500,
    loop: true,
    loopFillGroupWithBlank: true,
    centeredSlides: false,
    breakpoints: {
      1600: {
        slidesPerView: 5,
      },
      1300: {
        slidesPerView: 5.6,
      },
      1220: {
        slidesPerView: 5,
      },
      1200: {
        slidesPerView: 4.5,
      },
      900: {
        slidesPerView: 3,
      },
      768: {
        slidesPerView: 2,
      },
      633: {
        slidesPerView: 2,
      },
      500: {
        slidesPerView: 1,
      },
      0: {
        slidesPerView: 1,
      }
    },
    autoplay: {
      delay: 2500,
      disableOnInteraction: true
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    pagination: {
      el: ".swiper-pag",
      clickable: true,
    }
  });
  // Common-slider-over
  var swiper = new Swiper(".rts-cmmnSlider-over3", {
    slidesPerView: 3,
    spaceBetween: 30,
    slidesPerGroup: 1,
    speed: 1500,
    loop: true,
    loopFillGroupWithBlank: true,
    centeredSlides: false,
    breakpoints: {
      1600: {
        slidesPerView: 3,
      },
      1300: {
        slidesPerView: 3,
      },
      1220: {
        slidesPerView: 3,
      },
      1200: {
        slidesPerView: 3,
      },
      900: {
        slidesPerView: 2,
      },
      576: {
        slidesPerView: 2,
      },
      0: {
        slidesPerView: 1,
      }
    },
    autoplay: {
      delay: 2500,
      disableOnInteraction: true
    },
    navigation: {
      prevEl: ".swiper-button-prev",
      nextEl: ".swiper-button-next",
    },
    pagination: {
      el: ".swiper-pag",
      clickable: true,
    }
  });
  // Common-slider-over
  var swiper = new Swiper(".rts-fiveSlide", {
    slidesPerView: 5,
    spaceBetween: 10,
    slidesPerGroup: 1,
    speed: 1500,
    loop: true,
    loopFillGroupWithBlank: true,
    centeredSlides: false,
    breakpoints: {
      1600: {
        slidesPerView: 5,
      },
      1300: {
        slidesPerView: 5,
      },
      1220: {
        slidesPerView: 5,
      },
      1200: {
        slidesPerView: 4,
      },
      900: {
        slidesPerView: 3,
      },
      768: {
        slidesPerView: 3,
      },
      633: {
        slidesPerView: 3,
      },
      500: {
        slidesPerView: 2,
      },
      0: {
        slidesPerView: 1,
      }
    },
    autoplay: {
      delay: 2500,
      disableOnInteraction: true
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    pagination: {
      el: ".swiper-pag",
      clickable: true,
    }
  });
  // Common-slider-over
  var swiper = new Swiper(".rts-sixSlide-over", {
    slidesPerView: 4,
    spaceBetween: 30,
    slidesPerGroup: 1,
    speed: 1500,
    loop: true,
    loopFillGroupWithBlank: true,
    centeredSlides: false,
    breakpoints: {
      1600: {
        slidesPerView: 5,
      },
      1300: {
        slidesPerView: 5.6,
      },
      1220: {
        slidesPerView: 5,
      },
      1200: {
        slidesPerView: 4.5,
      },
      900: {
        slidesPerView: 3,
      },
      768: {
        slidesPerView: 3,
      },
      633: {
        slidesPerView: 3,
      },
      500: {
        slidesPerView: 2,
      },
      0: {
        slidesPerView: 1,
      }
    },
    autoplay: {
      delay: 2500,
      disableOnInteraction: true
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    pagination: {
      el: ".swiper-pag",
      clickable: true,
    }
  });
  // Common-slider-over
  var swiper = new Swiper(".rts-brandSlide1", {
    slidesPerView: 4,
    spaceBetween: 30,
    slidesPerGroup: 1,
    speed: 1500,
    loop: true,
    loopFillGroupWithBlank: true,
    centeredSlides: false,
    breakpoints: {
      1600: {
        slidesPerView: 6,
      },
      1300: {
        slidesPerView: 6,
      },
      1220: {
        slidesPerView: 5,
      },
      1200: {
        slidesPerView: 5,
      },
      900: {
        slidesPerView: 4,
      },
      768: {
        slidesPerView: 3,
      },
      633: {
        slidesPerView: 3,
      },
      500: {
        slidesPerView: 2,
      },
      0: {
        slidesPerView: 1,
      }
    },
    autoplay: {
      delay: 2500,
      disableOnInteraction: true
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    pagination: {
      el: ".swiper-pag",
      clickable: true,
    }
  });
  // Common-slider-over
  var swiper = new Swiper(".rts-topSlide1", {
    slidesPerView: 3,
    spaceBetween: 0,
    slidesPerGroup: 1,
    speed: 700,
    loop: false,
    loopFillGroupWithBlank: false,
    autoplay: {
      delay: 3000,
      disableOnInteraction: true
    },
    centeredSlides: false,
    breakpoints: {
      1500: {
        slidesPerView: 1,
      },
      991: {
        slidesPerView: 1,
      },
      767: {
        slidesPerView: 1,
      },
      575: {
        slidesPerView: 1,
      },
      0: {
        slidesPerView: 1,
      }
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    }
  });
  var swiper = new Swiper(".rts-topSlide2", {
    slidesPerView: 4,
    spaceBetween: 30,
    slidesPerGroup: 1,
    speed: 1500,
    loop: false,
    autoplay: false,
    loopFillGroupWithBlank: true,
    centeredSlides: false,
    breakpoints: {
      1600: {
        slidesPerView: 1,
      },
      1300: {
        slidesPerView: 1,
      },
      1220: {
        slidesPerView: 1,
      },
      1200: {
        slidesPerView: 1,
      },
      900: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 1,
      },
      633: {
        slidesPerView: 1,
      },
      500: {
        slidesPerView: 1,
      },
      0: {
        slidesPerView: 1,
      }
    },
    autoplay: {
      delay: 2500,
      disableOnInteraction: true
    },
    pagination: {
      el: ".swiper-pag",
      clickable: true,
    }
  });


  // feature-slider
  var swiper = new Swiper(".rts-featureSlider", {
    slidesPerView: 4,
    spaceBetween: 30,
    slidesPerGroup: 1,
    speed: 1500,
    loop: true,
    loopFillGroupWithBlank: true,
    centeredSlides: false,
    breakpoints: {
      1200: {
        slidesPerView: 4,
      },
      1093: {
        slidesPerView: 4,
        spaceBetween: 0,
      },
      991: {
        slidesPerView: 4,
        spaceBetween: 10,
      },
      800: {
        slidesPerView: 3,
      },
      575: {
        slidesPerView: 2,
        spaceBetween: 0,

      },
      520: {
        slidesPerView: 2,
        spaceBetween: 10,

      },
      0: {
        slidesPerView: 1,
        spaceBetween: 0,
      }
    },
    autoplay: {
      delay: 25000,
      disableOnInteraction: false
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    pagination: {
      el: ".swiper-pag",
      clickable: true,
    }
  });
  // three-slider
  var swiper = new Swiper(".rts-threeSlider", {
    slidesPerView: 3,
    spaceBetween: 0,
    slidesPerGroup: 1,
    speed: 1500,
    loop: true,
    loopFillGroupWithBlank: true,
    centeredSlides: false,

    breakpoints: {
      1500: {
        slidesPerView: 3,
      },
      1200: {
        slidesPerView: 3,
      },
      991: {
        slidesPerView: 2,
      },
      880: {
        slidesPerView: 2,
      },
      575: {
        slidesPerView: 1,
      },
      0: {
        slidesPerView: 1,
      }
    },
    autoplay: {
      delay: 2500,
      disableOnInteraction: false
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    pagination: {
      el: ".swiper-pag",
      clickable: true,
    }
  });

  /* magnificPopup video view */
  $('.popup-videos').magnificPopup({
    type: 'iframe'
  });

  // One Group slider
  var swiper = new Swiper(".rts-oneGroupSlider", {
    slidesPerView: 1,
    spaceBetween: 0,
    slidesPerGroup: 1,
    speed: 1500,
    loop: true,
    loopFillGroupWithBlank: true,
    centeredSlides: false,
    breakpoints: {
      1500: {
        slidesPerView: 1,
      },
      991: {
        slidesPerView: 1,
      },
      767: {
        slidesPerView: 1,
      },
      575: {
        slidesPerView: 1,
      },
      0: {
        slidesPerView: 1,
      }
    },
    pagination: {
      el: ".swiper-pag",
      clickable: true,
    }
  });

  // banner slider
  var swiper = new Swiper(".bannerSlide", {
    slidesPerView: 3,
    spaceBetween: 0,
    slidesPerGroup: 1,
    speed: 700,
    effect: 'fade',
    loop: false,
    loopFillGroupWithBlank: false,
    autoplay: {
      delay: 3000,
      disableOnInteraction: false
    },
    centeredSlides: false,
    breakpoints: {
      1500: {
        slidesPerView: 1,
      },
      991: {
        slidesPerView: 1,
      },
      767: {
        slidesPerView: 1,
      },
      575: {
        slidesPerView: 1,
      },
      0: {
        slidesPerView: 1,
      }
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    }
  });
  // banner slider
  var swiper = new Swiper(".bannerSlide2", {
    slidesPerView: 1,
    spaceBetween: 0,
    slidesPerGroup: 1,
    speed: 700,
    effect: 'fade',
    loop: false,
    loopFillGroupWithBlank: true,
    autoplay: {
      delay: 3000,
      disableOnInteraction: false
    },
    centeredSlides: false,
    breakpoints: {
      1500: {
        slidesPerView: 1,
      },
      991: {
        slidesPerView: 1,
      },
      767: {
        slidesPerView: 1,
      },
      575: {
        slidesPerView: 1,
      },
      0: {
        slidesPerView: 1,
      }
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    }
  });


  var swiper = new Swiper(".oneSlide", {
    slidesPerView: 1,
    spaceBetween: 30,
    slidesPerGroup: 1,
    speed: 700,
    loop: true,
    loopFillGroupWithBlank: true,
    centeredSlides: false,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    pagination: {
      el: ".swiper-pag",
      clickable: true
    }
  });


  // Testimonial slide
  var menu = ['', '', '', '']
  var swiper = new Swiper(".testimonialSlide", {
    slidesPerView: 5,
    spaceBetween: 10,
    slidesPerGroup: 1,
    speed: 1500,
    loop: true,
    autoplay: true,
    loopFillGroupWithBlank: true,
    centeredSlides: false,
    breakpoints: {
      1500: {
        slidesPerView: 1,
      },
      992: {
        slidesPerView: 1,
      },
      991: {
        slidesPerView: 1,
      },
      600: {
        slidesPerView: 1,
      },
      450: {
        slidesPerView: 1,
      },
      0: {
        slidesPerView: 1,
      }
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
      renderBullet: function (index, className) {
        return '<span class="' + className + '">' + (menu[index]) + '</span>';
      },
    },
  });

  // No gap slide
  var swiper = new Swiper(".noGapSlide", {
    slidesPerView: 5,
    spaceBetween: 10,
    slidesPerGroup: 1,
    speed: 1500,
    loop: true,
    loopFillGroupWithBlank: true,
    centeredSlides: false,
    breakpoints: {
      1500: {
        slidesPerView: 5,
      },
      992: {
        slidesPerView: 4,
      },
      991: {
        slidesPerView: 3,
      },
      600: {
        slidesPerView: 3,
      },
      450: {
        slidesPerView: 2,
      },
      0: {
        slidesPerView: 2,
      }
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true
    }
  });

  // productSlide
  var swiper = new Swiper(".productSlide", {
    slidesPerView: 1,
    slidesPerGroup: 1,
    speed: 500,
    loop: true,
    loopFillGroupWithBlank: true,
    centeredSlides: false,
    navigation: {
      nextEl: ".button-next",
      prevEl: ".button-prev",
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true
    }
  });
  // productSlide2
  var swiper2 = new Swiper(".productSlide2", {
    slidesPerView: 1,
    slidesPerGroup: 1,
    speed: 500,
    loop: true,
    loopFillGroupWithBlank: true,
    centeredSlides: false,
    navigation: {
      nextEl: ".button-next2",
      prevEl: ".button-prev2",
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true
    }
  });
  // productSlide3
  var swiper3 = new Swiper(".productSlide3", {
    slidesPerView: 1,
    slidesPerGroup: 1,
    speed: 500,
    loop: true,
    loopFillGroupWithBlank: true,
    centeredSlides: false,
    navigation: {
      nextEl: ".button-next3",
      prevEl: ".button-prev3",
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true
    }
  });


  var swiperthumb = new Swiper(".productGallerySlideThumb", {
    spaceBetween: 10,
    slidesPerView: 4,
    freeMode: true,
    watchSlidesProgress: true,
  });

  var swiper = new Swiper(".productGallerySlide", {
    spaceBetween: 10,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    thumbs: {
      swiper: swiperthumb,
    },
  });

  var swiperthumb2 = new Swiper(".productGallerySlideThumb2", {
    spaceBetween: 10,
    slidesPerView: 4,
    freeMode: true,
    watchSlidesProgress: true,
  });

  var swiper2 = new Swiper(".productGallerySlide2", {
    spaceBetween: 10,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    thumbs: {
      swiper: swiperthumb2,
    },
  });

  //nice-select
  $(document).ready(function () {
    $('.filters-select').niceSelect();
  });

  // Video Popup
  if ($(".play-video").length) {
    $('.play-video').magnificPopup({
      delegate: 'a',
      type: 'iframe',
      removalDelay: 0,
      callbacks: {
        beforeOpen: function () {
          this.st.image.markup = this.st.image.markup.replace('mfp-figure', 'mfp-figure mfp-with-anim');
          this.st.mainClass = this.st.el.attr('data-effect');
        }
      },
      closeOnContentClick: true,
      midClick: true
    });
  }


  // Search Bar show & hide
  $(document).on('click', '.search-icon', function () {
    $(".search-input-area").addClass("show");
  });
  $(document).on('click', '.search-input-area input', function () {
    $(".search-input-area").addClass("show");
  });
  $(document).on('click', '.search-input-inner before', function () {
    $(".search-input-area").addClass("show");
  });
  $('html').click(function (e) {
    if (!$(e.target).hasClass('show')) {
      $(".search-input-area").removeClass("show");
    }
    $(document).on('click', '.search-close-icon', function () {
      $(".search-input-area").removeClass("show");
    });
  });


  // Cart Bar show & hide
  $(document).on('click', '.cart-icon', function () {
    $(".cart-bar").addClass("show");
    $(".anywere").addClass("bgshow");
  });
  $(document).on('click', '.close-cart', function () {
    $(".cart-bar").removeClass("show");
    $(".anywere").removeClass("bgshow");
  });
  $(document).on('click', '.anywere', function () {
    $(".cart-bar").removeClass("show");
    $(".anywere").removeClass("bgshow");
  });


  $(function () {
    var header = $(".start-style");
    $(window).scroll(function () {
      var scroll = $(window).scrollTop();

      if (scroll >= 10) {
        header.removeClass('start-style').addClass("scroll-on");
      } else {
        header.removeClass("scroll-on").addClass('start-style');
      }
    });
  });

  //Animation
  $(document).ready(function () {
    $('body.hero-anime').removeClass('hero-anime');
  });

  //Menu On Hover
  $('body').on('mouseenter mouseleave', '.nav-item', function (e) {
    if ($(window).width() > 750) {
      var _d = $(e.target).closest('.nav-item');
      _d.addClass('show');
      setTimeout(function () {
        _d[_d.is(':hover') ? 'addClass' : 'removeClass']('show');
      }, 1);
    }
  });
  //Switch light/dark

  $("#switch").on('click', function () {
    if ($("body").hasClass("dark")) {
      $("body").removeClass("dark");
      $("#switch").removeClass("switched");
    } else {
      $("body").addClass("dark");
      $("#switch").addClass("switched");
    }
  });


  // Image popup
  $(document).ready(function () {
    $('.image-popup-vertical-fit').magnificPopup({
      type: 'image',
      mainClass: 'mfp-with-zoom',
      gallery: {
        enabled: true
      },

      zoom: {
        enabled: true,

        duration: 300,
        easing: 'ease-in-out',

        opener: function (openerElement) {

          return openerElement.is('img') ? openerElement : openerElement.find('img');
        }
      }
    });
  });


  // Sidebar open & close
  $('.hamburger').on('click', function () {
    $(".hamburger").toggleClass("active");
  });

  $('.hamburger').on('click', function () {
    $(".slide-bar").toggleClass("show");
    $(".anywere").addClass("bgshow");
    $(".hamburger").addClass("move");
  });

  $('.mobile-hamburger').click('click', function () {
    $(".slide-bar").removeClass("show");
    $(".anywere").removeClass("bgshow");
    $(".hamburger").addClass("move");
  });

  $('.anywere').on('click', function () {
    $(".slide-bar").removeClass("show");
    $(".anywere").removeClass("bgshow");
    $(".hamburger").removeClass("active");
  });

  $('.action-item').on('click', function () {
    $(".slide-bar").removeClass("show");
    $(".anywere").removeClass("bgshow");
    $(".hamburger").removeClass("active");
  });

  $(function () {
    $('.toggle-menu').on('focus', function () {
      $('.rts-menu').toggleClass('display');
    });
  });
  $('.hamburger-1').on('click', function () {
    $(".hamburger-1").toggleClass("active");
  });

  $('.hamburger-1').on('click', function () {
    $(".slide-bar").toggleClass("show");
    $(".anywere").addClass("bgshow");
    $(".hamburger-1").addClass("move");
  });

  $('.mobile-hamburger-1').click('click', function () {
    $(".slide-bar").removeClass("show");
    $(".anywere").removeClass("bgshow");
    $(".hamburger-1").addClass("move");
  });

  $('.anywere').on('click', function () {
    $(".slide-bar").removeClass("show");
    $(".anywere").removeClass("bgshow");
    $(".hamburger-1").removeClass("active");
  });

  $('.action-item').on('click', function () {
    $(".slide-bar").removeClass("show");
    $(".anywere").removeClass("bgshow");
    $(".hamburger-1").removeClass("active");
  });

  $(function () {
    $('.toggle-menu').on('focus', function () {
      $('.rts-menu').toggleClass('display');
    });
  });


  /*------------------------------------
    Mobile Menu
  --------------------------------------*/

  $('#mobile-menu-active').metisMenu();

  $('#mobile-menu-active .has-dropdown > a').on('click', function (e) {
    e.preventDefault();
  });


  $(".hamburger-menu > a").on("click", function (e) {
    e.preventDefault();
    $(".slide-bar").toggleClass("show");
    $("body").addClass("on-side");
    $('.body-overlay').addClass('active');
    $(this).addClass('active');
  });

  /* Search
    -------------------------------------------------------*/
  var $searchWrap = $('.search-wrap');
  var $navSearch = $('.nav-search');
  var $searchClose = $('#search-close');

  $('.search-trigger').on('click', function (e) {
    e.preventDefault();
    $searchWrap.animate({
      opacity: 'toggle'
    }, 500);
    $navSearch.add($searchClose).addClass("open");
  });

  $('.search-close').on('click', function (e) {
    e.preventDefault();
    $searchWrap.animate({
      opacity: 'toggle'
    }, 500);
    $navSearch.add($searchClose).removeClass("open");
  });

  function closeSearch() {
    $searchWrap.fadeOut(200);
    $navSearch.add($searchClose).removeClass("open");
  }

  $(document.body).on('click', function (e) {
    closeSearch();
  });

  $(".search-trigger, .main-search-input").on('click', function (e) {
    e.stopPropagation();
  });


  //sticky-menu
  $(window).on('scroll', function () {
    var scroll = $(window).scrollTop();
    if (scroll < 200) {
      $(".navbar-sticky").removeClass("sticky-menu");
      $(".navbar-sticky-mobile").removeClass("sticky-menu-mobile");
    } else {
      $(".navbar-sticky").addClass("sticky-menu");
      $(".navbar-sticky-mobile").addClass("sticky-menu-mobile");
    }
  });

  // Scroll to top
  var btn = $('.scroll-top-btn');
  $(window).scroll(function () {
    if ($(window).scrollTop() > 300) {
      btn.addClass('jumpTop');
    } else {
      btn.removeClass('jumpTop');
    }
  });

  btn.on('click', function (e) {
    e.preventDefault();
    $('html, body').animate({
      scrollTop: 0
    }, '300');
  });

  $("#nav ul li a[href^='#']").on('click', function (e) {
    e.preventDefault();
    var hash = this.hash;

    $('html, body').animate({
      scrollTop: $(hash).offset().top
    }, 1000, function () {
      window.location.hash = hash;
    });
  });

  $("#nav div div a[href^='#']").on('click', function (e) {
    e.preventDefault();
    var hash = this.hash;
    $('html, body').animate({
      scrollTop: $(hash).offset().top
    }, 1000, function () {
      window.location.hash = hash;
    });

  });

  $("#nav ul li a[href^='#']").on('click', function (e) {
    e.preventDefault();

    // store hash
    var hash = this.hash;

    // animate
    $('html, body').animate({
      scrollTop: $(hash).offset().top
    }, 1000, function () {
      window.location.hash = hash;
    });

  });

  $("#nav div div a[href^='#']").on('click', function (e) {
    e.preventDefault();
    var hash = this.hash;
    $('html, body').animate({
      scrollTop: $(hash).offset().top
    }, 1000, function () {
      window.location.hash = hash;
    });
  });

  // Filter item
  $(document).on('click', '.filter-btn', function () {
    var show = $(this).data('show');
    $(show).removeClass("hide").siblings().addClass("hide");
  });

  $(document).on('click', '.filter-btn', function () {
    $(this).addClass('active').siblings().removeClass('active')
  })



  // Isotope Filter
  var $grid = $('.grid').isotope({
    itemSelector: '.element-item',
    layoutMode: 'fitRows'
  });
  // filter functions
  var filterFns = {
    // show if number is greater than 50
    numberGreaterThan50: function () {
      var number = $(this).find('.number').text();
      return parseInt(number, 10) > 50;
    },
    // show if name ends with -ium
    ium: function () {
      var name = $(this).find('.name').text();
      return name.match(/ium$/);
    }
  };
  // bind filter button click
  $('.filter-buttons-group').on('click', 'button', function () {
    var filterValue = $(this).attr('data-filter');
    // use filterFn if matches value
    filterValue = filterFns[filterValue] || filterValue;
    $grid.isotope({
      filter: filterValue
    });
  });
  // change is-checked class on buttons
  $('.button-group').each(function (i, buttonGroup) {
    var $buttonGroup = $(buttonGroup);
    $buttonGroup.on('click', 'button', function () {
      $buttonGroup.find('.checked').removeClass('checked');
      $(this).addClass('checked');
    });
  });

  $(function () {
    $(".button").on("click", function () {
      var $button = $(this);
      var $parent = $button.parent();
      var oldValue = $parent.find('.input').val();

      if ($button.text() == "+") {
        var newVal = parseFloat(oldValue) + 1;
      } else {
        // Don't allow decrementing below zero
        if (oldValue > 1) {
          var newVal = parseFloat(oldValue) - 1;
        } else {
          newVal = 1;
        }
      }
      $parent.find('a.add-to-cart').attr('data-quantity', newVal);
      $parent.find('.input').val(newVal);
    });
  });
  var countdown = $('.countdown');

  if (countdown.length) {

    $(function () {
      const second = 1000,
        minute = second * 60,
        hour = minute * 60,
        day = hour * 24;
      let today = new Date(),
        dd = String(today.getDate()).padStart(2, "0"),
        mm = String(today.getMonth() + 1).padStart(2, "0"),
        yyyy = today.getFullYear(),
        nextYear = yyyy + 1,
        dayMonth = "09/30/",
        counterday = dayMonth + yyyy;

      today = mm + "/" + dd + "/" + yyyy;
      if (today > counterday) {
        counterday = dayMonth + nextYear;
      }
      //end

      const countDown = new Date(counterday).getTime(),
        x = setInterval(function () {

          const now = new Date().getTime(),
            distance = countDown - now;

          document.getElementById("days").innerText = Math.floor(distance / (day)),
            document.getElementById("hours").innerText = Math.floor((distance % (day)) / (hour)),
            document.getElementById("minutes").innerText = Math.floor((distance % (hour)) / (minute)),
            document.getElementById("seconds").innerText = Math.floor((distance % (minute)) / second);

        }, 0)
    }());
  }


  // init Isotope
  var $grid = $('.fill').isotope({
    itemSelector: '.element-item',
    layoutMode: 'fitRows'
  });
  // filter functions
  var filterFns = {
    // show if number is greater than 50
    numberGreaterThan50: function () {
      var number = $(this).find('.number').text();
      return parseInt(number, 10) > 50;
    },
    // show if name ends with -ium
    ium: function () {
      var name = $(this).find('.name').text();
      return name.match(/ium$/);
    }
  };
  // bind filter on select change
  $('.filters-select').on('change', function () {
    // get filter value from option value
    var filterValue = this.value;
    // use filterFn if matches value
    filterValue = filterFns[filterValue] || filterValue;
    $grid.isotope({
      filter: filterValue
    });
  });

  $('.custom-select').each(function () {
    var $this = $(this),
      numberOfOptions = $(this).children('option').length;

    $this.addClass('select-hidden');
    $this.wrap('<div class="select"></div>');
    $this.after('<div class="select-styled"></div>');

    var $styledSelect = $this.next('div.select-styled');
    $styledSelect.text($this.children('option').eq(0).text());

    var $list = $('<ul />', {
      'class': 'select-options'
    }).insertAfter($styledSelect);

    for (var i = 0; i < numberOfOptions; i++) {
      $('<li />', {
        text: $this.children('option').eq(i).text(),
        rel: $this.children('option').eq(i).val()
      }).appendTo($list);
    }

    var $listItems = $list.children('li');


    $styledSelect.on('click', function (e) {
      e.stopPropagation();
      $('div.select-styled.active').not(this).each(function () {
        $(this).removeClass('active').next('ul.select-options').hide();
      });
      $(this).toggleClass('active').next('ul.select-options').toggle();
    });

    $listItems.on('click', function (e) {
      e.stopPropagation();
      $styledSelect.text($(this).text()).removeClass('active');
      $this.val($(this).attr('rel'));
      $list.hide();
    });

    $(document).click(function () {
      $styledSelect.removeClass('active');
      $list.hide();
    });

  });
  $('.custom-select2').each(function () {
    var $this = $(this),
      numberOfOptions = $(this).children('option').length;

    $this.addClass('select-hidden');
    $this.wrap('<div class="select2"></div>');
    $this.after('<div class="select-styled"></div>');

    var $styledSelect = $this.next('div.select-styled');
    $styledSelect.text($this.children('option').eq(0).text());

    var $list = $('<ul />', {
      'class': 'select-options'
    }).insertAfter($styledSelect);

    for (var i = 0; i < numberOfOptions; i++) {
      $('<li />', {
        text: $this.children('option').eq(i).text(),
        rel: $this.children('option').eq(i).val()
      }).appendTo($list);
    }

    var $listItems = $list.children('li');


    $styledSelect.on('click', function (e) {
      e.stopPropagation();
      $('div.select-styled.active').not(this).each(function () {
        $(this).removeClass('active').next('ul.select-options').hide();
      });
      $(this).toggleClass('active').next('ul.select-options').toggle();
    });

    $listItems.on('click', function (e) {
      e.stopPropagation();
      $styledSelect.text($(this).text()).removeClass('active');
      $this.val($(this).attr('rel'));
      $list.hide();
    });

    $(document).click(function () {
      $styledSelect.removeClass('active');
      $list.hide();
    });

  });

  var cookies = document.cookie.split(';')
    .reduce((res, c) => {
      const [key, val] = c.trim().split('=').map(decodeURIComponent)
      return Object.assign(res, {
        [key]: val
      })
    }, {});


  $(".header-topbar5").on('click', function () {
    $(".header-topbar5").addClass("close");
  });

  $(".category-item-inner").on('click', function () {
    var cateItem = $(this).parent(".category-item")
    cateItem.toggleClass('show');
    cateItem.siblings(".category-item").removeClass('show');
  });


  $(".color-item").one('click', function () {
    $(this).toggleClass('selected');

  });


  $(".coupon-click").on('click', function () {
    $(".coupon-input-area").toggleClass('show');
  });


  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
  })


  // Newsletter popup
  // $(document).ready(function () {
  //   function showpanel() {
  //     $(".anywere-home").addClass("bgshow");
  //     $(".rts-newsletter-popup").addClass("popup");
  //   }
  //   setTimeout(showpanel, 4000)
  // });

  // $(".anywere-home").on('click', function () {
  //   $(".rts-newsletter-popup").removeClass("popup")
  //   $(".anywere-home").removeClass("bgshow")
  // });
  // $(".newsletter-close-btn").on('click', function () {
  //   $(".rts-newsletter-popup").removeClass("popup")
  //   $(".anywere-home").removeClass("bgshow")
  // });

  // Product details popup
  $(".product-details-popup-btn").on('click', function () {
    $(".product-details-popup-wrapper").addClass("popup")
    $(".anywere").addClass("bgshow")
  });
  $(".product-bottom-action .view-btn").on('click', function () {
    $(".product-details-popup-wrapper").addClass("popup")
    $(".anywere").addClass("bgshow")
  });
  $(".product-details-popup-wrapper .cart-edit").on('click', function () {
    $(".product-details-popup-wrapper").addClass("popup")
    $(".anywere-home").addClass("bgshow")
  });

  $(".product-details-close-btn").on('click', function () {
    $(".product-details-popup-wrapper").removeClass("popup")
    $(".anywere").removeClass("bgshow")
  });
  $(".anywere").on('click', function () {
    $(".product-details-popup-wrapper").removeClass("popup")
    $(".anywere").removeClass("bgshow")
  });


})(jQuery);

function zoom(e) {
  var zoomer = e.currentTarget;
  e.offsetX ? offsetX = e.offsetX : offsetX = e.touches[0].pageX
  e.offsetY ? offsetY = e.offsetY : offsetX = e.touches[0].pageX
  x = offsetX / zoomer.offsetWidth * 100
  y = offsetY / zoomer.offsetHeight * 100
  zoomer.style.backgroundPosition = x + '% ' + y + '%';
}

var nstSlider = $('.nstSlider');

if (nstSlider.length) {
  $('.nstSlider').nstSlider({
    "left_grip_selector": ".leftGrip",
    "right_grip_selector": ".rightGrip",
    "value_bar_selector": ".bar",
    "value_changed_callback": function (cause, leftValue, rightValue) {
      $(this).parent().find('.leftLabel').text(leftValue);
      $(this).parent().find('.rightLabel').text(rightValue);
    }
  });
}


// handle alamat di halaman checkout
$('input[name="paymentMethod"]').on("change", function () {
  const selectedMethod = $(this).attr("id");

  if (selectedMethod === "freetrans") {
    // Jika memilih COD, tampilkan form alamat
    $("#addressContainer").slideDown();
  } else {
    // Jika memilih Bayar di Outlet, sembunyikan form alamat
    $("#addressContainer").slideUp();
  }
});