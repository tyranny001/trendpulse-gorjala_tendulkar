import pandas as pd
import glob
import os

json_files = glob.glob("data/trends_*.json")

if not json_files:
    print("No JSON file found in data folder.")
    exit()

latest_file = max(json_files, key=os.path.getctime)

df = pd.read_json(latest_file)

print("Original shape:", df.shape)

df = df.drop_duplicates(subset=["post_id"])

df["title"] = df["title"].fillna("Unknown Title")
df["category"] = df["category"].fillna("Unknown")
df["score"] = df["score"].fillna(0)
df["num_comments"] = df["num_comments"].fillna(0)
df["author"] = df["author"].fillna("unknown")
df["collected_at"] = pd.to_datetime(df["collected_at"], errors="coerce")

df["title"] = df["title"].astype(str).str.strip()
df["author"] = df["author"].astype(str).str.strip()
df["category"] = df["category"].astype(str).str.lower().str.strip()

df["title_length"] = df["title"].apply(len)

os.makedirs("data", exist_ok=True)

output_file = "data/cleaned_trends.csv"
df.to_csv(output_file, index=False)

print("Cleaned shape:", df.shape)
print(f"Saved cleaned data to {output_file}")
print(df.head())