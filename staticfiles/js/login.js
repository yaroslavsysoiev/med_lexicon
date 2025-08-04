// Login page JavaScript enhancements
document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.querySelector('.login-form');
    const loginBtn = document.querySelector('.login-btn');
    const usernameInput = document.querySelector('input[name="username"]');
    const passwordInput = document.querySelector('input[name="password"]');
    const alerts = document.querySelectorAll('.alert');

    // Auto-hide alerts after 5 seconds
    alerts.forEach(alert => {
        setTimeout(() => {
            if (alert) {
                alert.style.transition = 'opacity 0.5s ease';
                alert.style.opacity = '0';
                setTimeout(() => {
                    alert.remove();
                }, 500);
            }
        }, 5000);
    });

    // Manual alert dismissal
    document.querySelectorAll('.close').forEach(closeBtn => {
        closeBtn.addEventListener('click', function() {
            const alert = this.closest('.alert');
            alert.style.transition = 'opacity 0.3s ease';
            alert.style.opacity = '0';
            setTimeout(() => {
                alert.remove();
            }, 300);
        });
    });

    // Real-time form validation
    function validateForm() {
        let isValid = true;
        const username = usernameInput.value.trim();
        const password = passwordInput.value.trim();

        // Remove previous error states
        document.querySelectorAll('.is-invalid').forEach(el => {
            el.classList.remove('is-invalid');
        });

        // Username validation
        if (!username) {
            usernameInput.classList.add('is-invalid');
            showFieldError(usernameInput, 'Username is required');
            isValid = false;
        } else if (username.length < 3) {
            usernameInput.classList.add('is-invalid');
            showFieldError(usernameInput, 'Username must be at least 3 characters');
            isValid = false;
        }

        // Password validation
        if (!password) {
            passwordInput.classList.add('is-invalid');
            showFieldError(passwordInput, 'Password is required');
            isValid = false;
        } else if (password.length < 6) {
            passwordInput.classList.add('is-invalid');
            showFieldError(passwordInput, 'Password must be at least 6 characters');
            isValid = false;
        }

        return isValid;
    }

    // Show field-specific error messages
    function showFieldError(field, message) {
        // Remove existing error message
        const existingError = field.parentNode.querySelector('.field-error');
        if (existingError) {
            existingError.remove();
        }

        // Create new error message
        const errorDiv = document.createElement('div');
        errorDiv.className = 'field-error text-danger mt-1';
        errorDiv.style.fontSize = '0.875rem';
        errorDiv.innerHTML = `<i class="fas fa-exclamation-circle"></i> ${message}`;
        field.parentNode.appendChild(errorDiv);
    }

    // Clear field errors on input
    [usernameInput, passwordInput].forEach(input => {
        input.addEventListener('input', function() {
            this.classList.remove('is-invalid');
            const errorDiv = this.parentNode.querySelector('.field-error');
            if (errorDiv) {
                errorDiv.remove();
            }
        });

        // Add focus effects
        input.addEventListener('focus', function() {
            this.parentNode.classList.add('focused');
        });

        input.addEventListener('blur', function() {
            this.parentNode.classList.remove('focused');
        });
    });

    // Form submission with loading state
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            if (!validateForm()) {
                e.preventDefault();
                return;
            }

            // Show loading state
            loginBtn.disabled = true;
            loginBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Logging in...';
            
            // Add loading animation to card
            const loginCard = document.querySelector('.login-card');
            loginCard.style.opacity = '0.8';
        });
    }

    // Password visibility toggle
    const passwordToggle = document.createElement('button');
    passwordToggle.type = 'button';
    passwordToggle.className = 'btn btn-link password-toggle';
    passwordToggle.innerHTML = '<i class="fas fa-eye"></i>';
    passwordToggle.style.position = 'absolute';
    passwordToggle.style.right = '10px';
    passwordToggle.style.top = '50%';
    passwordToggle.style.transform = 'translateY(-50%)';
    passwordToggle.style.border = 'none';
    passwordToggle.style.background = 'none';
    passwordToggle.style.color = '#667eea';

    if (passwordInput) {
        passwordInput.parentNode.style.position = 'relative';
        passwordInput.parentNode.appendChild(passwordToggle);

        passwordToggle.addEventListener('click', function() {
            const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            passwordInput.setAttribute('type', type);
            this.innerHTML = type === 'password' ? '<i class="fas fa-eye"></i>' : '<i class="fas fa-eye-slash"></i>';
        });
    }

    // Enter key to submit form
    [usernameInput, passwordInput].forEach(input => {
        input.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                loginForm.dispatchEvent(new Event('submit'));
            }
        });
    });

    // Add floating label effect
    [usernameInput, passwordInput].forEach(input => {
        input.addEventListener('focus', function() {
            this.parentNode.classList.add('has-focus');
        });

        input.addEventListener('blur', function() {
            if (!this.value) {
                this.parentNode.classList.remove('has-focus');
            }
        });

        // Check if field has value on load
        if (input.value) {
            input.parentNode.classList.add('has-focus');
        }
    });

    // Add subtle animations
    const loginCard = document.querySelector('.login-card');
    if (loginCard) {
        loginCard.style.opacity = '0';
        loginCard.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            loginCard.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            loginCard.style.opacity = '1';
            loginCard.style.transform = 'translateY(0)';
        }, 100);
    }

    // Add typing animation to title
    const loginTitle = document.querySelector('.login-title');
    if (loginTitle) {
        const text = loginTitle.textContent;
        loginTitle.textContent = '';
        loginTitle.style.borderRight = '2px solid #667eea';
        
        let i = 0;
        const typeWriter = () => {
            if (i < text.length) {
                loginTitle.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            } else {
                loginTitle.style.borderRight = 'none';
            }
        };
        
        setTimeout(typeWriter, 500);
    }
});

// Add CSS for new features
const style = document.createElement('style');
style.textContent = `
    .field-error {
        animation: shake 0.5s ease-in-out;
    }

    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        25% { transform: translateX(-5px); }
        75% { transform: translateX(5px); }
    }

    .form-group.focused .form-label {
        color: #667eea;
        transform: translateY(-2px);
        transition: all 0.3s ease;
    }

    .password-toggle:hover {
        color: #5a6fd8 !important;
    }

    .login-card {
        animation: fadeInUp 0.6s ease;
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .login-btn:disabled {
        background: #6c757d !important;
        transform: none !important;
        box-shadow: none !important;
    }
`;
document.head.appendChild(style); 