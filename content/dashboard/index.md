---
title: "Forecast Dashboard"
---

## Interactive NetCDF Forecast Visualization

Explore gridded forecast outputs with interactive controls for time, variable selection, and spatial analysis.

<div style="margin: 2rem 0; padding: 1rem; background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%); border-radius: 8px; border-left: 4px solid #667eea;">
  <p><strong>📊 Dashboard Features:</strong></p>
  <ul>
    <li>🌡️ Multi-variable display (temperature, precipitation, soil moisture)</li>
    <li>📅 Time series animation and selection</li>
    <li>🗺️ Interactive spatial plotting with Plotly</li>
    <li>📈 Statistical analysis and trend visualization</li>
  </ul>
</div>

<iframe src="https://prakrutkansara-hydroclimate-s2s.hf.space" style="width:100%; height:1200px; border:2px solid #e5e7eb; border-radius: 12px; box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);"></iframe>

<p style="margin-top: 1rem; text-align: center;">
<a href="https://huggingface.co/spaces/prakrutkansara/hydroclimate-s2s" target="_blank" style="display: inline-block; padding: 0.75rem 1.5rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; text-decoration: none; border-radius: 8px; font-weight: 600;">
🚀 Open Dashboard in New Tab
</a>
</p>

---

### About the Dashboard

**Interactive NASA GEOSS2S Precipitation Forecasts**

Explore seasonal precipitation forecasts for South America using NASA's GEOSS2S multi-model ensemble system.

**Features:**
- 🗺️ Interactive spatial maps with geographic context
- 📅 Monthly forecast lead times (0.5-8.5 months)
- 📊 Statistical analysis and distribution plots
- 📈 Time series visualization for any location

**Powered by:** Panel, HoloViews, GeoViews, and xarray

### Technical Stack

- **Dash/Plotly** for interactive visualization
- **xarray** for NetCDF data handling
- **cartopy/geopandas** for geospatial plotting
- **NumPy/pandas** for data processing
