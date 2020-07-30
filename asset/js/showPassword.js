const passwords = document.querySelectorAll('input[type="password"]')

eyeIcon = document.createElement('i')
eyeIcon.classList.add('fa', 'fa-eye')

passwords[0].parentElement.appendChild(eyeIcon)

eyeIcon.addEventListener('click', () => {
    eyeIcon.classList.toggle('fa-eye')
    eyeIcon.classList.toggle('fa-eye-slash')
    passwords.forEach(password => {
        password.type == 'text' ? password.type ='password' : password.type = 'text'
    })
})