const navBtn = document.querySelector('.navbtn')
const navbar = document.querySelector('nav')
const darkMode = document.querySelector('.switch')
const body = document.querySelector('body')
navBtn.addEventListener('click', ()=>{
    margin = window.getComputedStyle(navbar).marginTop
    if (margin === '-240px') {
        navbar.style.marginTop = '0%'
        navBtn.classList.add('close')
    }
    else {
        navbar.style.marginTop = '-240px'
        navBtn.classList.remove('close')
    }
})
function nightMode(){
    return body.classList.toggle('dark')
}
darkMode.addEventListener('click', () => {
    localStorage.setItem('darkmode', nightMode())
})
if (localStorage.darkmode == 'true'){
    nightMode()
}