const notification = document.querySelector('.notification')
const bubbles = notification.querySelectorAll('.bubble')
const lines = notification.querySelectorAll('.notification .bubble .line')
const closeBtns = notification.querySelectorAll('.notification .bubble .fa-times')
function lineanimstart() {
    this.children[3].style.transition = "none";
    this.children[3].style.borderBottomRightRadius = '10px'
    this.children[3].style.width = '100%'
}
function lineanimend() {
    this.children[3].style.transition = 'width 10s';
    this.children[3].style.width = '0%'
}
bubbles.forEach(bubble => {
    bubble.addEventListener('transitionend', function() {
        if (this.children[2].style.width == '0%'){
            setTimeout(() => {
                this.remove()
            }, 500);
        }
    })
    bubble.addEventListener('mouseenter', lineanimstart)
    bubble.addEventListener('touchstart', lineanimstart)
    bubble.addEventListener('mouseleave', lineanimend)
    bubble.addEventListener('touchend', lineanimend)
})
closeBtns.forEach(btn => {
    btn.addEventListener('click', function (){
        this.parentElement.parentElement.style.opacity = 0
        setTimeout(() => {
            this.parentElement.parentElement.remove()
        }, 500);
    })
})
window.addEventListener('load', ()=>{
    lines.forEach(line => {
        line.style.width = '0%'
        line.addEventListener('transitionstart', function() {
            this.style.borderBottomRightRadius = '0px'
        })
        line.addEventListener('transitionend', function() {
            if (this.style.width == '0%'){
                this.parentElement.style.opacity = 0
            }
        })
    })
})