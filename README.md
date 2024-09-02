# Emergency Navigation Rescue System

This project is a Python-based rescue system designed to assist ships in distress by identifying the nearest port based on their current coordinates. The system leverages geospatial data and the haversine formula to calculate the shortest distance between the ship and various ports.

## Features:
- **Geospatial Calculations**: Uses the haversine formula to calculate the distance between the ship's coordinates and port locations.
- **Graph Representation**: Ports are represented as nodes in a graph, allowing for efficient distance calculations and nearest port identification.
- **Interactive Map Visualization**:
  - Displays the ship's location and surrounding ports on a map using Folium.
  - Visualizes the nearest port and the path from the ship to the port.
- **Excel Integration**: Reads port data (including coordinates and country) from an Excel file, making it easy to update and manage the list of ports.

## How It Works:
1. **Input**: The user provides the latitude and longitude of the ship in distress.
2. **Distance Calculation**: The system calculates the distance from the ship to each port.
3. **Nearest Port Identification**: The port with the shortest distance is identified as the nearest port.
4. **Map Visualization**: An interactive map is generated, showing the ship's location, nearby ports, and the route to the nearest port.
5. **Output**: The nearest port is printed, and the map is saved as an HTML file (`emergency_navigation_map.html`).

## How to Use:
1. **Prepare Data**:
   - Ensure you have an Excel file (`Book2.xlsx`) containing the port data with columns for `Port Name`, `country`, `Latitude`, and `Longitude`.
   - Update the file path in the code if necessary.

2. **Run the Code**:
   - Execute the script.
   - Enter the latitude and longitude of the ship in distress when prompted.

3. **Output**:
   - The nearest port's name will be printed in the console.
   - An HTML map file (`emergency_navigation_map.html`) will be generated, displaying the ship's location, nearby ports, and the route to the nearest port.

## Example Usage:
```python
Enter the latitude of the ship in distress: 37.7412
Enter the longitude of the ship in distress: -25.6756
Nearest Port: Ponta Delgada
