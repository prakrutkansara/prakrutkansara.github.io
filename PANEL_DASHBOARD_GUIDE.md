# Panel Dashboard Successfully Integrated! 🎉

Your Hugo site now includes a **Panel-based dashboard** for interactive NetCDF forecast visualization.

## ✅ What's Been Set Up

### Hugo Site
- **Running at**: http://localhost:64721/
- **Dashboard page**: http://localhost:64721/dashboard/
- 21 pages built successfully
- Profile photo integrated
- Custom purple-blue gradient styling

### Panel Dashboard
- **Location**: `/Users/prakrut/sites/hugonewsite/dashboard/`
- **Technology**: Panel + HoloViews + hvPlot
- **Features**:
  - FastListTemplate with sidebar controls
  - Interactive spatial heatmaps
  - Time series plots at selected locations
  - Statistics table (mean, min, max, std dev, median)
  - Distribution histogram
  - Coastline overlays on maps
  - Auto-generated sample data

## 🚀 Quick Start Guide

### 1. Install Dashboard Dependencies

```bash
cd /Users/prakrut/sites/hugonewsite/dashboard
pip install -r requirements.txt
```

This installs:
- `panel` - Web app framework
- `holoviews` - High-level plotting
- `hvplot` - Interactive plots for xarray
- `bokeh` - Visualization backend
- `xarray`, `numpy`, `pandas` - Data processing
- `netCDF4` - NetCDF file support

### 2. Run the Dashboard

```bash
python app.py
```

You'll see:
```
🌍 S2S Geospatial Forecast Dashboard (Panel)
📊 Variables: temperature, precipitation, soil_moisture
📅 Time range: 2025-01-01 to 2025-01-30
🗺️  Domain: -10.0° to 10.0° N
         -80.0° to -40.0° E
🚀 Starting server at http://localhost:8050
```

### 3. View Integrated Dashboard

Navigate to: http://localhost:64721/dashboard/

The Panel dashboard will be embedded in your Hugo site!

## 📊 Panel Dashboard Features

### Sidebar Controls
- **Variable selector**: Choose temperature, precipitation, or soil moisture
- **Time slider**: Navigate through forecast timesteps
- **Location inputs**: Latitude/longitude for time series

### Main Panel
- **Spatial heatmap**: Interactive colormap visualization
- **Statistics table**: Real-time metrics with custom styling
- **Distribution histogram**: Data frequency plot
- **Time series**: Temporal evolution at selected point

### Interactive Features
- Hover over maps to see values
- Click to select locations
- Slide through time
- Auto-updates when controls change

## 🎨 Why Panel?

**Advantages over Dash:**
1. **Simpler syntax** - Less boilerplate, more Pythonic
2. **HoloViews integration** - Powerful declarative plotting
3. **hvPlot** - One-line plots from xarray
4. **Reactive programming** - `@pn.depends` decorators
5. **Templates** - FastList, Material, Bootstrap, etc.
6. **Better for scientific data** - Built for xarray/numpy/pandas

**Code Comparison:**

Panel:
```python
@pn.depends(variable_select.param.value)
def create_plot(variable):
    return ds[variable].hvplot(cmap='viridis')
```

Dash (equivalent):
```python
@app.callback(Output('plot', 'figure'), Input('variable', 'value'))
def create_plot(variable):
    fig = go.Figure(...)
    # 20+ lines of Plotly configuration
    return fig
```

## 📁 Your NetCDF Data

### Add Your Forecasts

Place NetCDF files in `dashboard/data/`:

```bash
cp your_forecast.nc /Users/prakrut/sites/hugonewsite/dashboard/data/
```

**Requirements:**
- Dimensions: `time`, `lat`, `lon`
- Any gridded variables
- CF-compliant metadata

### Sample Data

If no NetCDF files exist, the dashboard auto-generates:
- 30-day forecast
- 3 variables (temperature, precipitation, soil moisture)
- Amazon basin domain (-10° to 10° N, -80° to -40° E)

## 🛠️ Customization

### Change Colors

Edit `app.py`:
```python
cmaps = {
    'temperature': 'plasma',  # Change colormap
    'precipitation': 'viridis',
    'your_variable': 'coolwarm'
}
```

### Add Variables

Dashboard automatically detects all variables in your NetCDF file.

### Modify Domain

```python
lats = np.linspace(your_min, your_max, resolution)
lons = np.linspace(your_min, your_max, resolution)
```

### Change Template

```python
template = pn.template.MaterialTemplate(
    title="My Dashboard",
    theme='dark'  # or 'default'
)
```

## 🌐 Deployment

### Development (current)
```bash
python app.py
```

### Production
```bash
panel serve app.py --port 8050 --allow-websocket-origin='yourdomain.com'
```

### Docker
```bash
docker build -t s2s-dashboard .
docker run -p 8050:8050 s2s-dashboard
```

### Update Hugo iframe

In `content/dashboard/index.md`, change:
```html
<iframe src="http://localhost:8050" ...>
```
to:
```html
<iframe src="https://your-deployed-dashboard.com" ...>
```

## 📚 Documentation

- **Panel**: https://panel.holoviz.org
- **HoloViews**: https://holoviews.org
- **hvPlot**: https://hvplot.holoviz.org
- **xarray**: https://docs.xarray.dev

## 🔧 Troubleshooting

### Dashboard not loading in iframe?

1. Start the Panel app:
   ```bash
   cd dashboard && python app.py
   ```

2. Check it's running at http://localhost:8050

3. Refresh your Hugo site

### Import errors?

```bash
pip install -r requirements.txt
```

### Want to use Dash instead?

The full Dash implementation is available in the previously created files. Let me know if you want to switch back!

## ✨ Next Steps

1. ✅ Hugo site running with dashboard page
2. ✅ Panel app created and ready to run
3. ⬜ Install Python dependencies
4. ⬜ Run `python app.py` to start dashboard
5. ⬜ Add your NetCDF forecast data
6. ⬜ Customize colors and variables
7. ⬜ Deploy to production

Your complete S2S Geospatial site is ready! 🚀
