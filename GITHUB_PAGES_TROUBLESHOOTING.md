# GitHub Pages Deployment Troubleshooting Guide

## Quick Diagnostic Commands

```bash
# 1. Check if your changes are pushed
git status
git log --oneline -5

# 2. Check when the live site was last updated
curl -I https://YOUR-DOMAIN.com | grep -i "last-modified"

# 3. Check if your changes are live
curl -s https://YOUR-DOMAIN.com | grep "YOUR-UNIQUE-CONTENT"

# 4. Check GitHub Actions status
echo "Go to: https://github.com/YOUR-ORG/YOUR-REPO/actions"
```

## Common Issues & Solutions

### ❌ Issue 1: Changes pushed but not showing on live site

**Symptoms:**
- Git shows changes are pushed
- Live site shows old content
- No visible errors

**Solutions:**
1. Check GitHub Pages settings (`Settings > Pages`)
2. Verify "Source" is configured:
   - Either "Deploy from a branch" with branch selected
   - Or "GitHub Actions" with workflow file
3. If using branch deployment, ensure branch is set (not "None")

### ❌ Issue 2: GitHub Actions workflow exists but not running

**Symptoms:**
- `.github/workflows/deploy.yml` exists
- No workflow runs in Actions tab
- Site not updating

**Solutions:**
1. Change Pages source to "Deploy from a branch"
2. Or fix workflow permissions:
   ```yaml
   permissions:
     contents: read
     pages: write
     id-token: write
   ```

### ❌ Issue 3: Caching issues

**Symptoms:**
- Random users see old content
- Hard refresh sometimes works
- Inconsistent behavior

**Solutions:**
```bash
# Force deployment with timestamp
echo "Deploy: $(date)" > .deploy-timestamp
git add . && git commit -m "Force cache clear" && git push

# Check cache headers
curl -I https://YOUR-DOMAIN.com | grep -i "cache"
```

## Emergency Fix Procedure

1. **Go to GitHub Pages settings**
   ```
   https://github.com/YOUR-ORG/YOUR-REPO/settings/pages
   ```

2. **Enable branch deployment**
   - Source: Deploy from a branch
   - Branch: main
   - Folder: / (root)
   - Save

3. **Force new deployment**
   ```bash
   git commit --allow-empty -m "Force GitHub Pages rebuild"
   git push origin main
   ```

4. **Wait 5-10 minutes**

5. **Verify deployment**
   ```bash
   curl -s https://YOUR-DOMAIN.com | grep -q "old-content" && echo "❌ Not updated" || echo "✅ Updated!"
   ```

## Pro Tips

- 🔍 Always check Pages settings FIRST
- 🚀 Use empty commits to force rebuilds
- 📊 Monitor with curl, not browser (avoids cache)
- ⏰ GitHub Pages can take 10+ minutes sometimes
- 🔄 Switch deployment methods if one fails

## When All Else Fails

1. Delete `.github/workflows` temporarily
2. Use simple branch deployment
3. Once working, re-add GitHub Actions if needed
4. Document what worked for future reference!

---
*Remember: It's usually a configuration issue, not a code issue!* 