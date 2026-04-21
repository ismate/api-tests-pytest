// const btn = document.querySelector('.three-stripe');
// const panel = document.querySelector('.left-panel');


// btn.addEventListener('click',()=>{
//     panel.classList.toggle('open');
// });
const btn = document.getElementById('sidebar-toggle');
const panel = document.getElementById('left-panel');
const icon = btn.querySelector('i');

btn.addEventListener('click', () =>{
    const isOpen = panel.classList.toggle('open');
    btn.setAttribute('aria-expanded', isOpen);
    if (isOpen) {
        icon.classList.remove('fa-bars');
        icon.classList.add('fa-times');

        icon.classList.add('rotate');
        icon.addEventListener('animationend', () => {
            icon.classList.remove('rotate');
        }, {once: true });
    } else {
        icon.classList.remove('fa-times');
        icon.classList.add('fa-bars');
    }
});
console.log(icon);

// document.addEventListener('keydown', e =>{
//     if (e.key === 'Escape' && panel.classList.contains('open')){
//         panel.classList.remove('open');
//     }
// });
// btn.addEventListener('click', () => {
//     const opened = panel.classList.toggle('open');
//     btn.setAttribute('aria-expanded', opened);
//     ;
// })

