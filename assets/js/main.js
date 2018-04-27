var hoverDropdown = document.querySelector('#hover-dropdown')
var clickDropdown = document.querySelector('#click-dropdown')
var parallax = document.querySelector('.parallax')
var mobileNav = document.querySelector('#mobile-nav')

M.Dropdown.init(hoverDropdown, {
  hover: true,
  constrainWidth: false
})
M.Dropdown.init(clickDropdown, {
  constrainWidth: false
})

M.Sidenav.init(mobileNav)

M.Parallax.init(parallax)



  

