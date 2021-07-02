// Menu Close Button
const menuBtn = document.querySelector('.menu__button');
const nav = document.querySelector('.header nav');
const navItems = document.querySelectorAll('.header nav ul li');
let menuOpen = false;
menuBtn.addEventListener('click', () => {
    if(!menuOpen) {
        menuBtn.classList.add('open');
        // Nav Close Event
        nav.classList.add('active');
        menuOpen = true;
    } else {
        menuBtn.classList.remove('open');
        // Nav Close Event
        nav.classList.remove('active');
        menuOpen = false;
    }
}); 

navItems.forEach(item => {
    item.addEventListener('click',() => {
        if(!menuOpen) {
            menuBtn.classList.add('open');
            // Nav Close Event
            nav.classList.add('active');
            menuOpen = true;
        } else {
            menuBtn.classList.remove('open');
            // Nav Close Event
            nav.classList.remove('active');
            menuOpen = false;
        }
    })
})

// User Profile
const editProfile = document.querySelector('.edit__profile');
const myCourses = document.querySelector('.my__courses');

myCourses.addEventListener('click', () => {
    myCourses.classList.add('edit__profile');
    editProfile.classList.remove('edit__profile');
    editProfile.classList.add('my__courses')
})
editProfile.addEventListener('click', () => {
    editProfile.classList.add('edit__profile');
    myCourses.classList.remove('edit__profile');
    myCourses.classList.add('my__courses')
})