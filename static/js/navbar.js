// Allowing mobile nav (burger) menu
const burgerIcon = document.querySelector('#burger');
const navbarMenu = document.querySelector('#navbar');

burgerIcon.addEventListener('click', () => {
    navbarMenu.classList.toggle('is-active')
})