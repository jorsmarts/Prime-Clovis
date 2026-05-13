import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

base_url = "https://appliancerepairclovis.com"
visited = set()
all_urls = set()
to_visit = [base_url]

def is_same_domain(url):
    return urlparse(url).netloc in ["appliancerepairclovis.com", "www.appliancerepairclovis.com", ""]

headers = {"User-Agent": "Mozilla/5.0 (compatible; SiteCrawler/1.0)"}

while to_visit:
    url = to_visit.pop(0)
    if url in visited:
        continue
    visited.add(url)
    
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        if "text/html" not in resp.headers.get("Content-Type", ""):
            continue
        all_urls.add(url)
        soup = BeautifulSoup(resp.text, "html.parser")
        
        for tag in soup.find_all("a", href=True):
            href = tag["href"]
            full_url = urljoin(url, href)
            parsed = urlparse(full_url)
            # Clean URL (remove fragments and query strings for dedup)
            clean = parsed.scheme + "://" + parsed.netloc + parsed.path
            if is_same_domain(full_url) and clean not in visited and clean not in to_visit:
                if not any(ext in parsed.path for ext in ['.jpg','.jpeg','.png','.gif','.pdf','.css','.js','.xml','.ico','.svg','.webp','.mp4','.zip']):
                    to_visit.append(clean)
        
        print(f"✅ {url}")
        time.sleep(0.3)
    except Exception as e:
        print(f"❌ {url} — {e}")

print("\n\n========== ALL URLS ==========")
for u in sorted(all_urls):
    print(u)
print(f"\nTotal: {len(all_urls)} pages found")
