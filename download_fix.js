// Enhanced download functionality
document.addEventListener('DOMContentLoaded', function() {
    console.log('Download fix script loaded');
    
    // Function to force download
    function forceDownload(url, filename) {
        console.log('Attempting to download:', url);
        
        // Method 1: Create temporary link
        const link = document.createElement('a');
        link.href = url;
        link.download = filename || url.split('/').pop();
        link.style.display = 'none';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        
        // Method 2: Open in new window as fallback
        setTimeout(() => {
            window.open(url, '_blank');
        }, 100);
    }
    
    // Add click handlers to download buttons
    const downloadButtons = document.querySelectorAll('.action-btn.download, .action-btn.lean-proof');
    console.log('Found download buttons:', downloadButtons.length);
    
    downloadButtons.forEach((button, index) => {
        console.log('Setting up button', index, button.href);
        
        button.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            const url = this.getAttribute('href');
            console.log('Button clicked, downloading:', url);
            
            if (url) {
                forceDownload(url);
            }
            
            return false;
        });
    });
}); 