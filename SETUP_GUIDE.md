# S2S Geospatial Hugo Site - Complete Setup Guide

## 🎉 Your Site is Ready!

Your personalized Hugo website with integrated Python dashboard is now set up.

## 📁 Site Structure

```
hugonewsite/
├── config.toml              # Site configuration
├── content/
│   ├── _index.md           # Home page
│   ├── about/              # About page with your bio
│   ├── posts/              # Research posts
│   ├── maps/               # Interactive Leaflet map
│   └── dashboard/          # Dashboard integration page
├── dashboard/
│   ├── app.py              # Dash application (READY TO USE!)
│   ├── requirements.txt    # Python dependencies
│   ├── README.md           # Dashboard setup guide
│   └── data/               # Place NetCDF files here
├── static/
│   └── images/
│       └── profile.jpg     # Your profile photo
├── assets/css/extended/
│   └── custom.css          # Custom styling
└── themes/PaperMod/        # Hugo theme

```

## 🚀 Quick Start

### 1. Start Hugo Site

```bash
cd /Users/prakrut/sites/hugonewsite
hugo server -D
```

Access at: http://localhost:1313

### 2. Start Dashboard (Optional)

```bash
cd /Users/prakrut/sites/hugonewsite/dashboard
pip install -r requirements.txt
python app.py
```

Access at: http://localhost:8050

## ✨ Features Included

### Hugo Site
- ✅ Profile mode with your photo and credentials
- ✅ Custom purple-blue gradient color scheme
- ✅ Interactive maps with colored markers for 4 research regions
- ✅ Research content from your CV
- ✅ Responsive design with PaperMod theme
- ✅ Custom CSS with hover effects

### Dashboard
- ✅ Interactive NetCDF visualization
- ✅ Time slider for temporal data
- ✅ Spatial heatmaps with Plotly
- ✅ Click-to-select time series plots
- ✅ Real-time statistics panel
- ✅ Sample data generation (no NetCDF needed to test)
- ✅ Embedded in Hugo site via iframe

## 📊 Dashboard Usage

### With Your Data

1. Add NetCDF files to `dashboard/data/`:
   ```bash
   cp your_forecast.nc /Users/prakrut/sites/hugonewsite/dashboard/data/
   ```

2. NetCDF requirements:
   - Dimensions: `time`, `lat`, `lon`
   - Variables: any gridded forecast data
   - CF-compliant format

### Without Data (Demo Mode)

The dashboard automatically generates sample data if no NetCDF files are found.

## 🎨 Customization

### Colors

Edit `assets/css/extended/custom.css`:
- Primary: `#667eea` (purple-blue)
- Secondary: `#10b981` (green)
- Accent: `#f59e0b` (orange)

### Content

Edit markdown files in `content/`:
- Home: `content/_index.md`
- About: `content/about/index.md`
- Posts: `content/posts/`
- Maps: `content/maps/index.md`
- Dashboard: `content/dashboard/index.md`

### Menu

Edit `config.toml` under `[menu.main]` section.

## 🔧 Dashboard Customization

### Add Variables

Edit `dashboard/app.py`:

```python
# Add custom colorscales
if variable == 'your_variable':
    colorscale = 'Viridis'
```

### Change Domain

Update spatial extent:

```python
lats = np.linspace(your_min_lat, your_max_lat, resolution)
lons = np.linspace(your_min_lon, your_max_lon, resolution)
```

### Add Features

- Export data: Add download button
- Animations: Use `dcc.Interval`
- Multiple datasets: Use `xr.concat()`

## 🌐 Deployment

### Hugo Site

**Netlify:**
1. Push to GitHub
2. Connect repo to Netlify
3. Build command: `hugo -D`
4. Publish directory: `public`

**GitHub Pages:**
```bash
hugo
git add public/
git commit -m "Deploy site"
git push
```

### Dashboard

**Heroku:**
```bash
cd dashboard
echo "web: python app.py" > Procfile
heroku create your-dashboard
git push heroku main
```

**Update iframe in `content/dashboard/index.md`:**
```html
<iframe src="https://your-dashboard.herokuapp.com" ...>
```

## 📋 Next Steps

1. ✅ Site created with personalized content
2. ✅ Dashboard app ready to run
3. ⬜ Add your NetCDF forecast data
4. ⬜ Test dashboard locally
5. ⬜ Customize colors/content as needed
6. ⬜ Deploy to production

## 🛠️ Troubleshooting

### Hugo not building?
```bash
# Check for errors
hugo -v
# Clear cache
rm -rf public resources
```

### Dashboard not loading?
```bash
# Check dependencies
pip install -r requirements.txt
# Verify port
lsof -i :8050
```

### Profile photo not showing?
```bash
# Check file exists
ls -la static/images/profile.jpg
# Restart Hugo server
```

## 📞 Support

Dashboard implementation: See `dashboard/README.md`
Hugo theme docs: https://github.com/adityatelange/hugo-PaperMod/wiki
Dash documentation: https://dash.plotly.com/

## 🎯 Key Files Modified

1. `create_hugo_site.sh` - Site generation script (UPDATED)
2. `config.toml` - Added dashboard menu, profile mode
3. `content/dashboard/index.md` - Dashboard integration page (NEW)
4. `dashboard/app.py` - Complete Dash application (NEW)
5. `assets/css/extended/custom.css` - Custom styling (NEW)

Your site is production-ready! 🚀
