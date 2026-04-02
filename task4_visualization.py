import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("data/cleaned_trends.csv")

os.makedirs("data", exist_ok=True)

category_counts = df["category"].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(category_counts.index, category_counts.values)
plt.title("Number of Stories per Category")
plt.xlabel("Category")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("data/category_counts.png")
plt.show()

avg_score = df.groupby("category")["score"].mean().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
plt.bar(avg_score.index, avg_score.values)
plt.title("Average Score by Category")
plt.xlabel("Category")
plt.ylabel("Average Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("data/average_score_by_category.png")
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df["score"], df["num_comments"])
plt.title("Score vs Number of Comments")
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.tight_layout()
plt.savefig("data/score_vs_comments.png")
plt.show()

top10 = df.nlargest(10, "score")

plt.figure(figsize=(10, 6))
plt.barh(top10["title"], top10["score"])
plt.title("Top 10 Stories by Score")
plt.xlabel("Score")
plt.ylabel("Title")
plt.tight_layout()
plt.savefig("data/top10_stories_by_score.png")
plt.show()

print("Visualizations saved in data/ folder.")