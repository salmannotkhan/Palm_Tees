const navBtn = document.querySelector('.navbtn')
const navbar = document.querySelector('nav')
navBtn.addEventListener('click', ()=>{
    margin = window.getComputedStyle(navbar).marginTop
    if (margin === '-235px') {
        navbar.style.marginTop = '0%'
        navBtn.classList.add('close')
    }
    else {
        navBtn.classList.remove('close')
        navbar.style.marginTop = '-235px'
    }
})