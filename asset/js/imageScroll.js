showcase = document.querySelector('.images')
var zoom = 1.3


document.querySelectorAll('.image-nav').forEach(button => {
    button.addEventListener('click', (e) => {
        var imgWidth = showcase.childNodes[1].width
        var pxToScroll = imgWidth / 2 + 100
        if (e.target.dataset.direction == 'Next'){
            showcase.scrollTo(imgWidth + pxToScroll, 0)
        }
        else{
            showcase.scrollTo(-pxToScroll, 0)
        }
    })
})