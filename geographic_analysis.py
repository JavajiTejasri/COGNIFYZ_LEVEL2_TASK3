import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset.csv")

# Remove missing values
df = df.dropna(subset=["Latitude", "Longitude"])

# Display first few locations
print("Restaurant Locations:")
print(df[["Restaurant Name", "Latitude", "Longitude"]].head())

# Create scatter plot
plt.figure(figsize=(8,6))

plt.scatter(df["Longitude"], df["Latitude"])

# Graph title and labels
plt.title("Restaurant Geographic Distribution")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

# Save graph
plt.savefig("restaurant_locations.png")

# Show graph
plt.show()