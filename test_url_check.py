from app import is_suspicious, load_blacklist

# Load the blacklist
blacklist = load_blacklist()

# Test the URL
test_url = "http://secure-account-update.com/login"
result = is_suspicious(test_url, blacklist)

print(f"URL: {test_url}")
print(f"Is suspicious: {result}")

# Print some debug info
print("\nDebug Info:")
print(f"Blacklist entries: {len(blacklist)}")
print(f"First few entries: {list(blacklist)[:3]}")
print(f"Is domain in blacklist: {'secure-account-update.com' in blacklist}")
