import pandas as pd

df = pd.read_csv("cleaned_github_data.csv")

print("\n===== TRENDPULSE ANALYSIS =====\n")

print("📌 Total repositories collected:", len(df))

print("⭐ Average stars:", round(df["stars"].mean(), 2))

print("🍴 Average forks:", round(df["forks"].mean(), 2))

print("👀 Average watchers:", round(df["watchers"].mean(), 2))

print("\n🔥 Top 5 repositories by stars:")
print(df[["full_name", "stars"]].head(5))

print("\n💻 Top programming languages:")
print(df["language"].value_counts().head(10))

max_issues_repo = df.loc[df["open_issues"].idxmax()]
print("\n⚠ Repository with highest open issues:")
print(max_issues_repo[["full_name", "open_issues"]])

oldest_repo = df.loc[df["repo_age_days"].idxmax()]
print("\n🕒 Oldest repository:")
print(oldest_repo[["full_name", "repo_age_days"]])