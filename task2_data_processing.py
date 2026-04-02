import pandas as pd

df = pd.read_csv("raw_github_data.csv")

print("Original shape:", df.shape)

df = df.drop_duplicates()

df["description"] = df["description"].fillna("No description")
df["language"] = df["language"].fillna("Unknown")

df["created_at"] = pd.to_datetime(df["created_at"], utc=True)
df["updated_at"] = pd.to_datetime(df["updated_at"], utc=True)

current_time = pd.Timestamp.now(tz="UTC")

df["repo_age_days"] = (current_time - df["created_at"]).dt.days

df = df.sort_values(by="stars", ascending=False)

df.to_csv("cleaned_github_data.csv", index=False)

print("✅ Data cleaning complete!")
print("Saved as cleaned_github_data.csv")
print(df.head())