const showcase = document.querySelector('.images')
const glass = document.querySelector('.magnifier')
if (window.innerWidth > 768){
    showcase.childNodes.forEach(image => {
        image.addEventListener('mousemove', e => {
            img = e.target
            posX = e.layerX % img.width
            posY = e.layerY + 1 % img.height
            
            if (img.tagName == 'IMG' && e.layerX % img.width > 70){
                img.style.filter = 'opacity(0.5)'
                glass.style.display = 'block';
                
                // Pure Hack
                glass.style.backgroundImage = 'url(\'' + img.attributes['src'].value + '\')'
                glass.style.backgroundSize = (img.width * zoom) + 'px ' + (img.height * zoom)  + 'px' 
                glass.style.backgroundPosition = '-' + (posX - 70) + 'px -' + posY + 'px'
                glass.style.left = posX + 'px'
                glass.style.top = posY + 'px'
                glass.style.scale = '100%'
            }
            
            image.addEventListener('mouseleave', () => {
                image.style.filter = 'opacity(1)'
                glass.style.scale = '0%'
                glass.addEventListener('animationend', ()=>{
                    setTimeout(100)
                })
                glass.style.display = 'none'
            })
        })
    })
}