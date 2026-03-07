import csv
import json
from urllib.parse import urlparse

def normalize_url(url):
    """Normalize URL for consistent comparison."""
    try:
        parsed = urlparse(url)
        # Rebuild URL with standardized components
        scheme = parsed.scheme.lower() if parsed.scheme else 'http'
        netloc = parsed.netloc.lower().lstrip('www.').split(':')[0]  # Remove www. and port
        path = parsed.path.rstrip('/')
        return f"{scheme}://{netloc}{path}"
    except:
        return url.lower()

# Load existing enhanced blacklist to avoid duplicates
try:
    with open('blacklist_enhanced.json', 'r', encoding='utf-8') as f:
        existing_urls = set(json.load(f)['fake_urls'])
    print(f"Loaded {len(existing_urls)} existing URLs from enhanced blacklist")
except FileNotFoundError:
    existing_urls = set()

fake_urls = list(existing_urls)  # Start with existing URLs

with open('dataset/phishing_dataset.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        label = row['label'].strip().lower()
        url = normalize_url(row['url'].strip())

        # Covers: 1, 1.0, phishing, malicious
        if label in ['1', '1.0', 'phishing', 'malicious'] and url not in existing_urls:
            fake_urls.append(url)
            existing_urls.add(url)

# Save the combined and deduplicated list
with open('blacklist.json', 'w', encoding='utf-8') as out:
    json.dump({"fake_urls": sorted(fake_urls)}, out, indent=2)

print("Blacklist created successfully")
print("Total fake URLs:", len(fake_urls))
