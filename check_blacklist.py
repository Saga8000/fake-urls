import json

def test_blacklist():
    with open('blacklist.json', 'r', encoding='utf-8') as f:
        blacklist = json.load(f)['fake_urls']
        print(f"Total blacklist entries: {len(blacklist)}")
        print("Sample entries:", blacklist[:5])
        print("\nSearching for 'secure-account-update.com'...")
        matches = [url for url in blacklist if 'secure-account-update.com' in url]
        print(f"Found {len(matches)} matches")
        for match in matches:
            print(f"- {match}")

if __name__ == '__main__':
    test_blacklist()
