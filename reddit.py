from reddit_client import search_posts
from utils import banner

def main():
    banner()

    while True:
        start = input("Continue? (Y/N): ").strip().lower()

        if start == "y":
            query = input("Search Reddit: ").strip()
            results = search_posts(query)

            if results:
                print("\nTop Results:\n")
                for i, post in enumerate(results, 1):
                    print(f"{i}. {post['title']}")
                    print(f"   🔗 {post['url']}\n")
            else:
                print("No results found.\n")

        elif start == "n":
            print("Exiting...")
            break

        else:
            print("Invalid input. Use Y or N.\n")

if __name__ == "__main__":
    main()
