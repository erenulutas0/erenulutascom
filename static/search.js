// İstemci tarafı arama: search-index.json üzerinde basit skorlama.
(function () {
  var input = document.getElementById('q');
  var srcSel = document.getElementById('kaynak');
  var lvlSel = document.getElementById('seviye');
  var list = document.getElementById('sonuclar');
  var countEl = document.getElementById('sonuc-sayisi');
  var emptyEl = document.getElementById('bos');
  if (!input || !list) return;

  var rows = [];

  // Türkçe karakterleri sadeleştir: "önbellek" ~ "onbellek" ikisi de bulsun
  function fold(s) {
    return (s || '')
      .toLocaleLowerCase('tr')
      .replace(/ç/g, 'c').replace(/ğ/g, 'g').replace(/ı/g, 'i')
      .replace(/ö/g, 'o').replace(/ş/g, 's').replace(/ü/g, 'u')
      .replace(/î/g, 'i').replace(/â/g, 'a');
  }

  function escapeHtml(s) {
    return (s || '').replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function highlight(text, terms) {
    var out = escapeHtml(text);
    terms.forEach(function (t) {
      if (t.length < 2) return;
      // fold edilmiş konumları bul, orijinal metinde işaretle
      var folded = fold(out);
      var idx = folded.indexOf(t);
      if (idx === -1) return;
      out = out.slice(0, idx) + '<mark>' + out.slice(idx, idx + t.length) + '</mark>' + out.slice(idx + t.length);
    });
    return out;
  }

  function score(row, terms) {
    var hay = {
      t: fold(row.t), o: fold(row.o), b: fold(row.b),
      s: fold(row.s), g: fold((row.g || []).join(' '))
    };
    var total = 0;
    for (var i = 0; i < terms.length; i++) {
      var t = terms[i], hit = 0;
      if (hay.t.indexOf(t) !== -1) hit += 10;
      if (hay.g.indexOf(t) !== -1) hit += 6;
      if (hay.o.indexOf(t) !== -1) hit += 4;
      if (hay.s.indexOf(t) !== -1) hit += 3;
      if (hay.b.indexOf(t) !== -1) hit += 2;
      if (hit === 0) return 0;          // her terim eşleşmeli (AND)
      total += hit;
    }
    return total;
  }

  function render() {
    var raw = input.value.trim();
    var terms = fold(raw).split(/\s+/).filter(function (t) { return t.length > 1; });
    var src = srcSel ? srcSel.value : '';
    var lvl = lvlSel ? lvlSel.value : '';

    var results = rows.filter(function (r) {
      if (src && r.k !== src) return false;
      if (lvl && r.x !== lvl) return false;
      return true;
    });

    if (terms.length) {
      results = results
        .map(function (r) { return { r: r, s: score(r, terms) }; })
        .filter(function (x) { return x.s > 0; })
        .sort(function (a, b) { return b.s - a.s || (a.r.d < b.r.d ? 1 : -1); })
        .map(function (x) { return x.r; });
    } else {
      results = results.slice().sort(function (a, b) { return a.d < b.d ? 1 : -1; });
    }

    countEl.textContent = raw || src || lvl
      ? results.length + ' sonuç'
      : rows.length + ' özet listeleniyor';
    emptyEl.hidden = results.length > 0;

    list.innerHTML = results.slice(0, 120).map(function (r) {
      return '<li class="row"><a class="row-link" href="' + r.u + '">' +
        '<span class="row-date">' + escapeHtml(r.d) + '</span>' +
        '<span class="row-body">' +
          '<strong>' + highlight(r.t, terms) + '</strong>' +
          '<span class="row-orig">' + escapeHtml(r.o) + '</span>' +
          '<span class="row-sum">' + highlight(r.b, terms) + '…</span>' +
        '</span></a>' +
        '<span class="badge">' + escapeHtml(r.s) + '</span></li>';
    }).join('');
  }

  fetch('/search-index.json')
    .then(function (r) { return r.json(); })
    .then(function (data) {
      rows = data;
      render();
      // URL'de ?q= varsa doldur
      var q = new URLSearchParams(location.search).get('q');
      if (q) { input.value = q; render(); }
    })
    .catch(function () {
      countEl.textContent = 'Arama dizini yüklenemedi.';
    });

  var timer;
  function debounced() { clearTimeout(timer); timer = setTimeout(render, 120); }
  input.addEventListener('input', debounced);
  if (srcSel) srcSel.addEventListener('change', render);
  if (lvlSel) lvlSel.addEventListener('change', render);
})();
