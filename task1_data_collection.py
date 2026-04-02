import requests
import pandas as pd

url = "https://api.github.com/search/repositories?q=stars:>5000&sort=stars&order=desc&per_page=50"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    repos = data["items"]

    repo_list = []

    for repo in repos:
        repo_list.append({
            "name": repo["name"],
            "full_name": repo["full_name"],
            "owner": repo["owner"]["login"],
            "html_url": repo["html_url"],
            "description": repo["description"],
            "language": repo["language"],
            "stars": repo["stargazers_count"],
            "forks": repo["forks_count"],
            "watchers": repo["watchers_count"],
            "open_issues": repo["open_issues_count"],
            "created_at": repo["created_at"],
            "updated_at": repo["updated_at"]
        })

    df = pd.DataFrame(repo_list)

    df.to_csv("raw_github_data.csv", index=False)

    print("✅ Data collection complete!")
    print("Saved as raw_github_data.csv")
    print(df.head())

else:
    print("❌ Failed to fetch data")
    print("Status Code:", response.status_code)