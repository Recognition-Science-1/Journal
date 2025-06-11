# 🚀 DEPLOY RECOGNITION SCIENCE JOURNAL TO LIVE WEBSITE

## Overview
This guide will help you replace the current recognitionjournal.com website with the new 6-layer truth ledger system.

## 📦 Deployment Package
**File:** `recognition-science-journal-20250609-225731.tar.gz`
**Size:** ~300KB total
**Contains:** All files needed for the new website

## 🎯 What You're Deploying

### New Website Features:
- **Brutalist Design** - Clean, minimal, academic aesthetic (as Jonathan requested)
- **Live Truth Ledger** - 6-layer machine-verifiable system
- **Reality Crawler** - Autonomous data validation
- **Uncertainty Pruner** - Contradiction detection
- **System Dashboard** - Real-time monitoring
- **Expandable Axioms** - Interactive 8 foundational principles

### Core Files:
- `index.html` - New homepage with expandable axioms
- `journal.html` - Live truth ledger interface
- `truth-packets.html` - Real-time packet browser
- `system-dashboard.html` - System monitoring dashboard
- `truth-ledger.js` - Core ledger functionality
- `reality-crawler.js` - Data ingestion system
- `uncertainty-pruner.js` - Contradiction detection

## 📋 Deployment Steps

### Option 1: Manual Upload (Recommended)

1. **Backup Current Site**
   ```bash
   # Download current recognitionjournal.com files as backup
   # Store in a safe location before proceeding
   ```

2. **Extract Deployment Package**
   ```bash
   tar -xzf recognition-science-journal-20250609-225731.tar.gz
   ```

3. **Upload Files**
   - Use your hosting provider's file manager (cPanel, etc.)
   - Or use FTP client (FileZilla, etc.)
   - Upload ALL files to the root directory of recognitionjournal.com
   - Ensure `index.html` becomes the main page

4. **Verify Upload**
   - Check that all .js files are uploaded correctly
   - Ensure proper file permissions (644 for files, 755 for directories)

### Option 2: FTP Upload
```bash
# Example FTP commands (adjust for your hosting)
ftp your-hosting-server.com
# Login with your credentials
cd public_html  # or httpdocs, www, etc.
mput *.html
mput *.js
quit
```

### Option 3: cPanel File Manager
1. Login to your hosting cPanel
2. Open File Manager
3. Navigate to public_html (or your domain's root folder)
4. Upload the deployment package
5. Extract it in the file manager
6. Move all files to the root directory

## 🔧 Post-Deployment Configuration

### 1. Web Server Settings
Ensure your web server serves JavaScript files with correct MIME type:
```
.js files should be served as application/javascript
```

### 2. HTTPS Setup
- Enable HTTPS if not already active
- Update any HTTP links to HTTPS

### 3. DNS/CDN
- Clear any CDN cache (Cloudflare, etc.)
- DNS propagation may take up to 24 hours

## ✅ Testing Checklist

After deployment, test these URLs:

- [ ] **Main Site:** https://recognitionjournal.com
  - Should show brutalist Recognition Science homepage
  - 8 axioms should be expandable when clicked
  - Clean monospace typography

- [ ] **Truth Ledger:** https://recognitionjournal.com/journal.html
  - Should show 6-layer architecture
  - Submit form should be functional
  - Layer status indicators should work

- [ ] **Truth Packets:** https://recognitionjournal.com/truth-packets.html
  - Should show live packet browser
  - Filtering should work
  - Real-time updates should function

- [ ] **System Dashboard:** https://recognitionjournal.com/system-dashboard.html
  - Should show comprehensive monitoring
  - Start/stop buttons should work
  - Real-time metrics should update

## 🎯 Expected Results

### Before (Old Site):
- Traditional academic website
- Static content
- No interactive features

### After (New Site):
- **Brutalist design** - minimal, clean, academic
- **Live truth ledger** - interactive 6-layer system
- **Real-time monitoring** - system dashboard
- **Machine verification** - proof submission system
- **Reality crawler** - autonomous data validation
- **Contradiction detection** - uncertainty pruning

## 🚨 Troubleshooting

### JavaScript Not Working
- Check browser console for errors
- Ensure .js files uploaded correctly
- Verify MIME type configuration

### Styling Issues
- Check that CSS is embedded in HTML files
- Clear browser cache
- Verify file permissions

### 404 Errors
- Ensure all files are in the root directory
- Check file names match exactly (case-sensitive)
- Verify index.html is the default page

## 📞 Support

If you encounter issues:
1. Check browser developer console for errors
2. Verify all files uploaded successfully
3. Test on multiple browsers
4. Clear cache and try again

## 🎉 Success!

Once deployed, recognitionjournal.com will showcase:
- Jonathan's Recognition Science theory
- The world's first live truth ledger
- Machine-verifiable scientific publishing
- Reality debugging its own source code

**The future of science publishing is now live!** 🚀 