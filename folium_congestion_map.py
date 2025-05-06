# folium_congestion_map.py
##folium.CircleMarker is used to plot circular markers on a map at specified coordinates. 
# In this project, each marker represents a traffic intersection. I used the radius parameter to set the size, 
# and the color and fill_color to visually show the congestion level — red for high, green for low.
##The popup parameter lets the user click the circle and see the name of the intersection and its congestion index. 
# It’s an effective way to make the map interactive and informative.

# Import the Folium library for creating interactive leaflet maps
import folium

# Define the traffic congestion data for 4 intersections
# Each item includes:
# - Location name
# - Latitude and longitude (for plotting)
# - Congestion index (pre-calculated)
locations = [
    {"name": "Broad St & 5th", "lat": 40.7357, "lon": -74.1724, "index": 0.444},
    {"name": "Market & Raymond", "lat": 40.7380, "lon": -74.1801, "index": 2.0},
    {"name": "Central Ave", "lat": 40.7410, "lon": -74.1865, "index": 10.0},
    {"name": "University Heights", "lat": 40.7441, "lon": -74.1900, "index": 0.25},
]

# Create a base map centered around Newark, NJ
# Zoom level 14 gives a clear view of local intersections
m = folium.Map(location=[40.74, -74.18], zoom_start=14)

# Add congestion markers to the map
for loc in locations:
    # Choose red if congestion index is high (>2), otherwise green
    color = "red" if loc["index"] > 2 else "green"

    # Create a circle marker at the location
    folium.CircleMarker(
        location=(loc["lat"], loc["lon"]),      # Coordinates of the point
        radius=10,                              # Size of the circle
        popup=f"{loc['name']} - Index: {loc['index']}",  # Tooltip on click
        color=color,                            # Border color
        fill=True,                              # Fill the circle
        fill_color=color                        # Fill color same as border
    ).add_to(m)  # Add the marker to the map

# Save the map as an interactive HTML file
m.save("congestion_map.html")

# to run - open congestion_map.html  
