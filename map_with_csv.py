import pandas as pd
import folium

# Load data from CSV
df = pd.read_csv("traffic_data.csv")

# Compute congestion index = vehicle_count / speed
df["congestion_index"] = df["vehicle_count"] * (1 / df["speed"])

# Classify severity based on index value
def classify(index):
    if index < 1:
        return "Low"
    elif index < 2:
        return "Moderate"
    else:
        return "High"

df["severity"] = df["congestion_index"].apply(classify)

# Initialize the map
m = folium.Map(location=[40.74, -74.18], zoom_start=14)

# Add markers with color-coded severity
for _, row in df.iterrows():
    color = {
        "Low": "green",
        "Moderate": "orange",
        "High": "red"
    }[row["severity"]]

    folium.CircleMarker(
        location=(row["lat"], row["lon"]),
        radius=10,
        popup=f"{row['name']} - {row['severity']} (Index: {row['congestion_index']:.2f})",
        color=color,
        fill=True,
        fill_color=color
    ).add_to(m)

# Save map
m.save("adv_congestion_map.html")
print("Map generated and saved as 'adv_congestion_map.html'")

# to run - open adv_congestion_map.html  