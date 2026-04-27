import folium
import pandas as pd


avg_temp_data = pd.read_csv('data/GlobalLandTemperaturesByCountry.csv')

political_conty_layer = (
    'http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson'
)

map = folium.Map(
    location=(8.7832, 34.5085),
    zoom_control=True,
    zoom_start=3,
    tiles='cartoDB positron',
    control_scale=True,
    
)
folium.GeoJson(political_conty_layer).add_to(map)
















folium.LayerControl().add_to(map)
map.save('output/map.html')