// scripts.js

document.addEventListener('DOMContentLoaded', function () {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function (event) {
            event.preventDefault();
            alert('Форма отправлена!');
            form.submit();
        });
    });

    const faqItems = document.querySelectorAll('.faq-item .question');
    faqItems.forEach(item => {
        item.addEventListener('click', function () {
            const answer = this.nextElementSibling;
            if (answer.style.display === 'none' || answer.style.display === '') {
                answer.style.display = 'block';
            } else {
                answer.style.display = 'none';
            }
        });
    });

    // Slider logic
    const gallery = document.querySelector('.slides');
    const images = gallery.querySelectorAll('img');
    const leftArrow = document.querySelector('.arrow-left');
    const rightArrow = document.querySelector('.arrow-right');
    let currentIndex = 0;

    function showSlide(index) {
        const totalImages = images.length;
        if (index >= totalImages) {
            currentIndex = 0;
        } else if (index < 0) {
            currentIndex = totalImages - 1;
        } else {
            currentIndex = index;
        }
        gallery.style.transform = `translateX(-${currentIndex * 100}%)`;
    }

    leftArrow.addEventListener('click', () => showSlide(currentIndex - 1));
    rightArrow.addEventListener('click', () => showSlide(currentIndex + 1));

    setInterval(() => showSlide(currentIndex + 1), 5000); // Автоматическое переключение каждые 5 секунд
});
