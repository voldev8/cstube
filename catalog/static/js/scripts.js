const results = Array.from(document.querySelectorAll('#search_result_list'));

function slideIn(results, index) {
  setTimeout(function() {
    results.classList.remove('slide-out');
  }, (index + 5) * 200);  
}

results.forEach(slideIn);

