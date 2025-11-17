# S2S Geospatial - NASA GEOSS2S Precipitation Forecasts

Personal research website showcasing seasonal-to-subseasonal hydrological forecasting and climate-health research.

## 🚀 Deployment

This site is deployed using:
- **GitHub Pages** - Hugo static site
- **Hugging Face Spaces** - Panel dashboard

## 📦 Local Development

### Hugo Site
```bash
hugo server -D
# Visit http://localhost:1313
```

### Panel Dashboard
```bash
cd dashboard
pip install -r requirements.txt
python app.py
# Visit http://localhost:8050
```

## 🌐 Live Site

- **Website**: [Your GitHub Pages URL]
- **Dashboard**: [Your Hugging Face Space URL]

## 📁 Project Structure

```
.
├── content/          # Hugo content (markdown)
├── static/           # Static assets
├── themes/PaperMod/  # Hugo theme
├── dashboard/        # Panel dashboard
│   ├── app.py       # Dashboard code
│   ├── data/        # NetCDF files
│   └── requirements.txt
└── .github/workflows/hugo.yml  # GitHub Actions
```

## 🔧 Tech Stack

- Hugo + PaperMod theme
- Panel + HoloViews + GeoViews
- xarray for NetCDF data
- Leaflet.js for maps

## 📊 Data

NASA GEOSS2S precipitation forecasts for South America
- Source: NMME Multi-Model Ensemble
- Coverage: -95°W to -34°W, -57°S to 19°N
- Temporal: Monthly forecasts, 0.5-8.5 month lead times

## 👤 Author

Prakrut Kansara, Ph.D.  
Assistant Research Scientist  
Johns Hopkins University
