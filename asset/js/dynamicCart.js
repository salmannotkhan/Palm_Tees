const plusMinusBtn = document.querySelectorAll('.qty button')
const grand = document.querySelector('.grand > span')

grandtotal = 0
document.querySelectorAll('.details > .total > div').forEach(total => {
    qty = total.parentNode.parentNode.childNodes[5].childNodes[1].childNodes[3].value
    total.innerHTML = (total.innerHTML * qty).toFixed(2)
    grandtotal += parseFloat(total.innerHTML)
})
grand.innerHTML = grandtotal.toFixed(2)
const grandTotal = (e) => {
    price = parseFloat(e.target.parentNode.parentNode.previousElementSibling.innerHTML)
    const qty = e.target.parentNode.childNodes[3].value
    const total = e.target.parentNode.parentNode.nextElementSibling.lastElementChild
    total.innerHTML =  (price * qty).toFixed(2)
    
    grandtotal = 0
    document.querySelectorAll('.details > .total > div').forEach(total => {
        grandtotal += parseFloat(total.innerHTML)
    })
    return grandtotal.toFixed(2)
}

plusMinusBtn.forEach(button => {
    button.addEventListener('click', (e) => {
        const qtyField = e.target.parentNode.childNodes[3]
        if (e.target.dataset['sign'] == '+') {
            if (parseInt(qtyField.value) < 100) {
                qtyField.value = parseInt(qtyField.value) + 1
                grand.innerHTML = grandTotal(e)
            }
        }
        else {
            if (parseInt(qtyField.value) > 1) {
                qtyField.value -= 1
                grand.innerHTML = grandTotal(e)
            }
        }
    })
})