self.addEventListener('install', event => {
  event.waitUntil(
    caches.open('ytmp3-cache').then(cache =>
      cache.addAll([
        '/',
        '/static/style.css',
        '/static/manifest.json'
      ])
    )
  );
});
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response =>
      response || fetch(event.request)
    )
  );
});
