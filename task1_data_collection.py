import requests
import json
import os
import time
from datetime import datetime

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"
HEADERS = {"User-Agent": "TrendPulse/1.0"}

CATEGORY_KEYWORDS = {
    "technology": [
        "ai", "software", "tech", "code", "computer",
        "data", "cloud", "api", "gpu", "llm"
    ],
    "worldnews": [
        "war", "government", "country", "president",
        "election", "climate", "attack", "global"
    ],
    "sports": [
        "nfl", "nba", "fifa", "sport", "game",
        "team", "player", "league", "championship"
    ],
    "science": [
        "research", "study", "space", "physics",
        "biology", "discovery", "nasa", "genome"
    ],
    "entertainment": [
        "movie", "film", "music", "netflix", "game",
        "book", "show", "award", "streaming"
    ]
}

def fetch_json(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed for {url}: {e}")
        return None

def assign_category(title):
    if not title:
        return None

    title_lower = title.lower()

    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword.lower() in title_lower:
                return category

    return None

def main():
    print("Fetching top stories from Hacker News...")

    top_story_ids = fetch_json(TOP_STORIES_URL)

    if not top_story_ids:
        print("Could not fetch top stories.")
        return

    top_story_ids = top_story_ids[:500]

    collected_stories = []

    category_counts = {
        "technology": 0,
        "worldnews": 0,
        "sports": 0,
        "science": 0,
        "entertainment": 0
    }

    for category in CATEGORY_KEYWORDS.keys():
        print(f"\nCollecting stories for category: {category}")

        for story_id in top_story_ids:
            if category_counts[category] >= 25:
                break

            story_url = ITEM_URL.format(story_id)
            story_data = fetch_json(story_url)

            if not story_data:
                continue

            title = story_data.get("title", "")
            if not title:
                continue

            matched_category = assign_category(title)

            if matched_category == category:
                story_record = {
                    "post_id": story_data.get("id"),
                    "title": title,
                    "category": matched_category,
                    "score": story_data.get("score", 0),
                    "num_comments": story_data.get("descendants", 0),
                    "author": story_data.get("by", "unknown"),
                    "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

                collected_stories.append(story_record)
                category_counts[category] += 1

                print(f"Added [{category_counts[category]}/25] -> {title}")

        time.sleep(2)

    os.makedirs("data", exist_ok=True)

    today_str = datetime.now().strftime("%Y%m%d")
    output_file = f"data/trends_{today_str}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(collected_stories, f, indent=4, ensure_ascii=False)

    print("\n====================================")
    print(f"Collected {len(collected_stories)} stories.")
    print(f"Saved to {output_file}")
    print("Category counts:")
    for cat, count in category_counts.items():
        print(f"{cat}: {count}")
    print("====================================")

if __name__ == "__main__":
    main()