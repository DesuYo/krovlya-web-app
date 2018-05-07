var hoverDropdown = document.querySelector('#hover-dropdown')
var clickDropdown = document.querySelector('#click-dropdown')
var parallax = document.querySelector('.parallax')
var mobileNav = document.querySelector('#mobile-nav')
var tabs = document.querySelector('.tabs')

M.Dropdown.init(hoverDropdown, {
  hover: true,
  constrainWidth: false
})
M.Dropdown.init(clickDropdown, {
  constrainWidth: false
})

M.Tabs.init(tabs)

M.Sidenav.init(mobileNav)

M.Parallax.init(parallax)



  

