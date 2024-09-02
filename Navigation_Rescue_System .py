import networkx as nx
import folium
import pandas as pd
import math

# Function to calculate the distance between two coordinates using the haversine formula
def calculate_distance(lat1, lon1, lat2, lon2):
    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Haversine formula
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = 6371 * c  # Earth's radius in kilometers
    return distance

# Read the port coordinates and countries from the Excel file
data = pd.read_excel('D:/my_studies_year _2/sem_2/Discrete/zip/Book2.xlsx')
port_data = {row['Port Name']: {'country': row['country'], 'latitude': row['Latitude'], 'longitude': row['Longitude']} for _, row in data.iterrows()}

# Create a graph
graph = nx.Graph()

# Add ports as nodes to the graph
for port, data in port_data.items():
    graph.add_node(port, country=data['country'], latitude=data['latitude'], longitude=data['longitude'])

# Get the latitude and longitude of the ship in distress
ship_latitude = float(input("Enter the latitude of the ship in distress: "))
ship_longitude = float(input("Enter the longitude of the ship in distress: "))

# Calculate the distances between the ship and all ports
distances = {}
for port, data in port_data.items():
    distance = calculate_distance(ship_latitude, ship_longitude, data['latitude'], data['longitude'])
    distances[port] = distance

# Find the nearest port
nearest_port = min(distances, key=distances.get)

# Example usage: Visualize the graph on a map
m = folium.Map(location=[ship_latitude, ship_longitude], zoom_start=8)

# Plot signal circles around the ship
folium.Circle(
    location=[ship_latitude, ship_longitude],
    radius=50000,  # Adjust the radius as needed
    color='green',
    fill=False,
    opacity=0.5
).add_to(m)

# Plot the ship in distress on the map
folium.Marker([ship_latitude, ship_longitude], popup="Ship in Distress", icon=folium.Icon(color='red')).add_to(m)

# Plot the ports on the map
for port, data in port_data.items():
    folium.Marker([data['latitude'], data['longitude']], popup=port).add_to(m)

# Plot a polyline between the ship and the nearest port
ship_coords = (ship_latitude, ship_longitude)
nearest_port_coords = (port_data[nearest_port]['latitude'], port_data[nearest_port]['longitude'])
folium.PolyLine([ship_coords, nearest_port_coords], color='blue', weight=2.5, opacity=1).add_to(m)

# Display the map
m.save('emergency_navigation_map.html')  # Save the map as an HTML file

# Print the nearest port
print("Nearest Port:", nearest_port)