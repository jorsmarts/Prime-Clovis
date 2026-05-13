from playwright.sync_api import sync_playwright
import os

pages = [
    ("https://appliancerepairclovis.com/", "homepage"),
    ("https://appliancerepairclovis.com/services/", "services"),
    ("https://appliancerepairclovis.com/about-us/", "about"),
    ("https://appliancerepairclovis.com/contact-us/", "contact"),
    ("https://appliancerepairclovis.com/refrigerator-repair-clovis-ca/", "refrigerator"),
    ("https://appliancerepairclovis.com/washer-repair-clovis-ca/", "washer"),
    ("https://appliancerepairclovis.com/blog-2/", "blog"),
    ("https://appliancerepairclovis.com/your-fridge-is-lying-to-you/", "blog-post"),
    ("https://appliancerepairclovis.com/fresno-appliance-repair/", "fresno"),
    ("https://appliancerepairclovis.com/book-an-appointment/", "book"),
]

os.makedirs("/home/user/webapp/screenshots", exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    for url, name in pages:
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto(url, wait_until="networkidle", timeout=30000)
        page.screenshot(path=f"/home/user/webapp/screenshots/{name}.png", full_page=True)
        print(f"✅ {name}: {url}")
    browser.close()

print("Done!")
