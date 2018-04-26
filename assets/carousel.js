var carousel = document.querySelector('.carousel')
var carouselInstance = M.Carousel.init(carousel, {
  fullWidth: true,
  dist: 0,
  indicators: true
})
setInterval(function() {
  carouselInstance.next()
}, 4000)
