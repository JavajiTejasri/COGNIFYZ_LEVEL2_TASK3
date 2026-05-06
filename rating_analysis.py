import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset.csv")

# Remove zero ratings
ratings = df['Aggregate rating']
ratings = ratings[ratings > 0]

# Show statistics
print("Average Rating:", ratings.mean())
print("Maximum Rating:", ratings.max())
print("Minimum Rating:", ratings.min())

# Plot histogram
plt.figure(figsize=(8,5))

plt.hist(ratings, bins=10)

plt.title("Rating Distribution")
plt.xlabel("Ratings")
plt.ylabel("Number of Restaurants")

plt.tight_layout()

# Save graph
plt.savefig("rating_distribution.png")

plt.show()