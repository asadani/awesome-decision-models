// Filter the tools table. The full table is already in the HTML, so the page works without JS.
(function () {
  var q = document.getElementById('q');
  var cat = document.getElementById('cat');
  var lic = document.getElementById('lic');
  var rows = Array.prototype.slice.call(document.querySelectorAll('#tools-body tr'));
  var count = document.getElementById('count');
  var empty = document.getElementById('empty');
  if (!q || !rows.length) return;

  function apply() {
    var term = q.value.trim().toLowerCase();
    var shown = 0;
    rows.forEach(function (r) {
      var ok = (!term || r.getAttribute('data-text').indexOf(term) !== -1) &&
               (!cat.value || r.getAttribute('data-cat') === cat.value) &&
               (!lic.value || r.getAttribute('data-lic') === lic.value);
      r.hidden = !ok;
      if (ok) shown++;
    });
    count.textContent = 'Showing ' + shown + ' of ' + rows.length + ' projects';
    empty.hidden = shown !== 0;
  }
  q.addEventListener('input', apply);
  cat.addEventListener('change', apply);
  lic.addEventListener('change', apply);
  apply();
})();
