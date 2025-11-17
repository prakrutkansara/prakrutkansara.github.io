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

<iframe src="https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME" style="width:100%; height:900px; border:2px solid #e5e7eb; border-radius: 12px; box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);"></iframe>

---

### Setup Instructions

**Dashboard is deployed on Hugging Face Spaces**

Update the iframe URL above after deploying to Hugging Face.

Replace:
- `YOUR_USERNAME` with your Hugging Face username
- `YOUR_SPACE_NAME` with your space name (e.g., `nasa-geoss2s-dashboard`)

### Technical Stack

- **Dash/Plotly** for interactive visualization
- **xarray** for NetCDF data handling
- **cartopy/geopandas** for geospatial plotting
- **NumPy/pandas** for data processing
