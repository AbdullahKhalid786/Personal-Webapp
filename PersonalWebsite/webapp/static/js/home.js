// Observer for showing elements when they enter the viewport
const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        // Toggle 'show' class based on intersection
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
        } else {
            entry.target.classList.remove('show');
        }

        // Debugging logs to ensure the project menu is being observed
        if (entry.target.classList.contains('project-menu')) {
            console.log('Project menu visibility:', entry.isIntersecting);

            // Show/hide navbar based on intersection with project-menu
            if (entry.isIntersecting) {
                document.querySelector('.nav-hidden').classList.add('visible');
            } else {
                document.querySelector('.nav-hidden').classList.remove('visible');
            }
        }
    });
});

// Observe all hidden elements
const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((el) => observer.observe(el));

// Ensure the project menu section is correctly selected and observed
const projectSection = document.querySelector('.project-menu');
if (projectSection) {
    observer.observe(projectSection);
} else {
    window.alert('Project section not found');
}
