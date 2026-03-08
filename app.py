from flask import Flask, render_template, request
import json
import os
from urllib.parse import urlparse, urlunparse
from typing import List, Set, Tuple
import re

app = Flask(__name__)

def get_domain(url: str) -> str:
    """Extract the main domain from a URL."""
    try:
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        netloc = urlparse(url).netloc.lower()
        # Remove port if present
        netloc = netloc.split(':')[0]
        # Remove www. prefix
        netloc = netloc[4:] if netloc.startswith('www.') else netloc
        return netloc
    except Exception as e:
        print(f"Error extracting domain from {url}: {e}")
        return ""

def normalize_url(url: str) -> str:
    """Normalize URL for consistent comparison."""
    try:
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
            
        parsed = urlparse(url)
        netloc = parsed.netloc.lower()
        netloc = netloc[4:] if netloc.startswith('www.') else netloc
        netloc = netloc.split(':')[0]  # Remove port
        path = parsed.path.rstrip('/')
        
        # For root path, return just the domain
        if not path or path == '/':
            return netloc
        return f"{netloc}{path}"
    except Exception as e:
        print(f"Error normalizing URL {url}: {e}")
        return url.lower()

def load_blacklist() -> Set[str]:
    """Load and normalize blacklisted URLs."""
    try:
        # Use absolute path for serverless environment
        current_dir = os.path.dirname(os.path.abspath(__file__))
        blacklist_path = os.path.join(current_dir, 'blacklist.json')
        
        print(f"Attempting to load blacklist from: {blacklist_path}")
        
        if not os.path.exists(blacklist_path):
            print(f"Blacklist file not found at: {blacklist_path}")
            return set()
        
        with open(blacklist_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            urls = data.get('fake_urls', [])
            # Normalize all blacklisted URLs and remove duplicates
            result = {normalize_url(url) for url in urls if url.strip()}
            print(f"Successfully loaded {len(result)} URLs from blacklist")
            return result
    except Exception as e:
        print(f"Error loading blacklist: {e}")
        import traceback
        traceback.print_exc()
        return set()

def is_blacklisted(url: str, blacklist: Set[str]) -> bool:
    """Check if a URL is in the blacklist."""
    normalized_url = normalize_url(url)
    print(f"\nChecking URL: {url}")
    print(f"Normalized: {normalized_url}")
    
    # Check for direct match
    if normalized_url in blacklist:
        print(f"Direct match found in blacklist: {normalized_url}")
        return True
    
    # Get the domain part
    domain = normalized_url.split('/')[0] if '/' in normalized_url else normalized_url
    print(f"Extracted domain: {domain}")
    
    # Check if domain is in blacklist
    if domain in blacklist:
        print(f"Domain match found in blacklist: {domain}")
        return True
    
    # Check for partial matches
    for blacklisted in blacklist:
        if not blacklisted.strip():
            continue
            
        # Check if the blacklisted item is a substring of the URL or domain
        if (blacklisted in normalized_url or 
            (domain and blacklisted in domain) or
            (blacklisted.count('.') > 0 and domain and domain in blacklisted)):
            print(f"Partial match found - Blacklisted: {blacklisted}")
            return True
            
    print("No matches found in blacklist")
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    try:
        url = request.form['url'].strip()
        if not url:
            return render_template('result.html', 
                                url="", 
                                status="error",
                                message="Please enter a URL")
        
        blacklist = load_blacklist()
        is_blocked = is_blacklisted(url, blacklist)
        
        # Debug info
        print(f"\nFinal Decision for {url}:")
        print(f"Status: {'BLOCKED' if is_blocked else 'SAFE'}")
        print(f"Blacklist size: {len(blacklist)}")
        print("-" * 50)
        
        return render_template('result.html', 
                            url=url, 
                            status="blocked" if is_blocked else "safe")
                            
    except Exception as e:
        print(f"Error in /check: {str(e)}")
        return render_template('result.html', 
                            url=url if 'url' in locals() else "", 
                            status="error",
                            message=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)