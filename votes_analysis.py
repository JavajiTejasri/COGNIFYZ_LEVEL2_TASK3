import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset.csv")

# Remove missing values
df = df.dropna(subset=["Aggregate rating", "Votes"])

# Select top restaurants by votes
top_votes = df.nlargest(10, "Votes")[["Restaurant Name", "Votes"]]

print("Top Restaurants by Votes:")
print(top_votes)

# Plot graph
plt.figure(figsize=(10,6))

plt.bar(top_votes["Restaurant Name"], top_votes["Votes"])

plt.title("Top Restaurants by Votes")

plt.xlabel("Restaurant Name")

plt.ylabel("Votes")

plt.xticks(rotation=45)

# Save graph
plt.tight_layout()

plt.savefig("restaurant_votes.png")

plt.show()