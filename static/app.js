// Tema geçişi: görünen temanın tersine geç. Seçim sistem temasıyla aynıysa
// kayıt silinir, böylece site yeniden sistemi izler.
(function () {
  var btn = document.getElementById('tema');
  if (!btn) return;
  var root = document.documentElement;
  var mq = window.matchMedia('(prefers-color-scheme: dark)');

  btn.addEventListener('click', function () {
    var system = mq.matches ? 'dark' : 'light';
    var current = root.dataset.theme;
    if (current !== 'light' && current !== 'dark') current = system;
    var next = current === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next === system ? 'auto' : next;
    try {
      if (next === system) localStorage.removeItem('tema');
      else localStorage.setItem('tema', next);
    } catch (e) {}
  });
})();

// Okuma ilerlemesi (masthead altındaki ince çizgi)
(function () {
  var bar = document.getElementById('ilerleme');
  if (!bar) return;
  var ticking = false;
  function update() {
    var max = document.documentElement.scrollHeight - window.innerHeight;
    bar.style.transform = 'scaleX(' + (max > 0 ? Math.min(1, window.scrollY / max) : 0) + ')';
    ticking = false;
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { ticking = true; requestAnimationFrame(update); }
  }, { passive: true });
  update();
})();

// İçindekiler: ekranda okunan yazıyı işaretle
(function () {
  var toc = document.getElementById('toc');
  if (!toc || !('IntersectionObserver' in window)) return;
  var links = {};
  toc.querySelectorAll('a[href^="#"]').forEach(function (a) {
    links[a.getAttribute('href').slice(1)] = a;
  });
  var stories = Object.keys(links)
    .map(function (id) { return document.getElementById(id); })
    .filter(Boolean);
  if (!stories.length) return;

  function activate(id) {
    Object.keys(links).forEach(function (k) {
      links[k].classList.toggle('is-active', k === id);
    });
  }
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) activate(e.target.id); });
  }, { rootMargin: '-25% 0px -65% 0px' });
  stories.forEach(function (s) { observer.observe(s); });
  activate(stories[0].id);
})();

// Bir yazıya # ile gelindiğinde kısa süre vurgula
(function () {
  function flash() {
    var id = location.hash.slice(1);
    if (!id) return;
    var el = document.getElementById(id);
    if (!el || !el.classList.contains('story')) return;
    el.style.transition = 'background-color .8s ease';
    el.style.backgroundColor = 'var(--accent-soft)';
    setTimeout(function () { el.style.backgroundColor = ''; }, 1600);
  }
  window.addEventListener('hashchange', flash);
  if (location.hash) setTimeout(flash, 80);
})();

// "/" tuşu: arama kutusuna odaklan, arama sayfasında değilsen oraya git
(function () {
  document.addEventListener('keydown', function (e) {
    if (e.key !== '/' || e.ctrlKey || e.metaKey || e.altKey) return;
    var t = e.target;
    if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.tagName === 'SELECT' || t.isContentEditable)) return;
    e.preventDefault();
    var q = document.getElementById('q');
    if (q) q.focus(); else location.href = '/ara/';
  });
})();
