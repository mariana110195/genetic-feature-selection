/**
 * Main JavaScript File
 * Genetic Algorithm Feature Selection Project
 * Developed by: Student 4 (Frontend Developer)
 */

// Global variables
let uploadedFile = null;
let gaResults = null;

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    console.log('GA Feature Selection App Initialized');
    initializeApp();
});

/**
 * Initialize the application
 */
function initializeApp() {
    // Add fade-in animations to main containers
    document.querySelectorAll('.main-container').forEach(el => {
        el.classList.add('fade-in');
    });
    
    // Add smooth scroll behavior
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

/**
 * Show loading overlay
 */
function showLoading(message = 'Processing...') {
    const overlay = document.createElement('div');
    overlay.id = 'loadingOverlay';
    overlay.className = 'loading-overlay';
    overlay.innerHTML = `
        <div class="loading-content">
            <div class="loading-spinner"></div>
            <h4 class="mt-3">${message}</h4>
        </div>
    `;
    document.body.appendChild(overlay);
}

/**
 * Hide loading overlay
 */
function hideLoading() {
    const overlay = document.getElementById('loadingOverlay');
    if (overlay) {
        overlay.remove();
    }
}

/**
 * Show notification
 */
function showNotification(message, type = 'info') {
    const alertClass = `alert-${type}-custom`;
    const notification = document.createElement('div');
    notification.className = `alert ${alertClass} alert-dismissible fade show`;
    notification.style.position = 'fixed';
    notification.style.top = '20px';
    notification.style.right = '20px';
    notification.style.zIndex = '10000';
    notification.style.minWidth = '300px';
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.body.appendChild(notification);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        notification.remove();
    }, 5000);
}

/**
 * Format number with commas
 */
function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

/**
 * Calculate percentage
 */
function calculatePercentage(value, total) {
    if (total === 0) return 0;
    return ((value / total) * 100).toFixed(2);
}

/**
 * Validate file before upload
 */
function validateFile(file) {
    const validExtensions = ['csv', 'xlsx', 'xls'];
    const fileExtension = file.name.split('.').pop().toLowerCase();
    
    if (!validExtensions.includes(fileExtension)) {
        showNotification('Invalid file type. Please upload CSV or Excel file.', 'danger');
        return false;
    }
    
    // Check file size (max 16MB)
    const maxSize = 16 * 1024 * 1024;
    if (file.size > maxSize) {
        showNotification('File is too large. Maximum size is 16MB.', 'danger');
        return false;
    }
    
    return true;
}

/**
 * Upload file to server
 */
async function uploadFile(file) {
    if (!validateFile(file)) {
        return null;
    }
    
    const formData = new FormData();
    formData.append('file', file);
    
    try {
        showLoading('Uploading file...');
        
        const response = await fetch('/api/upload', {
            method: 'POST',
            body: formData
        });
        
        hideLoading();
        
        if (!response.ok) {
            throw new Error('Upload failed');
        }
        
        const data = await response.json();
        
        if (data.success || data.filename) {
            showNotification('File uploaded successfully!', 'success');
            uploadedFile = data;
            return data;
        } else {
            throw new Error(data.error || 'Upload failed');
        }
        
    } catch (error) {
        hideLoading();
        showNotification(`Upload error: ${error.message}`, 'danger');
        return null;
    }
}

/**
 * Run Genetic Algorithm
 */
async function runGeneticAlgorithm(params) {
    try {
        showLoading('Running Genetic Algorithm... This may take a few minutes.');
        
        const response = await fetch('/api/run-ga', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(params)
        });
        
        hideLoading();
        
        if (!response.ok) {
            throw new Error('GA execution failed');
        }
        
        const data = await response.json();
        
        if (data.success) {
            showNotification('Genetic Algorithm completed successfully!', 'success');
            gaResults = data;
            return data;
        } else {
            throw new Error(data.error || 'GA execution failed');
        }
        
    } catch (error) {
        hideLoading();
        showNotification(`GA Error: ${error.message}`, 'danger');
        return null;
    }
}

/**
 * Run comparison analysis
 */
async function runComparison() {
    try {
        showLoading('Running comparison analysis...');
        
        const response = await fetch('/api/comparison', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({})
        });
        
        hideLoading();
        
        if (!response.ok) {
            throw new Error('Comparison failed');
        }
        
        const data = await response.json();
        
        if (data.success) {
            showNotification('Comparison completed successfully!', 'success');
            return data;
        } else {
            throw new Error(data.error || 'Comparison failed');
        }
        
    } catch (error) {
        hideLoading();
        showNotification(`Comparison Error: ${error.message}`, 'danger');
        return null;
    }
}

/**
 * Export results to CSV
 */
function exportToCSV(data, filename = 'results.csv') {
    const csv = convertToCSV(data);
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    window.URL.revokeObjectURL(url);
    showNotification('Results exported successfully!', 'success');
}

/**
 * Convert data to CSV format
 */
function convertToCSV(data) {
    // Simple CSV conversion
    // This can be enhanced based on data structure
    let csv = '';
    
    if (Array.isArray(data)) {
        // Array of objects
        if (data.length > 0) {
            // Header
            csv += Object.keys(data[0]).join(',') + '\n';
            
            // Rows
            data.forEach(row => {
                csv += Object.values(row).join(',') + '\n';
            });
        }
    } else if (typeof data === 'object') {
        // Single object
        csv += Object.keys(data).join(',') + '\n';
        csv += Object.values(data).join(',') + '\n';
    }
    
    return csv;
}

/**
 * Create chart using Chart.js
 */
function createChart(canvasId, config) {
    const ctx = document.getElementById(canvasId);
    if (!ctx) {
        console.error(`Canvas ${canvasId} not found`);
        return null;
    }
    
    return new Chart(ctx, config);
}

/**
 * Update chart data
 */
function updateChart(chart, newData) {
    if (!chart) return;
    
    chart.data = newData;
    chart.update();
}

/**
 * Animate numbers (count up effect)
 */
function animateNumber(element, targetValue, duration = 1000) {
    const startValue = 0;
    const startTime = performance.now();
    
    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        const currentValue = startValue + (targetValue - startValue) * progress;
        element.textContent = Math.floor(currentValue);
        
        if (progress < 1) {
            requestAnimationFrame(update);
        }
    }
    
    requestAnimationFrame(update);
}

/**
 * Debounce function
 */
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

/**
 * Utility: Get query parameter
 */
function getQueryParameter(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
}

/**
 * Utility: Copy to clipboard
 */
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showNotification('Copied to clipboard!', 'info');
    }).catch(err => {
        console.error('Failed to copy:', err);
    });
}

// Export functions for use in other scripts
window.GAApp = {
    showLoading,
    hideLoading,
    showNotification,
    uploadFile,
    runGeneticAlgorithm,
    runComparison,
    exportToCSV,
    createChart,
    updateChart,
    animateNumber,
    formatNumber,
    calculatePercentage
};

