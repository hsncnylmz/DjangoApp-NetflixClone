    // Sayfa scroll edildiğinde bu fonksiyon çalışacak
    window.onscroll = function () {
        var navbar = document.querySelector('.navbar');
        // Sayfanın üst kısmından aşağı scroll edildiğinde arkaplan rengini dark yap
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            navbar.classList.remove('bg-transparent');
            navbar.classList.add('bg-dark');
        } else {
            navbar.classList.remove('bg-dark');
            navbar.classList.add('bg-transparent');
        }
    };
