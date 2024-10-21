// Observer options to trigger at different thresholds
const options = {
    threshold: [0, 0.5, 1] // Trigger at 0%, 50%, and 100% visibility
};

// Observer for showing elements when they enter the viewport
const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        // Toggle 'show' class based on intersection for non-hero elements
        if (entry.target.classList.contains('hidden') && entry.isIntersecting) {
            entry.target.classList.add('show');
        }

        // Check if the current element is the hero section
        if (entry.target.classList.contains('hero')) {
            console.log('hero visibility:', entry.intersectionRatio);

            // Show/hide navbar based on intersection with hero section
            if (entry.intersectionRatio >= 0.5) {
                // If 50% or more of the hero is visible, hide the navbar and reset elements
                document.querySelector('.nav-hidden').classList.remove('visible');
                
                // Reset all elements to hidden when 50% or more of the hero is visible
                document.querySelectorAll('.hidden').forEach((el) => {
                    el.classList.remove('show');
                });
            } else {
                // Less than 50% of hero is visible, show the navbar
                document.querySelector('.nav-hidden').classList.add('visible');
            }
        }
    });
}, options);

// Observing elements
const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((el) => observer.observe(el));

// Observe the hero section separately with specific options
const heroElement = document.querySelector('.hero');
observer.observe(heroElement);
