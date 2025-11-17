#!/usr/bin/env python3
"""
Interactive NetCDF Forecast Visualization Dashboard using Panel
NASA GEOSS2S Precipitation Forecasts over South America
"""

import panel as pn
import holoviews as hv
from holoviews import opts
import hvplot.xarray
import geoviews as gv
import geoviews.feature as gf
import xarray as xr
import numpy as np
import pandas as pd
from pathlib import Path
import colorcet as cc

# Enable Panel extensions
pn.extension('plotly', 'tabulator', sizing_mode='stretch_width')
hv.extension('bokeh')
gv.extension('bokeh')

# Configure template with custom styling
template = pn.template.FastListTemplate(
    title="🌧️ NASA GEOSS2S Precipitation Forecasts - South America",
    sidebar_width=320,
    accent_base_color="#2563eb",
    header_background="#2563eb",
)

# Sample data generation (replace with actual NetCDF loading)
def generate_sample_data():
    """Generate sample forecast data for demonstration"""
    times = pd.date_range('2025-01-01', periods=30, freq='D')
    lats = np.linspace(-10, 10, 50)
    lons = np.linspace(-80, -40, 60)
    
    # Create sample temperature and precipitation data
    temp = 25 + 5 * np.random.randn(len(times), len(lats), len(lons))
    precip = np.abs(10 + 5 * np.random.randn(len(times), len(lats), len(lons)))
    soil_moisture = 0.3 + 0.1 * np.random.randn(len(times), len(lats), len(lons))
    
    ds = xr.Dataset({
        'temperature': (['time', 'lat', 'lon'], temp, 
                       {'units': '°C', 'long_name': '2m Air Temperature'}),
        'precipitation': (['time', 'lat', 'lon'], precip,
                         {'units': 'mm/day', 'long_name': 'Daily Precipitation'}),
        'soil_moisture': (['time', 'lat', 'lon'], soil_moisture,
                         {'units': 'm³/m³', 'long_name': 'Soil Moisture'})
    }, coords={
        'time': times,
        'lat': lats,
        'lon': lons
    })
    
    return ds

# Load NASA GEOSS2S data
data_path = Path(__file__).parent / 'data'
nc_files = list(data_path.glob('*.nc'))

if nc_files:
    # Load the actual NASA GEOSS2S data
    ds_raw = xr.open_dataset(nc_files[0])
    
    # Convert X coordinate from 0-360 to -180 to 180
    ds_raw = ds_raw.assign_coords(X=(ds_raw.X + 180) % 360 - 180)
    ds_raw = ds_raw.sortby('X')
    
    # Rename coordinates to standard names
    ds_raw = ds_raw.rename({'Y': 'lat', 'X': 'lon', 'L': 'lead_time', 'M': 'ensemble'})
    
    # Create time dimension from lead_time (in months)
    # Base time is from the 'time' coordinate
    base_time = pd.Timestamp(ds_raw.time.values)
    lead_times = ds_raw.lead_time.values
    forecast_times = [base_time + pd.DateOffset(months=int(lt)) for lt in lead_times]
    
    # Take ensemble mean
    ds_mean = ds_raw.mean(dim='ensemble')
    
    # Drop the scalar 'time' coordinate and create new time from lead_time
    ds_mean = ds_mean.drop_vars('time')
    ds = ds_mean.assign_coords(lead_time=('lead_time', forecast_times))
    ds = ds.rename({'lead_time': 'time'})
    
    data_source = f"NASA GEOSS2S: {nc_files[0].name}"
    forecast_init = base_time.strftime('%Y-%m-%d')
else:
    raise FileNotFoundError("No NetCDF files found in data/ directory")

# Extract variables and times
variables = list(ds.data_vars.keys())
times = pd.to_datetime(ds.time.values)

# Color maps for different variables
cmaps = {
    'prec': 'Blues',
    'precipitation': 'Blues',
    'temperature': 'RdYlBu_r',
    'soil_moisture': 'BrBG',
}

# Create widgets
variable_select = pn.widgets.Select(
    name='Variable',
    options=variables,
    value=variables[0],
    width=280
)

time_slider = pn.widgets.DiscreteSlider(
    name='Forecast Lead Time',
    options={t.strftime('%b %Y (Lead: %m mo)'): i for i, t in enumerate(times)},
    value=0,
    width=280
)

lat_input = pn.widgets.FloatInput(
    name='Latitude',
    value=-10.0,  # Default to Amazon region
    start=float(ds.lat.min()),
    end=float(ds.lat.max()),
    step=1.0,
    width=130
)

lon_input = pn.widgets.FloatInput(
    name='Longitude', 
    value=-60.0,  # Default to Amazon region
    start=float(ds.lon.min()),
    end=float(ds.lon.max()),
    step=1.0,
    width=130
)

# Create info panel
info_panel = pn.pane.Markdown(f"""
### Dataset Information

**Source:** NASA GEOSS2S  
**Model:** NMME Multi-Model Ensemble  
**Initialization:** {forecast_init}

**Spatial Coverage:**
- Latitude: {ds.lat.min().values:.0f}°S to {ds.lat.max().values:.0f}°N
- Longitude: {ds.lon.min().values:.0f}°E to {ds.lon.max().values:.0f}°E
- Region: **South America**

**Forecast Period:**
- Lead times: 0.5 to 8.5 months
- Valid times: {times[0].strftime('%b %Y')} to {times[-1].strftime('%b %Y')}

**Variable:** Total Precipitation (mm/day)
""", width=280, styles={'font-size': '0.9em'})

# Reactive functions
@pn.depends(variable_select.param.value, time_slider.param.value)
def create_spatial_plot(variable, time_idx):
    """Create interactive spatial plot for South America"""
    data_slice = ds[variable].isel(time=time_idx)
    
    # Get colormap - using Bokeh's Turbo256 reversed (similar to nipy_spectral)
    cmap = 'turbo_r'
    
    # Get variable metadata
    var_name = ds[variable].attrs.get('long_name', variable)
    var_units = ds[variable].attrs.get('units', '')
    
    # Get extent from data
    lon_min, lon_max = float(ds.lon.min()), float(ds.lon.max())
    lat_min, lat_max = float(ds.lat.min()), float(ds.lat.max())
    
    # Calculate color limits as scalar floats
    clim_min = 0.0
    clim_max = float(data_slice.quantile(0.95).values)
    
    # Create geoviews plot with proper extent
    import cartopy.crs as ccrs
    
    gv_plot = gv.QuadMesh(
        (ds.lon.values, ds.lat.values, data_slice.values),
        kdims=['lon', 'lat'],
        crs=ccrs.PlateCarree()
    ).opts(
        cmap=cmap,
        clim=(clim_min, clim_max),
        colorbar=True,
        colorbar_opts={'width': 15},
        frame_width=650,
        frame_height=650,
        data_aspect=1,
        xlim=(lon_min, lon_max),
        ylim=(lat_min, lat_max),
        tools=['hover', 'tap', 'wheel_zoom', 'pan', 'reset'],
        bgcolor='#f8fafc',
        fontsize={'title': 14, 'labels': 12, 'xticks': 10, 'yticks': 10},
        title=f"{var_name} - {times[time_idx].strftime('%B %Y')} (Lead: {int(ds.time.values[time_idx] - pd.Timestamp(forecast_init).value) // (30*24*3600*1e9)} months)"
    )
    
    # Add coastlines and borders with proper extent
    coastlines = gf.coastline.opts(line_color='black', line_width=1.5, projection=ccrs.PlateCarree())
    borders = gf.borders.opts(line_color='gray', line_width=0.8, alpha=0.6, projection=ccrs.PlateCarree())
    
    # Combine layers
    plot = gv_plot * coastlines * borders
    
    return plot

@pn.depends(variable_select.param.value, lat_input.param.value, lon_input.param.value)
def create_time_series(variable, lat, lon):
    """Create forecast lead time series for selected location"""
    # Find nearest grid point
    lat_idx = np.argmin(np.abs(ds.lat.values - lat))
    lon_idx = np.argmin(np.abs(ds.lon.values - lon))
    
    # Extract time series
    time_series = ds[variable].isel(lat=lat_idx, lon=lon_idx)
    
    # Get variable metadata
    var_units = ds[variable].attrs.get('units', '')
    
    plot = time_series.hvplot.line(
        x='time',
        ylabel=f"Precipitation ({var_units})",
        title=f"Forecast at Lat: {ds.lat.values[lat_idx]:.1f}°, Lon: {ds.lon.values[lon_idx]:.1f}°",
        width=750,
        height=350,
        color='#2563eb',
        line_width=3,
        grid=True,
        xlabel='Forecast Valid Time'
    ).opts(
        bgcolor='#f8fafc',
        fontsize={'title': 13, 'labels': 11}
    ) * time_series.hvplot.scatter(
        x='time',
        size=80,
        color='#2563eb',
        alpha=0.6
    )
    
    return plot

@pn.depends(variable_select.param.value, time_slider.param.value)
def create_statistics(variable, time_idx):
    """Calculate and display precipitation statistics"""
    data_slice = ds[variable].isel(time=time_idx)
    
    # Calculate statistics
    stats_data = {
        'Statistic': ['Mean', 'Minimum', 'Maximum', 'Std Dev', 'Median', '95th %ile'],
        'Value (mm/day)': [
            f"{data_slice.mean().values:.2f}",
            f"{data_slice.min().values:.2f}",
            f"{data_slice.max().values:.2f}",
            f"{data_slice.std().values:.2f}",
            f"{data_slice.median().values:.2f}",
            f"{data_slice.quantile(0.95).values:.2f}"
        ]
    }
    
    stats_df = pd.DataFrame(stats_data)
    
    table = pn.widgets.Tabulator(
        stats_df,
        width=280,
        height=230,
        disabled=True,
        show_index=False,
        stylesheets=["""
            .tabulator-row { background-color: rgba(37, 99, 235, 0.05); }
            .tabulator-row:hover { background-color: rgba(37, 99, 235, 0.1); }
        """]
    )
    
    return table

# Create histogram
@pn.depends(variable_select.param.value, time_slider.param.value)
def create_histogram(variable, time_idx):
    """Create precipitation distribution histogram"""
    data_slice = ds[variable].isel(time=time_idx)
    
    # Filter out very high outliers for better visualization
    data_filtered = data_slice.where(data_slice < data_slice.quantile(0.98))
    
    plot = data_filtered.hvplot.hist(
        bins=40,
        xlabel="Precipitation (mm/day)",
        ylabel='Frequency',
        title='Distribution',
        width=280,
        height=220,
        color='#2563eb',
        alpha=0.7
    ).opts(
        bgcolor='#f8fafc'
    )
    
    return plot

# Layout
template.sidebar.append(pn.Column(
    pn.pane.Markdown("## Controls", styles={'color': '#2563eb', 'font-weight': 'bold'}),
    variable_select,
    time_slider,
    pn.layout.Divider(),
    pn.pane.Markdown("## Point Location", styles={'color': '#10b981', 'font-weight': 'bold'}),
    pn.Row(lat_input, lon_input),
    pn.layout.Divider(),
    info_panel
))

template.main.append(pn.Column(
    pn.pane.Markdown("## 🗺️ Precipitation Forecast Map", styles={'color': '#2563eb', 'font-size': '1.4em', 'font-weight': 'bold'}),
    pn.panel(create_spatial_plot),
    pn.layout.Divider(),
    pn.Row(
        pn.Column(
            pn.pane.Markdown("## 📊 Statistics", styles={'color': '#10b981', 'font-size': '1.2em', 'font-weight': 'bold'}),
            create_statistics,
            pn.pane.Markdown("## 📈 Distribution", styles={'color': '#f59e0b', 'font-size': '1.2em', 'font-weight': 'bold'}),
            create_histogram
        ),
        pn.Column(
            pn.pane.Markdown("## 📅 Forecast Timeline", styles={'color': '#2563eb', 'font-size': '1.2em', 'font-weight': 'bold'}),
            pn.panel(create_time_series)
        )
    )
))

# Serve the app
if __name__ == '__main__':
    import os
    
    # Get port from environment or default to 8050
    port = int(os.environ.get('PORT', 8050))
    
    # Get allowed origins for websocket (for deployment)
    allowed_origins = os.environ.get('PANEL_ALLOW_WEBSOCKET_ORIGIN', 'localhost:8050').split(',')
    
    print("\n" + "="*80)
    print("🌧️  NASA GEOSS2S Precipitation Forecast Dashboard - South America")
    print("="*80)
    print(f"📊 Variable: {variables[0]} ({ds[variables[0]].attrs.get('units', '')})")
    print(f"📅 Initialization: {forecast_init}")
    print(f"📅 Forecast range: {times[0].strftime('%b %Y')} to {times[-1].strftime('%b %Y')}")
    print(f"🗺️  Domain: {ds.lat.min().values:.0f}°S to {ds.lat.max().values:.0f}°N, "
          f"{ds.lon.min().values:.0f}°E to {ds.lon.max().values:.0f}°E")
    print(f"📦 Grid size: {len(ds.lat)} x {len(ds.lon)} points")
    print(f"\n🚀 Starting server at http://0.0.0.0:{port}")
    print(f"🌐 Allowed origins: {allowed_origins}")
    print("="*80 + "\n")
    
    template.show(port=port, address='0.0.0.0', 
                  websocket_origin=allowed_origins, 
                  open=False, verbose=True)
