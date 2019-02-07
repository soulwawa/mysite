document.querySelector('section').style.height = window.innerHeight + 'px';

window.addEventListener('resize', function () {
  document.querySelector('body').style.width = window.innerWidth + 'px';
  document.querySelector('section').style.height = window.innerHeight + 'px';
});