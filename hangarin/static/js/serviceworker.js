self.addEventListener('install', function(e) {
    e.waitUntil(
        caches.open('projectsite-cache-v1').then(function(cache) {
            return cache.addAll([
                '/',
                // CSS
                '/static/statics/css/theme.css',
                '/static/statics/css/font-face.css',
                '/static/statics/css/aos.css',
                '/static/statics/vendor/bootstrap-5.3.8.min.css',
                '/static/statics/vendor/perfect-scrollbar/perfect-scrollbar-1.5.6.css',
                '/static/statics/vendor/css-hamburgers/hamburgers.min.css',
                '/static/statics/vendor/fontawesome-7.1.0/css/all.min.css',
                '/static/statics/vendor/mdi-font/css/material-design-iconic-font.min.css',
                '/static/statics/css/swiper-bundle-12.0.3.min.css',
                // JS
                '/static/statics/vendor/bootstrap-5.3.8.bundle.min.js',
                '/static/statics/vendor/perfect-scrollbar/perfect-scrollbar-1.5.6.min.js',
                '/static/statics/js/vanilla-utils.js',
                '/static/statics/js/bootstrap5-init.js',
                '/static/statics/js/main-vanilla.js',
                '/static/statics/js/aos.js',
                '/static/statics/js/modern-plugins.js',
                '/static/js/ready.min.js',
                // Images
                '/static/img/user.jpg',
                '/static/img/icon-192.png',
                '/static/img/icon-512.png',
                // Fonts
                '/static/statics/fonts/poppins/poppins-v5-latin-regular.woff2',
                '/static/statics/fonts/poppins/poppins-v5-latin-500.woff2',
                '/static/statics/fonts/poppins/poppins-v5-latin-700.woff2',
                '/static/statics/fonts/poppins/poppins-v5-latin-300.woff2',
                '/static/statics/vendor/mdi-font/fonts/Material-Design-Iconic-Font.woff2?v=2.2.0',
                '/static/statics/vendor/fontawesome-7.1.0/webfonts/fa-solid-900.woff2',
            ]);
        })
    );
});

self.addEventListener('fetch', function(e) {
    e.respondWith(
        caches.match(e.request).then(function(response) {
            return response || fetch(e.request);
        })
    );
});