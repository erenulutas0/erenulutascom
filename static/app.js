// Tema geçişi: auto -> light -> dark -> auto
(function () {
  var btn = document.getElementById('tema');
  if (!btn) return;

  var order = ['auto', 'light', 'dark'];
  btn.addEventListener('click', function () {
    var current = document.documentElement.dataset.theme || 'auto';
    var next = order[(order.indexOf(current) + 1) % order.length];
    document.documentElement.dataset.theme = next;
    try {
      if (next === 'auto') localStorage.removeItem('tema');
      else localStorage.setItem('tema', next);
    } catch (e) {}
    btn.setAttribute('title', 'Tema: ' + next);
  });
})();

// Bir yazıya # ile gelindiğinde kısa süre vurgula
(function () {
  function flash() {
    var id = location.hash.slice(1);
    if (!id) return;
    var el = document.getElementById(id);
    if (!el) return;
    el.style.transition = 'background-color .8s ease';
    el.style.backgroundColor = 'var(--accent-soft)';
    setTimeout(function () { el.style.backgroundColor = ''; }, 1600);
  }
  window.addEventListener('hashchange', flash);
  if (location.hash) setTimeout(flash, 80);
})();
