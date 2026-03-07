import json

# Simple test URL that should always be blocked
test_url = "secure-account-update.com"

# Load existing blacklist
try:
    with open('blacklist.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    data = {"fake_urls": []}

# Add test URL if it doesn't exist
if test_url not in data["fake_urls"]:
    data["fake_urls"].append(test_url)
    print(f"Added test URL: {test_url}")
else:
    print("Test URL already in blacklist")

# Save updated blacklist
with open('blacklist.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Total URLs in blacklist: {len(data['fake_urls'])}")
