import requests

BASE_URL = "https://www.reddit.com/search.json"

HEADERS = {
    "User-Agent": "RedditCLI/0.1"
}

def search_posts(query, limit=5):
    params = {
        "q": query,
        "limit": limit
    }

    try:
        res = requests.get(BASE_URL, headers=HEADERS, params=params)
        data = res.json()

        posts = []
        for item in data["data"]["children"]:
            post = item["data"]
            posts.append({
                "title": post["title"],
                "url": "https://reddit.com" + post["permalink"]
            })

        return posts

    except Exception as e:
        print("Error:", e)
        return []
