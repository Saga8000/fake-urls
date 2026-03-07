import json

# Known spam/risky URL patterns
additional_urls = [
    "free-gift-card.com",
    "claim-reward-now.com",
    "secure-account-update.com",
    "verify-account-now.com",
    "login-verification-needed.com",
    "account-suspended-alert.com",
    "payment-confirmation-required.com",
    "unusual-activity-detected.com",
    "urgent-security-alert.com",
    "your-account-has-been-compromised.com"
]

# Load existing blacklist
try:
    with open('blacklist.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    data = {"fake_urls": []}

# Add new URLs if they don't exist
existing_urls = set(data["fake_urls"])
for url in additional_urls:
    if url not in existing_urls:
        data["fake_urls"].append(url)

# Save updated blacklist
with open('blacklist.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Updated blacklist with {len(additional_urls)} new entries")
print(f"Total URLs in blacklist: {len(data['fake_urls'])}")
