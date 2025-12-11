const UI = {
    init() {
        this.initScrollAnimations();
        this.initInputAnimations();
        this.initNavScroll();
    },

    initScrollAnimations() {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('fade-in');
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        document.querySelectorAll('.step, .stat-card, .fees-table').forEach(el => {
            el.style.opacity = '0';
            observer.observe(el);
        });
    },

    initInputAnimations() {
        document.querySelectorAll('.input-group input').forEach(input => {
            input.addEventListener('focus', function() {
                this.parentElement.classList.add('focused');
            });

            input.addEventListener('blur', function() {
                if (!this.value) {
                    this.parentElement.classList.remove('focused');
                }
            });
        });
    },

    initNavScroll() {
        let lastScroll = 0;
        const nav = document.querySelector('.glass-nav');

        if (nav) {
            window.addEventListener('scroll', () => {
                const currentScroll = window.pageYOffset;

                if (currentScroll > 100) {
                    nav.style.background = 'rgba(15, 15, 35, 0.95)';
                } else {
                    nav.style.background = 'rgba(15, 15, 35, 0.7)';
                }

                lastScroll = currentScroll;
            });
        }
    },

    showToast(message, type = 'info') {
        const existingToast = document.querySelector('.toast');
        if (existingToast) {
            existingToast.remove();
        }

        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        toast.innerHTML = `
            <span class="toast-message">${message}</span>
            <button class="toast-close">&times;</button>
        `;

        const style = document.createElement('style');
        style.textContent = `
            .toast {
                position: fixed;
                bottom: 30px;
                right: 30px;
                padding: 15px 25px;
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(20px);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 12px;
                display: flex;
                align-items: center;
                gap: 15px;
                animation: slideInRight 0.3s ease;
                z-index: 9999;
                max-width: 400px;
            }
            .toast-success { border-color: var(--success-color); }
            .toast-error { border-color: var(--error-color); }
            .toast-warning { border-color: var(--warning-color); }
            .toast-close {
                background: none;
                border: none;
                color: var(--text-primary);
                font-size: 1.2rem;
                cursor: pointer;
                opacity: 0.7;
                transition: opacity 0.3s;
            }
            .toast-close:hover { opacity: 1; }
        `;

        if (!document.querySelector('#toast-styles')) {
            style.id = 'toast-styles';
            document.head.appendChild(style);
        }

        document.body.appendChild(toast);

        toast.querySelector('.toast-close').addEventListener('click', () => {
            toast.style.animation = 'slideInRight 0.3s ease reverse';
            setTimeout(() => toast.remove(), 300);
        });

        setTimeout(() => {
            if (toast.parentNode) {
                toast.style.animation = 'slideInRight 0.3s ease reverse';
                setTimeout(() => toast.remove(), 300);
            }
        }, 5000);
    },

    showLoader(container) {
        const loader = document.createElement('div');
        loader.className = 'loader';
        loader.innerHTML = `
            <div class="loader-spinner"></div>
        `;

        const style = document.createElement('style');
        style.textContent = `
            .loader {
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 40px;
            }
            .loader-spinner {
                width: 40px;
                height: 40px;
                border: 3px solid rgba(255, 255, 255, 0.1);
                border-top-color: var(--primary-color);
                border-radius: 50%;
                animation: spin 1s linear infinite;
            }
            @keyframes spin {
                to { transform: rotate(360deg); }
            }
        `;

        if (!document.querySelector('#loader-styles')) {
            style.id = 'loader-styles';
            document.head.appendChild(style);
        }

        if (container) {
            container.innerHTML = '';
            container.appendChild(loader);
        }

        return loader;
    },

    hideLoader(loader) {
        if (loader && loader.parentNode) {
            loader.remove();
        }
    },

    formatCurrency(amount) {
        return `KES ${amount.toLocaleString()}`;
    },

    formatDate(dateString) {
        const date = new Date(dateString);
        return date.toLocaleDateString('en-KE', {
            year: 'numeric',
            month: 'short',
            day: 'numeric'
        });
    },

    formatDateTime(dateString) {
        const date = new Date(dateString);
        return date.toLocaleDateString('en-KE', {
            year: 'numeric',
            month: 'short',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        });
    },

    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },

    validatePhone(phone) {
        const phoneRegex = /^(?:254|\+254|0)?([17]\d{8})$/;
        return phoneRegex.test(phone.replace(/\s/g, ''));
    },

    validatePassword(password) {
        return password.length >= 6;
    },

    animateValue(element, start, end, duration) {
        const range = end - start;
        const startTime = performance.now();

        const animate = (currentTime) => {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            const easeProgress = 1 - Math.pow(1 - progress, 3);
            const current = Math.floor(start + range * easeProgress);

            element.textContent = `KES ${current.toLocaleString()}`;

            if (progress < 1) {
                requestAnimationFrame(animate);
            }
        };

        requestAnimationFrame(animate);
    },

    smoothScroll(target) {
        const element = document.querySelector(target);
        if (element) {
            element.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    }
};

document.addEventListener('DOMContentLoaded', () => {
    UI.init();
});

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        UI.smoothScroll(this.getAttribute('href'));
    });
});

if (typeof module !== 'undefined' && module.exports) {
    module.exports = UI;
}
