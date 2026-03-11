/* =============================
   HANGARIN - Main JavaScript
   ============================= */

document.addEventListener('DOMContentLoaded', function () {

    // ===== ACTIVE SIDEBAR LINK =====
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.sidebar-nav .nav-link');

    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });

    // ===== SIDEBAR TOGGLE (Mobile) =====
    const sidebarToggle = document.getElementById('sidebarToggle');
    const sidebar = document.querySelector('.sidebar');

    if (sidebarToggle && sidebar) {
        sidebarToggle.addEventListener('click', function () {
            sidebar.classList.toggle('sidebar-open');
        });
    }

    // ===== FADE IN STAT CARDS ON LOAD =====
    const statCards = document.querySelectorAll('.stat-card');
    statCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = `opacity 0.4s ease ${index * 0.1}s, transform 0.4s ease ${index * 0.1}s`;

        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 100);
    });

    // ===== TABLE ROW HOVER HIGHLIGHT =====
    const tableRows = document.querySelectorAll('.table tbody tr');
    tableRows.forEach(row => {
        row.style.cursor = 'pointer';
        row.style.transition = 'background 0.2s ease';
    });

    // ===== AUTO DISMISS ALERTS =====
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.transition = 'opacity 0.5s ease';
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 500);
        }, 3000);
    });

});