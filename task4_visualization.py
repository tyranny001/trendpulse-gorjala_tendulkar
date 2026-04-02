import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_github_data.csv")

top10 = df.nlargest(10, "stars")

plt.figure(figsize=(12, 6))
plt.bar(top10["name"], top10["stars"])
plt.title("Top 10 GitHub Repositories by Stars")
plt.xlabel("Repository Name")
plt.ylabel("Stars")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top10_stars.png")
plt.show()

language_counts = df["language"].value_counts().head(5)

plt.figure(figsize=(8, 8))
language_counts.plot(kind="pie", autopct="%1.1f%%")
plt.title("Top 5 Programming Languages")
plt.ylabel("")
plt.tight_layout()
plt.savefig("language_distribution.png")
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df["stars"], df["forks"])
plt.title("Stars vs Forks")
plt.xlabel("Stars")
plt.ylabel("Forks")
plt.tight_layout()
plt.savefig("stars_vs_forks.png")
plt.show()

print("✅ Visualizations created successfully!")