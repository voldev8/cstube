const results = Array.from(document.querySelectorAll('#search_result_list'));

function slideIn(results, index) {
  setTimeout(function () {
    results.classList.remove('slide-out');
  }, (index + 5) * 200);
}

results.forEach(slideIn);

const icon = document.getElementById('icon');
const icon1 = document.getElementById('a');
const icon2 = document.getElementById('b');
const icon3 = document.getElementById('c');
const sideBar = document.querySelector('.sidebar-nav');
const outer = document.querySelector('.sidebar-outer');

icon.addEventListener('click', function () {
  icon1.classList.toggle('a');
  icon2.classList.toggle('c');
  icon3.classList.toggle('b');
  sideBar.classList.toggle('show');
  outer.classList.toggle('slide');
});
