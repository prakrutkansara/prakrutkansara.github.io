# 🚀 Deployment Guide - GitHub Pages + Hugging Face Spaces

## Part 1: Deploy Dashboard to Hugging Face Spaces

### Step 1: Create Hugging Face Account
1. Go to https://huggingface.co/join
2. Sign up for a free account

### Step 2: Create a New Space
1. Click your profile → "New Space"
2. Fill in:
   - **Space name**: `nasa-geoss2s-dashboard` (or your choice)
   - **License**: MIT
   - **SDK**: Docker
   - **Hardware**: CPU basic (free)
3. Click "Create Space"

### Step 3: Upload Dashboard Files
In your new Space, upload these files from `dashboard/` folder:

```
dashboard/
├── Dockerfile           # ← Upload this
├── app_hf.py           # ← Rename to app.py when uploading
├── requirements.txt    # ← Upload this
├── README_HF.md        # ← Rename to README.md when uploading
└── data/
    └── nmme_nasa_geoss2s_prec_2025_01_01.nc  # ← Upload this
```

**Important:** 
- Rename `app_hf.py` → `app.py`
- Rename `README_HF.md` → `README.md`
- Create `data/` folder and upload the NetCDF file there

### Step 4: Wait for Build
- Hugging Face will automatically build and deploy
- Check the "Build" tab for progress (takes ~5-10 minutes)
- Once done, you'll see "Running" status

### Step 5: Get Your Dashboard URL
Your dashboard will be at: `https://huggingface.co/spaces/YOUR_USERNAME/nasa-geoss2s-dashboard`

---

## Part 2: Deploy Hugo Site to GitHub Pages

### Step 1: Create GitHub Repository
1. Go to https://github.com/new
2. Create repo: `YOUR_USERNAME.github.io` (or any name)
3. Make it **Public**
4. Don't initialize with README

### Step 2: Push Your Code
In your terminal:

```bash
cd /Users/prakrut/sites/hugonewsite

# Configure git
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Commit everything
git commit -m "Initial commit - S2S Geospatial site"

# Add GitHub remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages
1. Go to your repo on GitHub
2. Settings → Pages
3. Source: "GitHub Actions"
4. The workflow `.github/workflows/hugo.yml` will auto-deploy

### Step 4: Wait for Deployment
- Check "Actions" tab for build progress (~2-3 minutes)
- Once green ✓, site is live at: `https://YOUR_USERNAME.github.io/REPO_NAME/`

---

## Part 3: Connect Dashboard to Hugo Site

### Update iframe URL

Once your Hugging Face Space is running, update the Hugo site:

```bash
# Edit content/dashboard/index.md
# Change the iframe src from:
# http://localhost:8050
# to:
# https://huggingface.co/spaces/YOUR_USERNAME/nasa-geoss2s-dashboard
```

Then push the update:

```bash
git add content/dashboard/index.md
git commit -m "Update dashboard URL to Hugging Face Space"
git push
```

GitHub Actions will automatically rebuild and redeploy.

---

## 🔧 Troubleshooting

### Hugging Face Space Issues

**Problem: Build fails**
- Check Build logs in the "Build" tab
- Ensure all files are uploaded correctly
- Verify Dockerfile syntax

**Problem: Dashboard shows blank page**
- Check "Logs" tab for Python errors
- Ensure NetCDF file is in `data/` folder
- Verify port 7860 is used

### GitHub Pages Issues

**Problem: Workflow fails**
- Check "Actions" tab for error messages
- Ensure PaperMod submodule is committed: `git submodule update --init --recursive`
- Verify `hugo.yml` workflow file exists

**Problem: Site not updating**
- Check if workflow ran successfully in Actions tab
- Clear browser cache
- Wait 2-3 minutes for CDN to refresh

---

## 📝 Quick Checklist

### Hugging Face Spaces ✓
- [ ] Account created
- [ ] Space created with Docker SDK
- [ ] `Dockerfile` uploaded
- [ ] `app.py` uploaded (renamed from `app_hf.py`)
- [ ] `requirements.txt` uploaded
- [ ] `data/` folder created
- [ ] NetCDF file uploaded to `data/`
- [ ] Build completed successfully
- [ ] Dashboard loads in browser

### GitHub Pages ✓
- [ ] GitHub repo created
- [ ] Code pushed to GitHub
- [ ] GitHub Pages enabled (Actions)
- [ ] Workflow ran successfully
- [ ] Site loads at GitHub Pages URL
- [ ] Dashboard iframe updated with HF Space URL
- [ ] Dashboard loads within Hugo site

---

## 🎉 Final URLs

After successful deployment:

- **Hugo Site**: `https://YOUR_USERNAME.github.io/REPO_NAME/`
- **Dashboard**: `https://huggingface.co/spaces/YOUR_USERNAME/SPACE_NAME`

Share these links to showcase your research!

---

## 💰 Cost

Both deployments are **100% FREE**:
- GitHub Pages: Unlimited static hosting
- Hugging Face Spaces: Free CPU tier (sufficient for this dashboard)

---

## 🔄 Future Updates

To update your site:

```bash
# Make changes locally
git add -A
git commit -m "Description of changes"
git push

# GitHub Actions automatically redeploys
```

To update dashboard:
1. Go to your HF Space
2. Click "Files" → Upload new files
3. Auto-rebuilds on file change

---

Need help? Check:
- GitHub Pages: https://docs.github.com/pages
- Hugging Face Spaces: https://huggingface.co/docs/hub/spaces
