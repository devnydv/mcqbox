// Main JavaScript file for MCQ Dashboard

// Initialize application
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
    
    // Add loading states to forms
    const forms = document.querySelectorAll('form');
    forms.forEach(function(form) {
        form.addEventListener('submit', function() {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                const originalText = submitBtn.textContent;
                submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status"></span>Processing...';
                
                // Re-enable after 10 seconds as fallback
                setTimeout(function() {
                    submitBtn.disabled = false;
                    submitBtn.textContent = originalText;
                }, 10000);
            }
        });
    });
    
    // Confirm delete operations
    const deleteButtons = document.querySelectorAll('button[onclick*="confirm"]');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            const confirmMessage = button.getAttribute('onclick').match(/'([^']+)'/)[1];
            if (!confirm(confirmMessage)) {
                e.preventDefault();
                e.stopPropagation();
                return false;
            }
        });
    });
});

// Utility functions
function showLoading(element) {
    if (element) {
        element.innerHTML = '<div class="text-center"><div class="spinner-border" role="status"><span class="visually-hidden">Loading...</span></div></div>';
    }
}

function showError(element, message) {
    if (element) {
        element.innerHTML = `<div class="alert alert-danger">${message}</div>`;
    }
}

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Form validation helpers
function validateRequired(input) {
    const value = input.value.trim();
    const isValid = value.length > 0;
    
    input.classList.toggle('is-invalid', !isValid);
    input.classList.toggle('is-valid', isValid);
    
    return isValid;
}

function validateEmail(input) {
    const value = input.value.trim();
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const isValid = emailRegex.test(value);
    
    input.classList.toggle('is-invalid', !isValid);
    input.classList.toggle('is-valid', isValid);
    
    return isValid;
}

// Modal helpers
function resetModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        const form = modal.querySelector('form');
        if (form) {
            form.reset();
            // Remove validation classes
            const inputs = form.querySelectorAll('.form-control, .form-select');
            inputs.forEach(input => {
                input.classList.remove('is-valid', 'is-invalid');
            });
        }
    }
}

// API helper functions
async function fetchJSON(url, options = {}) {
    try {
        const response = await fetch(url, {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            },
            ...options
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    } catch (error) {
        console.error('Fetch error:', error);
        throw error;
    }
}

// Table helpers
function sortTable(table, column, direction = 'asc') {
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));
    
    rows.sort((a, b) => {
        const aVal = a.children[column].textContent.trim();
        const bVal = b.children[column].textContent.trim();
        
        if (direction === 'asc') {
            return aVal.localeCompare(bVal);
        } else {
            return bVal.localeCompare(aVal);
        }
    });
    
    rows.forEach(row => tbody.appendChild(row));
}

function filterTable(table, searchTerm) {
    const tbody = table.querySelector('tbody');
    const rows = tbody.querySelectorAll('tr');
    
    rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        const matches = text.includes(searchTerm.toLowerCase());
        row.style.display = matches ? '' : 'none';
    });
}

// Export utility functions globally
window.MCQDashboard = {
    showLoading,
    showError,
    debounce,
    validateRequired,
    validateEmail,
    resetModal,
    fetchJSON,
    sortTable,
    filterTable
};
