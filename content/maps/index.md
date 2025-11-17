---
title: "Research Regions"
markup: "html"
---

## Key Study Areas

Interactive map showing primary research regions for S2S hydrological forecasting and climate-health studies.

<div id="map" style="height: 600px; margin-top: 20px;"></div>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
const map = L.map('map').setView([10, 30], 2);
L.tileLayer('https://&#123;s&#125;.tile.openstreetmap.org/&#123;z&#125;/&#123;x&#125;/&#123;y&#125;.png', {
  maxZoom: 19,
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

// Custom colored markers
const greenIcon = L.divIcon({
  className: 'custom-marker',
  html: '&#60;div style="background: #10b981; width: 24px; height: 24px; border-radius: 50%; border: 3px solid white; box-shadow: 0 2px 8px rgba(0,0,0,0.3);"&#62;&#60;/div&#62;',
  iconSize: [24, 24]
});

const blueIcon = L.divIcon({
  className: 'custom-marker',
  html: '&#60;div style="background: #2563eb; width: 24px; height: 24px; border-radius: 50%; border: 3px solid white; box-shadow: 0 2px 8px rgba(0,0,0,0.3);"&#62;&#60;/div&#62;',
  iconSize: [24, 24]
});

const purpleIcon = L.divIcon({
  className: 'custom-marker',
  html: '&#60;div style="background: #764ba2; width: 24px; height: 24px; border-radius: 50%; border: 3px solid white; box-shadow: 0 2px 8px rgba(0,0,0,0.3);"&#62;&#60;/div&#62;',
  iconSize: [24, 24]
});

const orangeIcon = L.divIcon({
  className: 'custom-marker',
  html: '&#60;div style="background: #f59e0b; width: 24px; height: 24px; border-radius: 50%; border: 3px solid white; box-shadow: 0 2px 8px rgba(0,0,0,0.3);"&#62;&#60;/div&#62;',
  iconSize: [24, 24]
});

// Amazon Basin - Malaria & Fire Research
L.marker([-3.5, -65], {icon: greenIcon}).addTo(map)
  .bindPopup('&#60;div style="font-family: sans-serif;"&#62;&#60;b style="color: #10b981; font-size: 1.1rem;"&#62;🌳 Amazon Basin&#60;/b&#62;&#60;br&#62;&#60;span style="color: #6b7280;"&#62;Malaria prediction & forest fire monitoring&#60;/span&#62;&#60;/div&#62;');

// Nile River Basin - GERD
L.marker([12, 37], {icon: blueIcon}).addTo(map)
  .bindPopup('&#60;div style="font-family: sans-serif;"&#62;&#60;b style="color: #2563eb; font-size: 1.1rem;"&#62;💧 Nile River Basin&#60;/b&#62;&#60;br&#62;&#60;span style="color: #6b7280;"&#62;Grand Ethiopian Renaissance Dam studies&#60;/span&#62;&#60;/div&#62;');

// High Mountain Asia - Permafrost
L.marker([32, 85], {icon: purpleIcon}).addTo(map)
  .bindPopup('&#60;div style="font-family: sans-serif;"&#62;&#60;b style="color: #764ba2; font-size: 1.1rem;"&#62;⛰️ High Mountain Asia&#60;/b&#62;&#60;br&#62;&#60;span style="color: #6b7280;"&#62;Permafrost & ground temperature&#60;/span&#62;&#60;/div&#62;');

// Narmada Basin - India
L.marker([22.5, 76], {icon: orangeIcon}).addTo(map)
  .bindPopup('&#60;div style="font-family: sans-serif;"&#62;&#60;b style="color: #f59e0b; font-size: 1.1rem;"&#62;🌊 Narmada River Basin&#60;/b&#62;&#60;br&#62;&#60;span style="color: #6b7280;"&#62;Nitrogen transport modeling&#60;/span&#62;&#60;/div&#62;');
</script>

---

### Data Integration

Maps can integrate TiTiler for COG/STAC visualization, custom satellite data tiles, or embedded Python dashboards.
