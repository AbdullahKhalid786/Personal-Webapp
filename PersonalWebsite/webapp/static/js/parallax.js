document.addEventListener('scroll', function() {
    const backdrop = document.getElementById('backdrop');
    const nameTitle = document.getElementById('nameTitle');
    const scrollPosition = window.scrollY;
    const maxScroll = window.innerHeight;
    
    // Calculate scale and translateY based on scroll position
    const scaleValue = 1 + Math.min(scrollPosition / maxScroll, 0.2); // Stop scaling after 20%
    const translateValue = Math.min(scrollPosition / 2, 50); // Stop translating after 50px

    // Apply transformations
    // backdrop.style.transform = `scale(${scaleValue})`;
    // nameTitle.style.transform = `translateY(${translateValue}px)`;
});
