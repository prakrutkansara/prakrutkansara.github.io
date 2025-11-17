# S2S Forecast Dashboard (Panel)

Interactive Panel app for NetCDF visualization with reactive widgets and modern UI.

## Features

- **FastListTemplate** - Professional sidebar layout with custom branding
- **Interactive widgets** - Variable selection, time slider, location inputs  
- **HoloViews/hvPlot** - Powerful visualization with Bokeh backend
- **Reactive updates** - Automatic plot updates when controls change
- **Statistics table** - Real-time statistics with custom styling
- **Distribution plots** - Histogram showing data distribution
- **Coastline overlay** - Geographic context on spatial plots

## Quick Start

### 1. Install Dependencies

```bash
cd dashboard
pip install -r requirements.txt
```

### 2. Run the Dashboard

```bash
python app.py
```

The dashboard will start at `http://localhost:8050`

### 3. Add Your Data (Optional)

Place NetCDF files in `data/` directory. If no files are found, sample data is auto-generated.

**NetCDF Requirements:**
- CF-compliant format
- Dimensions: `time`, `lat`, `lon`
- Any gridded forecast variables

## Panel Advantages

- **🎨 Modern templates** - FastListTemplate, MaterialTemplate, etc.
- **🔄 Reactive programming** - Automatic updates with `@pn.depends`
- **📊 HoloViews integration** - Powerful plotting with hvPlot
- **🎯 Widget ecosystem** - Rich set of interactive controls
- **📱 Responsive layouts** - Adapts to screen sizes
- **🚀 Easy deployment** - Built-in server

## Customization Examples

### Change Template Theme

```python
template = pn.template.MaterialTemplate(
    title="My Dashboard",
    theme='dark'
)
```

### Add Animation

```python
play = pn.widgets.Player(
    name='Player',
    start=0,
    end=len(times)-1,
    loop_policy='loop'
)
time_slider.link(play, value='value')
```

### Add Download Button

```python
download_button = pn.widgets.FileDownload(
    callback=lambda: ds.to_netcdf(),
    filename='forecast_data.nc'
)
```

## Production Deployment

### Panel Server

```bash
panel serve app.py --port 8050 --allow-websocket-origin='*'
```

### Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["panel", "serve", "app.py", "--port", "8050", "--address", "0.0.0.0"]
```

## Documentation

- Panel: https://panel.holoviz.org
- HoloViews: https://holoviews.org  
- hvPlot: https://hvplot.holoviz.org
