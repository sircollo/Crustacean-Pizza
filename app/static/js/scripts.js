/*!
* Start Bootstrap - Agency v7.0.11 (https://startbootstrap.com/theme/agency)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-agency/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});

//////////////////////////

function slice() {
    var scrollPizza1 = document.querySelector(".scroll-pizza1");
    var scrollPizza2 = document.querySelector(".scroll-pizza2");
    
      var windowHeight = window.innerHeight;
      var elementTop1 = scrollPizza1.getBoundingClientRect().top;
      var elementTop2 = scrollPizza2.getBoundingClientRect().top;
      var elementVisible = 500;

      if (elementTop1 || elementTop2 < windowHeight - elementVisible) {
        scrollPizza1.classList.add("scroll");
        scrollPizza2.classList.add("scroll");
      } else {
        scrollPizza1.classList.remove("scroll");
        scrollPizza2.classList.remove("scroll");
      }
    }
    
  window.addEventListener("scroll", slice);

    // To check the scroll position on page load
    slice1();
    