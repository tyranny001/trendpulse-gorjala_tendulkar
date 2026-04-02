import pandas as pd
import numpy as np

df = pd.read_csv("data/cleaned_trends.csv")

print("\n===== TRENDPULSE ANALYSIS =====\n")

print("Total stories:", len(df))
print("Unique categories:", df["category"].nunique())
print("Average score:", round(np.mean(df["score"]), 2))
print("Average comments:", round(np.mean(df["num_comments"]), 2))
print("Average title length:", round(np.mean(df["title_length"]), 2))

print("\nStories per category:")
print(df["category"].value_counts())

print("\nTop 5 highest scored stories:")
top_score = df.nlargest(5, "score")[["title", "category", "score"]]
print(top_score)

print("\nTop 5 most commented stories:")
top_comments = df.nlargest(5, "num_comments")[["title", "category", "num_comments"]]
print(top_comments)

print("\nAverage score by category:")
avg_score_category = df.groupby("category")["score"].mean().sort_values(ascending=False)
print(avg_score_category)

print("\nAverage comments by category:")
avg_comments_category = df.groupby("category")["num_comments"].mean().sort_values(ascending=False)
print(avg_comments_category)

most_common_author = df["author"].mode()[0]
print("\nMost frequent author:", most_common_author)

max_score_story = df.loc[df["score"].idxmax()]
print("\nHighest scored story:")
print(max_score_story[["title", "category", "score"]])

max_comments_story = df.loc[df["num_comments"].idxmax()]
print("\nMost commented story:")
print(max_comments_story[["title", "category", "num_comments"]])