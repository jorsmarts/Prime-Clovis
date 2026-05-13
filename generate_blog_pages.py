#!/usr/bin/env python3
"""Generate 6 blog post pages + 3 category pages for Prime Appliance Repair static site."""

import os

BASE = "/home/user/webapp/static-site"

FAVICON = "https://appliancerepairclovis.com/wp-content/uploads/2022/10/appliance-repair.png"

HEADER = """<header>
  <div class="header-inner">
    <a href="/" class="logo"><span>Prime Appliance Repair</span></a>
    <nav>
      <a href="/">Home</a>
      <a href="/services/">Services</a>
      <a href="/about-us/">About Us</a>
      <a href="/blog-2/">Blog</a>
      <a href="/contact-us/" class="btn-outline">Contact</a>
      <a href="/book-an-appointment/" class="btn-primary">Book Online</a>
    </nav>
    <button class="hamburger" id="hamburger" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
  </div>
  <nav class="mobile-menu" id="mobile-menu">
    <a href="/">Home</a>
    <a href="/services/">Services</a>
    <a href="/about-us/">About Us</a>
    <a href="/blog-2/">Blog</a>
    <a href="/contact-us/">Contact</a>
    <a href="/book-an-appointment/">Book Online</a>
  </nav>
</header>"""

FOOTER = """<footer>
  <div class="footer-inner">
    <div class="footer-col">
      <div class="footer-logo">Prime Appliance Repair</div>
      <p>Professional appliance repair services in Clovis, Fresno, Madera, Sanger and surrounding areas. Fast, reliable, and affordable.</p>
    </div>
    <div class="footer-col">
      <h4>Services</h4>
      <ul>
        <li><a href="/refrigerator-repair-clovis-ca/">Refrigerator Repair</a></li>
        <li><a href="/washer-repair-clovis-ca/">Washer Repair</a></li>
        <li><a href="/dryer-repair-clovis-ca/">Dryer Repair</a></li>
        <li><a href="/dishwasher-repair-clovis-ca/">Dishwasher Repair</a></li>
        <li><a href="/oven-repair-clovis-ca/">Oven Repair</a></li>
        <li><a href="/stove-repair-clovis-ca/">Stove Repair</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Quick Links</h4>
      <ul>
        <li><a href="/about-us/">About Us</a></li>
        <li><a href="/blog-2/">Blog</a></li>
        <li><a href="/contact-us/">Contact Us</a></li>
        <li><a href="/book-an-appointment/">Book Appointment</a></li>
        <li><a href="/privacy-policy/">Privacy Policy</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Contact Us</h4>
      <ul>
        <li>📞 <a href="tel:5596003037">(559) 600-3037</a></li>
        <li>📍 Clovis, CA 93612</li>
        <li>⏰ Mon–Sat: 8am–6pm</li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <p>&copy; 2026 Prime Appliance Repair. All rights reserved.</p>
  </div>
</footer>
<script src="/js/main.js"></script>"""

CTA_BANNER = """<section class="cta-banner">
  <div class="container">
    <h2>Need Fast Appliance Repair?</h2>
    <p>Same-day and next-day appointments available in Clovis, Fresno, and surrounding areas.</p>
    <div style="display:flex;gap:16px;flex-wrap:wrap;justify-content:center;">
      <a href="/book-an-appointment/" class="btn-primary">Book Online Now</a>
      <a href="tel:5596003037" class="btn-secondary">Call (559) 600-3037</a>
    </div>
  </div>
</section>"""

def blog_page(slug, title, meta_desc, category, category_slug, date, read_time, hero_img, content_html):
    """Generate a full blog post page."""
    canonical = f"https://appliancerepairclovis.com/{slug}/"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Prime Appliance Repair Clovis</title>
<meta name="description" content="{meta_desc}">
<link rel="canonical" href="{canonical}">
<link rel="stylesheet" href="/css/style.css">
<link rel="icon" href="{FAVICON}">
<style>
.blog-post-hero {{
  background: var(--dark);
  padding: 60px 0 0;
  color: #fff;
}}
.blog-post-hero .container {{
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 20px;
}}
.blog-post-hero .breadcrumb {{
  font-size: 13px;
  color: rgba(255,255,255,0.6);
  margin-bottom: 18px;
}}
.blog-post-hero .breadcrumb a {{
  color: var(--accent);
  text-decoration: none;
}}
.blog-post-hero .blog-cat-pill {{
  display: inline-block;
  background: var(--accent);
  color: var(--dark);
  font-size: 12px;
  font-weight: 700;
  padding: 4px 14px;
  border-radius: 20px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 18px;
}}
.blog-post-hero h1 {{
  color: #fff;
  font-size: 42px;
  max-width: 760px;
  line-height: 1.2;
  margin-bottom: 16px;
}}
.blog-post-hero .meta {{
  font-size: 14px;
  color: rgba(255,255,255,0.6);
  margin-bottom: 40px;
}}
.hero-img-full {{
  width: 100%;
  max-height: 420px;
  object-fit: cover;
  display: block;
  margin-top: 40px;
  border-radius: 8px 8px 0 0;
}}
.blog-post-layout {{
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 60px 20px;
  display: grid;
  grid-template-columns: 1fr 320px;
  gap: 50px;
}}
.blog-post-content h2 {{
  font-size: 26px;
  color: var(--dark);
  margin: 36px 0 14px;
}}
.blog-post-content h3 {{
  font-size: 20px;
  color: var(--primary);
  margin: 28px 0 10px;
}}
.blog-post-content p {{
  margin-bottom: 18px;
  line-height: 1.8;
  color: var(--body-text);
}}
.blog-post-content ul, .blog-post-content ol {{
  margin: 0 0 18px 24px;
  line-height: 1.8;
  color: var(--body-text);
}}
.blog-post-content li {{
  margin-bottom: 6px;
}}
.blog-post-content .highlight-box {{
  background: #f0edfc;
  border-left: 4px solid var(--primary);
  padding: 20px 24px;
  border-radius: 0 8px 8px 0;
  margin: 24px 0;
}}
.blog-post-content .highlight-box p {{
  margin: 0;
  color: var(--dark);
  font-weight: 500;
}}
.blog-post-content .cost-table {{
  width: 100%;
  border-collapse: collapse;
  margin: 24px 0;
  font-size: 15px;
}}
.blog-post-content .cost-table th {{
  background: var(--primary);
  color: #fff;
  padding: 12px 16px;
  text-align: left;
  font-family: 'Poppins', sans-serif;
}}
.blog-post-content .cost-table td {{
  padding: 11px 16px;
  border-bottom: 1px solid #e0e0e0;
}}
.blog-post-content .cost-table tr:nth-child(even) td {{
  background: #f9f9f9;
}}
.blog-sidebar {{
  position: sticky;
  top: 80px;
  align-self: start;
}}
.sidebar-widget {{
  background: #f9f9f9;
  border-radius: 10px;
  padding: 24px;
  margin-bottom: 28px;
}}
.sidebar-widget h4 {{
  font-size: 16px;
  color: var(--dark);
  margin-bottom: 16px;
  padding-bottom: 10px;
  border-bottom: 2px solid var(--primary);
}}
.sidebar-widget ul {{
  list-style: none;
  padding: 0;
  margin: 0;
}}
.sidebar-widget ul li {{
  margin-bottom: 10px;
}}
.sidebar-widget ul li a {{
  color: var(--body-text);
  text-decoration: none;
  font-size: 14px;
  display: flex;
  align-items: center;
  gap: 8px;
}}
.sidebar-widget ul li a:hover {{
  color: var(--primary);
}}
.sidebar-cta {{
  background: var(--primary);
  color: #fff;
  border-radius: 10px;
  padding: 28px 24px;
  text-align: center;
}}
.sidebar-cta h4 {{
  color: #fff;
  font-size: 18px;
  margin-bottom: 12px;
}}
.sidebar-cta p {{
  font-size: 14px;
  color: rgba(255,255,255,0.85);
  margin-bottom: 20px;
}}
.sidebar-cta .btn-accent {{
  display: block;
  background: var(--accent);
  color: var(--dark);
  font-weight: 700;
  padding: 13px;
  border-radius: 6px;
  text-decoration: none;
  margin-bottom: 10px;
  font-family: 'Poppins', sans-serif;
}}
.sidebar-cta .btn-white {{
  display: block;
  background: rgba(255,255,255,0.15);
  color: #fff;
  font-weight: 600;
  padding: 11px;
  border-radius: 6px;
  text-decoration: none;
  font-size: 14px;
}}
.related-posts {{
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 20px 70px;
}}
.related-posts h2 {{
  font-size: 26px;
  color: var(--dark);
  margin-bottom: 30px;
  border-bottom: 3px solid var(--accent);
  padding-bottom: 14px;
}}
.related-grid {{
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 24px;
}}
@media(max-width:900px){{
  .blog-post-layout {{ grid-template-columns: 1fr; }}
  .blog-sidebar {{ position: static; }}
  .related-grid {{ grid-template-columns: 1fr 1fr; }}
  .blog-post-hero h1 {{ font-size: 30px; }}
}}
@media(max-width:600px){{
  .related-grid {{ grid-template-columns: 1fr; }}
}}
</style>
</head>
<body>
{HEADER}
<div class="blog-post-hero">
  <div class="container">
    <p class="breadcrumb"><a href="/">Home</a> &rsaquo; <a href="/blog-2/">Blog</a> &rsaquo; {title}</p>
    <span class="blog-cat-pill">{category}</span>
    <h1>{title}</h1>
    <p class="meta">By Prime Appliance Repair &nbsp;|&nbsp; {date} &nbsp;|&nbsp; {read_time} read</p>
  </div>
  <img src="{hero_img}" alt="{title}" class="hero-img-full">
</div>

<div class="blog-post-layout">
  <article class="blog-post-content">
{content_html}
  </article>

  <aside class="blog-sidebar">
    <div class="sidebar-cta">
      <h4>Appliance Acting Up?</h4>
      <p>We diagnose and fix all major brands. Same-day service available in Clovis &amp; Fresno.</p>
      <a href="/book-an-appointment/" class="btn-accent">Book Appointment</a>
      <a href="tel:5596003037" class="btn-white">📞 (559) 600-3037</a>
    </div>

    <div class="sidebar-widget">
      <h4>Our Services</h4>
      <ul>
        <li><a href="/refrigerator-repair-clovis-ca/">🧊 Refrigerator Repair</a></li>
        <li><a href="/washer-repair-clovis-ca/">🫧 Washer Repair</a></li>
        <li><a href="/dryer-repair-clovis-ca/">💨 Dryer Repair</a></li>
        <li><a href="/dishwasher-repair-clovis-ca/">🍽️ Dishwasher Repair</a></li>
        <li><a href="/oven-repair-clovis-ca/">🔥 Oven Repair</a></li>
        <li><a href="/stove-repair-clovis-ca/">🍳 Stove Repair</a></li>
        <li><a href="/microwave-repair-clovis-ca/">📡 Microwave Repair</a></li>
        <li><a href="/freezer-repair-clovis-ca/">❄️ Freezer Repair</a></li>
      </ul>
    </div>

    <div class="sidebar-widget">
      <h4>Recent Posts</h4>
      <ul>
        <li><a href="/your-fridge-is-lying-to-you/">Your Fridge Is Lying to You</a></li>
        <li><a href="/appliance-repair-cost-guide/">Appliance Repair Cost Guide</a></li>
        <li><a href="/repair-vs-replace/">Repair vs. Replace: How to Decide</a></li>
        <li><a href="/washer-maintenance-tips-most-people-ignore/">Washer Maintenance Tips</a></li>
        <li><a href="/why-your-dryer-takes-too-long-to-dry-clothes/">Why Your Dryer Takes Too Long</a></li>
        <li><a href="/when-everything-still-works-but-somethings-clearly-wrong/">When Something's Clearly Wrong</a></li>
      </ul>
    </div>

    <div class="sidebar-widget">
      <h4>Categories</h4>
      <ul>
        <li><a href="/category/appliance-problems-fixes/">🔧 Appliance Problems &amp; Fixes</a></li>
        <li><a href="/category/repair-cost-guides/">💰 Repair Cost Guides</a></li>
        <li><a href="/category/maintenance-insider-tips/">✅ Maintenance &amp; Insider Tips</a></li>
      </ul>
    </div>
  </aside>
</div>

{CTA_BANNER}

<div class="related-posts">
  <h2>More Articles</h2>
  <div class="related-grid">
    <a href="/appliance-repair-cost-guide/" class="blog-list-card">
      <img src="https://appliancerepairclovis.com/wp-content/uploads/2026/04/vecteezy_technician-or-worker-in-uniform-installs-dishwasher-into-the_35202703-1.jpg" alt="Appliance Repair Cost Guide" loading="lazy">
      <div class="blog-list-card-body">
        <span class="blog-cat">Repair Cost Guides</span>
        <h3>Appliance Repair Cost Guide</h3>
        <span class="read-more">Read More →</span>
      </div>
    </a>
    <a href="/repair-vs-replace/" class="blog-list-card">
      <img src="https://appliancerepairclovis.com/wp-content/uploads/2026/04/vecteezy_senior-technician-fixing-dishwasher-at-kitchen_42863819.jpg" alt="Repair vs Replace" loading="lazy">
      <div class="blog-list-card-body">
        <span class="blog-cat">Appliance Problems &amp; Fixes</span>
        <h3>Repair vs. Replace: How to Decide</h3>
        <span class="read-more">Read More →</span>
      </div>
    </a>
    <a href="/washer-maintenance-tips-most-people-ignore/" class="blog-list-card">
      <img src="https://appliancerepairclovis.com/wp-content/uploads/2026/04/vecteezy_the-plumber-tries-to-repair-a-broken-washing-machine_58009083.jpg" alt="Washer Maintenance Tips" loading="lazy">
      <div class="blog-list-card-body">
        <span class="blog-cat">Maintenance &amp; Tips</span>
        <h3>Washer Maintenance Tips Most People Ignore</h3>
        <span class="read-more">Read More →</span>
      </div>
    </a>
  </div>
</div>

{FOOTER}
</body>
</html>"""


def category_page(slug, title, meta_desc, posts_html):
    """Generate a blog category archive page."""
    canonical = f"https://appliancerepairclovis.com/category/{slug}/"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Prime Appliance Repair Blog</title>
<meta name="description" content="{meta_desc}">
<link rel="canonical" href="{canonical}">
<link rel="stylesheet" href="/css/style.css">
<link rel="icon" href="{FAVICON}">
</head>
<body>
{HEADER}
<section class="page-hero">
  <div class="container">
    <p style="font-size:13px;color:rgba(255,255,255,0.6);margin-bottom:10px;"><a href="/" style="color:var(--accent);text-decoration:none;">Home</a> &rsaquo; <a href="/blog-2/" style="color:var(--accent);text-decoration:none;">Blog</a> &rsaquo; {title}</p>
    <h1>{title}</h1>
    <p>{meta_desc}</p>
  </div>
</section>

<section style="padding:70px 0;">
  <div style="max-width:1120px;margin:0 auto;padding:0 20px;">
    <div style="display:flex;gap:16px;flex-wrap:wrap;margin-bottom:36px;">
      <a href="/blog-2/" style="display:inline-block;padding:8px 20px;background:#f5f5f5;color:#404040;border-radius:20px;font-size:14px;">All Posts</a>
      <a href="/category/appliance-problems-fixes/" style="display:inline-block;padding:8px 20px;background:#f5f5f5;color:#404040;border-radius:20px;font-size:14px;">Appliance Problems &amp; Fixes</a>
      <a href="/category/repair-cost-guides/" style="display:inline-block;padding:8px 20px;background:#f5f5f5;color:#404040;border-radius:20px;font-size:14px;">Repair Cost Guides</a>
      <a href="/category/maintenance-insider-tips/" style="display:inline-block;padding:8px 20px;background:#f5f5f5;color:#404040;border-radius:20px;font-size:14px;">Maintenance &amp; Tips</a>
    </div>
    <div class="blog-page-grid">
{posts_html}
    </div>
  </div>
</section>

{CTA_BANNER}
{FOOTER}
</body>
</html>"""


# ─────────────────────────────────────────────
# BLOG POST CONTENT
# ─────────────────────────────────────────────

posts = [
  {
    "slug": "your-fridge-is-lying-to-you",
    "title": "Your Fridge Is Lying to You",
    "meta": "Is your refrigerator quietly failing while appearing fine? Learn the hidden signs your fridge is losing efficiency — before food spoils or your energy bill spikes.",
    "category": "Appliance Problems & Fixes",
    "category_slug": "appliance-problems-fixes",
    "date": "April 18, 2026",
    "read_time": "4 min",
    "img": "https://appliancerepairclovis.com/wp-content/uploads/2026/04/vecteezy_woman-looking-disappointed-at-an-empty-fridge-feeling_69408907.jpg",
    "content": """    <p>It looks fine. The light turns on. It hums. It's cold… kind of. So you don't think about it much — until you pull out a carton of milk that went bad two days early, or you notice your electricity bill crept up $30 last month for no clear reason.</p>

    <p>Your refrigerator is one of the few appliances that runs 24 hours a day, 7 days a week. And because it never stops, it's also one of the first appliances where slow, subtle decline gets ignored the longest.</p>

    <div class="highlight-box"><p>"A fridge that's 'kind of cold' isn't doing its job — and it's costing you more money every single day it runs inefficiently."</p></div>

    <h2>The 7 Quiet Signs Your Fridge Is Failing</h2>

    <h3>1. The Motor Runs Almost Constantly</h3>
    <p>Your fridge's compressor cycles on and off throughout the day — that's normal. But if you notice the motor seems to run <em>almost all the time</em>, or it never seems to stop, that's a red flag. It usually means the fridge is struggling to hold temperature — often because of a dirty condenser coil, failing door seals, or a compressor that's on its way out.</p>

    <h3>2. Your Food Is Spoiling Faster Than It Should</h3>
    <p>If milk goes bad before the sell-by date, lettuce wilts in two days, or leftovers don't last as long as you expect — your fridge may not be holding the right temperature. The USDA recommends 35°F–38°F for the refrigerator compartment. Anything above 40°F and bacteria growth accelerates rapidly.</p>
    <p><strong>Quick test:</strong> Place a thermometer in the center of your fridge for 24 hours. If it reads above 40°F, something is wrong.</p>

    <h3>3. Excessive Condensation or Frost Buildup</h3>
    <p>A little condensation on the outside of a cold glass is normal. But if you're seeing water droplets forming on the inside walls of your fridge, or unexpected frost in the freezer section, your door gaskets may be failing — allowing warm, humid air to sneak in.</p>

    <h3>4. The Back Wall of the Fridge Feels Hot</h3>
    <p>The exterior sides of your fridge can feel slightly warm — that's by design, as refrigerators dispel heat through the walls. But if the back or sides feel noticeably hot to the touch, the condenser coils may be dirty and overworking the compressor.</p>

    <h3>5. Water Pooling Inside or Under the Unit</h3>
    <p>A small amount of water in the drain pan underneath is expected. But standing water inside the fridge, or puddles on your kitchen floor, typically means the defrost drain is clogged or the water supply line (on models with ice makers/water dispensers) is leaking.</p>

    <h3>6. Strange Noises You Haven't Heard Before</h3>
    <p>Every fridge has its own "normal" sounds. But if you're suddenly hearing:</p>
    <ul>
      <li><strong>Loud clicking</strong> — often a failing start relay on the compressor</li>
      <li><strong>Buzzing or rattling</strong> — loose drain pan, failing fan motor, or ice buildup on evaporator coils</li>
      <li><strong>High-pitched squealing</strong> — evaporator or condenser fan motor going bad</li>
      <li><strong>Knocking or banging</strong> — compressor issue; this is serious</li>
    </ul>
    <p>Don't dismiss new sounds. They're your fridge's way of waving a flag.</p>

    <h3>7. It's More Than 10 Years Old</h3>
    <p>Modern refrigerators are rated for 10–18 years of life. But efficiency drops significantly after year 10 — especially if maintenance has been minimal. An older unit working harder means higher energy bills even when everything "seems fine."</p>

    <h2>What Should You Do?</h2>
    <p>Start with these free checks you can do yourself:</p>
    <ul>
      <li>✅ Vacuum the condenser coils (usually behind or beneath the unit) — dust buildup is the #1 cause of overworking compressors</li>
      <li>✅ Inspect door gaskets for cracks or gaps — run a dollar bill through the seal; if it slides out easily, the seal is weak</li>
      <li>✅ Check freezer for excess frost buildup around the back panel (often means defrost heater failure)</li>
      <li>✅ Set temperature controls correctly: 37°F fridge, 0°F freezer</li>
    </ul>

    <p>If the problem persists after these basic checks, it's time to call a technician. Most refrigerator repairs — including thermostat replacement, door gasket seals, compressor start relays, and defrost system fixes — cost significantly less than buying a new unit.</p>

    <div class="highlight-box"><p><strong>Rule of thumb:</strong> If a repair costs less than 50% of a replacement unit's price and your fridge is under 10 years old, repair almost always wins financially.</p></div>

    <h2>We Repair All Major Refrigerator Brands</h2>
    <p>At Prime Appliance Repair, we diagnose and fix refrigerators from LG, Samsung, Whirlpool, GE, Bosch, Sub-Zero, Maytag, KitchenAid, and more — typically same day or next day in Clovis, Fresno, and the surrounding Central Valley.</p>
    <p>Don't let your fridge lie to you. <a href="/book-an-appointment/" style="color:var(--primary);font-weight:600;">Book a diagnostic visit today</a> — most repairs are completed in a single visit.</p>"""
  },

  {
    "slug": "appliance-repair-cost-guide",
    "title": "Appliance Repair Cost Guide: What to Expect and How to Decide",
    "meta": "Wondering how much appliance repair costs in 2026? This honest guide breaks down typical repair costs for refrigerators, washers, dryers, ovens, and more.",
    "category": "Repair Cost Guides",
    "category_slug": "repair-cost-guides",
    "date": "April 16, 2026",
    "read_time": "5 min",
    "img": "https://appliancerepairclovis.com/wp-content/uploads/2026/04/vecteezy_technician-or-worker-in-uniform-installs-dishwasher-into-the_35202703-1.jpg",
    "content": """    <p>One of the first questions people ask when an appliance breaks is: <em>"How much does appliance repair cost?"</em> The honest answer is: it depends — but there are useful ranges you can plan around, and a simple framework to help you decide whether repairing or replacing makes financial sense.</p>

    <p>This guide covers typical repair costs for the most common home appliances in 2026, what drives those costs, and how to avoid overpaying.</p>

    <h2>What Goes Into an Appliance Repair Bill?</h2>
    <p>Most repair invoices break down into two components:</p>
    <ol>
      <li><strong>Labor / Service Call Fee</strong> — The technician's time to diagnose the problem and perform the repair. In the Central Valley (Clovis, Fresno area), this typically runs $80–$120 for the diagnostic visit, often credited toward the repair.</li>
      <li><strong>Parts Cost</strong> — The price of any replacement component: control board, motor, pump, thermostat, door gasket, etc. Parts vary wildly depending on brand, appliance age, and part availability.</li>
    </ol>

    <h2>2026 Appliance Repair Cost Breakdown</h2>
    <table class="cost-table">
      <tr><th>Appliance</th><th>Common Issue</th><th>Typical Repair Cost</th></tr>
      <tr><td><strong>Refrigerator</strong></td><td>Not cooling / warm fridge</td><td>$150–$400</td></tr>
      <tr><td></td><td>Ice maker not working</td><td>$100–$250</td></tr>
      <tr><td></td><td>Water dispenser issues</td><td>$80–$200</td></tr>
      <tr><td></td><td>Compressor replacement</td><td>$350–$650+</td></tr>
      <tr><td><strong>Washing Machine</strong></td><td>Not draining</td><td>$100–$200</td></tr>
      <tr><td></td><td>Not spinning</td><td>$120–$280</td></tr>
      <tr><td></td><td>Leaking water</td><td>$80–$230</td></tr>
      <tr><td></td><td>Control board failure</td><td>$200–$400</td></tr>
      <tr><td><strong>Dryer</strong></td><td>Not heating</td><td>$80–$220</td></tr>
      <tr><td></td><td>Takes too long to dry</td><td>$80–$180</td></tr>
      <tr><td></td><td>Won't turn on</td><td>$100–$250</td></tr>
      <tr><td><strong>Dishwasher</strong></td><td>Not draining</td><td>$90–$200</td></tr>
      <tr><td></td><td>Not cleaning dishes</td><td>$80–$200</td></tr>
      <tr><td></td><td>Door latch failure</td><td>$80–$160</td></tr>
      <tr><td><strong>Oven / Range</strong></td><td>Not heating (electric)</td><td>$100–$250</td></tr>
      <tr><td></td><td>Burner not working</td><td>$80–$200</td></tr>
      <tr><td></td><td>Igniter replacement (gas)</td><td>$80–$180</td></tr>
      <tr><td></td><td>Control board</td><td>$200–$450</td></tr>
    </table>

    <p style="font-size:13px;color:#848484;"><em>Note: Costs shown are estimates for parts + labor in the Clovis/Fresno area. Prices vary by brand, model, and parts availability.</em></p>

    <h2>The Repair vs. Replace Rule of Thumb</h2>
    <div class="highlight-box"><p><strong>The 50% Rule:</strong> If a repair costs more than 50% of the cost of a new comparable appliance, and the unit is more than halfway through its expected lifespan, replacement is usually the better financial decision.</p></div>

    <p>Here are typical appliance lifespans to help you do the math:</p>
    <ul>
      <li>🧊 Refrigerator: 13–17 years</li>
      <li>🫧 Washing machine: 10–14 years</li>
      <li>💨 Dryer: 12–18 years</li>
      <li>🍽️ Dishwasher: 9–12 years</li>
      <li>🔥 Oven/Range: 13–20 years (gas ranges tend to last longer)</li>
    </ul>

    <h3>Example Calculation</h3>
    <p>Your 6-year-old washing machine needs a new control board: estimated repair cost $320. A comparable new washer costs $700. Repair cost is 46% of replacement — under 50%, and the machine still has years of life left. <strong>Repair wins.</strong></p>
    <p>Contrast: your 13-year-old refrigerator needs a new compressor: estimated $550. A new comparable fridge runs $900. Repair is 61% of replacement, and the unit is near end of life. <strong>Replacement makes more sense.</strong></p>

    <h2>How to Avoid Overpaying for Appliance Repair</h2>
    <ul>
      <li><strong>Get a clear diagnostic fee upfront.</strong> A reputable company will tell you the service call fee before they arrive. Ours is always disclosed — and applied toward the repair if you proceed.</li>
      <li><strong>Ask for an itemized quote.</strong> Parts + labor should be listed separately so you can compare part prices.</li>
      <li><strong>Check if your appliance is under warranty.</strong> Manufacturer warranties typically cover 1 year on parts and labor; extended warranties cover more.</li>
      <li><strong>Don't pay for a quote that amounts to "you need a new machine."</strong> Any qualified technician should be able to diagnose the specific fault and give you a cost estimate.</li>
    </ul>

    <h2>Our Pricing at Prime Appliance Repair</h2>
    <p>We charge a flat diagnostic fee that gets credited toward your repair. We provide a written estimate before starting any work — no surprises. Our rates are competitive for the Clovis and Fresno market, and we stock common parts on our trucks to complete most repairs in a single visit.</p>
    <p><a href="/book-an-appointment/" style="color:var(--primary);font-weight:600;">Book a service call today</a> or call us at <a href="tel:5596003037" style="color:var(--primary);font-weight:600;">(559) 600-3037</a>.</p>"""
  },

  {
    "slug": "when-everything-still-works-but-somethings-clearly-wrong",
    "title": "When Everything \"Still Works\"… But Something's Clearly Wrong",
    "meta": "That nagging feeling your appliance isn't right — even though it still runs — is often worth acting on. Learn the subtle warning signs that a repair is needed soon.",
    "category": "Appliance Problems & Fixes",
    "category_slug": "appliance-problems-fixes",
    "date": "April 11, 2026",
    "read_time": "3 min",
    "img": "https://appliancerepairclovis.com/wp-content/uploads/2026/04/9652c7398ec0b54a986526ec323ce798.jpg",
    "content": """    <p>There's a moment every homeowner hits. The appliance is technically still running — but something is clearly off. Maybe the dishwasher finishes its cycle but the dishes feel grimy. Maybe the dryer runs for an hour but the clothes still feel damp. Maybe the washing machine makes a new noise that you've decided to just… ignore.</p>

    <p>This is the gray zone: appliances that haven't failed yet, but are telling you something is wrong. Most people wait. That usually makes things worse — and more expensive.</p>

    <h2>Why "It Still Works" Is Dangerous Logic</h2>
    <p>A car that overheats "still drives." A tire with a slow leak "still rolls." In both cases, doing nothing leads to a much bigger, costlier problem down the road. Appliances work the same way. A washing machine with a worn drum bearing will eventually seize. A refrigerator with dirty condenser coils will eventually burn out its compressor.</p>

    <div class="highlight-box"><p>Small problems caught early = small repair bills. Small problems ignored = large repair bills or full replacement.</p></div>

    <h2>The "Clearly Something's Wrong" Warning Signs</h2>

    <h3>Refrigerator</h3>
    <ul>
      <li>Runs longer than it used to between cycles</li>
      <li>Ice cream is soft in the freezer</li>
      <li>You notice a slight chemical or musty smell when you open it</li>
      <li>Door doesn't seal as firmly as it used to</li>
    </ul>

    <h3>Washing Machine</h3>
    <ul>
      <li>Vibrates or "walks" more than before during the spin cycle</li>
      <li>Clothes smell musty after washing (mold in the drum seal or detergent drawer)</li>
      <li>Cycle times are noticeably longer</li>
      <li>You hear grinding, squeaking, or knocking during agitation</li>
    </ul>

    <h3>Dryer</h3>
    <ul>
      <li>Clothes need two cycles to feel fully dry</li>
      <li>Dryer feels hotter than usual on the outside</li>
      <li>Burning smell — even faint — at any point during operation</li>
      <li>Drum light works but cycle doesn't start consistently</li>
    </ul>

    <h3>Dishwasher</h3>
    <ul>
      <li>Dishes feel gritty or have white film despite using the same detergent</li>
      <li>Standing water at the bottom after the cycle ends</li>
      <li>Spray arms wobble or you notice less water pressure during wash</li>
    </ul>

    <h3>Oven / Range</h3>
    <ul>
      <li>Dishes cook unevenly — one side browning faster than the other</li>
      <li>Oven takes noticeably longer to preheat</li>
      <li>Gas burner ignites inconsistently or the flame is uneven</li>
      <li>Control panel feels sluggish or some buttons require extra pressure</li>
    </ul>

    <h2>What To Do When You Notice These Signs</h2>
    <p>First, don't convince yourself it'll go away on its own. With appliances, problems almost never resolve themselves — they escalate.</p>
    <p>Second, note when it started and whether anything changed around that time (new laundry detergent, power outage, installation of a new appliance nearby).</p>
    <p>Third, call a technician for a diagnostic. Most reputable repair companies charge a service call fee that gets applied toward the repair — so there's no financial downside to getting it checked early. The earlier the diagnosis, the more likely it's a minor, inexpensive fix.</p>

    <p>At Prime Appliance Repair, we handle exactly these kinds of "something's off but I'm not sure what" calls all the time. We diagnose it accurately, explain what's happening in plain English, and give you a straight recommendation — repair now, or wait. <a href="/book-an-appointment/" style="color:var(--primary);font-weight:600;">Book a visit here</a> or call <a href="tel:5596003037" style="color:var(--primary);font-weight:600;">(559) 600-3037</a>.</p>"""
  },

  {
    "slug": "why-your-dryer-takes-too-long-to-dry-clothes",
    "title": "Why Your Dryer Takes Too Long to Dry Clothes",
    "meta": "If your dryer needs two cycles to dry clothes, the fix is often simple — but could also signal a serious issue. Learn the most common causes and what to do about each one.",
    "category": "Appliance Problems & Fixes",
    "category_slug": "appliance-problems-fixes",
    "date": "April 9, 2026",
    "read_time": "4 min",
    "img": "https://appliancerepairclovis.com/wp-content/uploads/2026/04/vecteezy_a-broken-washing-machine-with-opened-door-dirty-clothes_58009100.jpg",
    "content": """    <p>Running your dryer twice to dry a single load is one of the most common appliance complaints — and also one of the most misunderstood. People assume it means the dryer is "getting old," but in most cases, there's a specific, diagnosable cause. Many of them are inexpensive fixes.</p>

    <p>Here's a breakdown of every common reason a dryer takes too long — from the free DIY fixes to the repairs that need a technician.</p>

    <h2>Start Here: The Free Fixes</h2>

    <h3>1. Clogged Lint Trap</h3>
    <p>This sounds too simple, but a severely clogged lint trap cuts airflow dramatically. Clean it after every single load — not just when it looks full. And once a month, wash the trap with warm water and a soft brush to remove detergent residue that coats the mesh and restricts airflow even when the lint is removed.</p>

    <h3>2. Blocked or Kinked Exhaust Vent</h3>
    <p>This is the #1 cause of slow drying and one of the most overlooked. Your dryer pushes hot, moist air out through a vent to the outside of your home. If that vent is:</p>
    <ul>
      <li>Clogged with lint (even partial blockage cuts efficiency 50%+)</li>
      <li>Crushed or kinked behind the dryer</li>
      <li>Too long or with too many 90° bends</li>
      <li>Terminated with a screen that's collecting debris</li>
    </ul>
    <p>…then moist air can't escape and your clothes never fully dry, no matter how long the dryer runs. Clean your exhaust vent at least once a year with a dryer vent brush kit (available for ~$20). If the exterior vent flap doesn't open freely when the dryer is running, it's blocked.</p>

    <div class="highlight-box"><p><strong>Safety note:</strong> Blocked dryer vents are a leading cause of house fires. This isn't just an efficiency issue — it's a safety issue. Don't ignore it.</p></div>

    <h3>3. Overloaded Drum</h3>
    <p>Stuffing the dryer past 75–80% capacity blocks hot air circulation. Clothes tumble against each other without proper airflow. Split large loads and you'll often find each half dries in a normal cycle time.</p>

    <h2>If the Free Fixes Don't Help: Time for a Technician</h2>

    <h3>4. Faulty Heating Element (Electric Dryers)</h3>
    <p>The heating element heats the air that dries your clothes. When it partially fails, the dryer still runs and produces some heat — but not enough to dry efficiently. If your dryer feels warm but not hot, or if one section of the element has burned out, replacement is the fix. This is a common repair ($80–$180 in most cases).</p>

    <h3>5. Defective Gas Valve Coils (Gas Dryers)</h3>
    <p>Gas dryers rely on solenoid coils to open the gas valve. When these wear out, the burner may ignite briefly then shut off — leaving the drum spinning with barely warm air. The symptom: dryer runs, doesn't heat much, takes forever. Gas valve coil replacement is typically $100–$200.</p>

    <h3>6. Cycling Thermostat Failure</h3>
    <p>The cycling thermostat regulates dryer temperature during the cycle. A faulty thermostat often causes the dryer to run at lower temperatures than designed — resulting in damp clothes after a full cycle. This is an inexpensive part but requires disassembly to replace.</p>

    <h3>7. Blower Wheel Clog or Failure</h3>
    <p>The blower wheel pulls air through the drum and pushes it out the exhaust. Lint and debris can accumulate on the wheel, or the wheel can crack. Either reduces airflow significantly. You'll often hear a rumbling or rattling sound alongside the drying issues.</p>

    <h3>8. Moisture Sensor Issues</h3>
    <p>Modern dryers use moisture sensors (two metal bars inside the drum) to detect when clothes are dry and shut off automatically. If the sensors are coated with dryer sheet residue, they may signal "dry" prematurely — shutting the cycle off with damp clothes — or conversely, fail to stop the dryer at all. Clean the sensors with rubbing alcohol every few months.</p>

    <h2>A Quick Diagnosis Approach</h2>
    <ol>
      <li>Clean the lint trap and run a small test load — if it dries normally, the problem was simple overloading or lint buildup</li>
      <li>Disconnect the exhaust vent and run the dryer briefly — if it heats much better, the vent is the issue</li>
      <li>If the dryer doesn't feel hot at all, suspect the heating element (electric) or gas valve coils (gas)</li>
      <li>If it's warm but not hot, suspect the cycling thermostat</li>
    </ol>

    <p>Still not sure? Our technicians carry the most common dryer parts on every service truck, and most dryer repairs in Clovis and Fresno are completed in a single visit. <a href="/book-an-appointment/" style="color:var(--primary);font-weight:600;">Book an appointment here</a>.</p>"""
  },

  {
    "slug": "washer-maintenance-tips-most-people-ignore",
    "title": "Washer Maintenance Tips Most People Ignore",
    "meta": "Your washing machine needs regular maintenance to avoid mold, odors, and costly repairs. Here are the most important washer care tips that most homeowners skip.",
    "category": "Maintenance & Insider Tips",
    "category_slug": "maintenance-insider-tips",
    "date": "April 6, 2026",
    "read_time": "4 min",
    "img": "https://appliancerepairclovis.com/wp-content/uploads/2026/04/vecteezy_the-plumber-tries-to-repair-a-broken-washing-machine_58009083.jpg",
    "content": """    <p>Washing machines are one of the most used appliances in any home — and one of the least maintained. People rarely think about their washer until it floods the laundry room, starts leaving clothes smelling worse than before, or stops working altogether.</p>

    <p>The good news: a few simple habits can extend the life of your washing machine by years and prevent the most common (and costly) repairs. Here are the maintenance steps most people skip entirely.</p>

    <h2>Front-Load Washer Maintenance</h2>

    <h3>1. Clean the Door Gasket Regularly</h3>
    <p>The rubber gasket (the seal around the door) is one of the most overlooked parts of a front-load washer. Moisture, detergent residue, and lint accumulate in its folds — creating the perfect environment for black mold. If your freshly washed clothes smell musty, mold in the door gasket is usually the culprit.</p>
    <p><strong>What to do:</strong> After every wash cycle, wipe the gasket dry with a clean cloth. Pull back the folds and check for mold. Monthly, clean it with a diluted bleach solution or white vinegar. Leave the door open between cycles to allow it to air dry.</p>

    <h3>2. Leave the Door Open After Washing</h3>
    <p>This is simple and most people don't do it. Closing the washer door immediately traps moisture inside the drum. Over time, this creates mold and mildew — which you then transfer back onto your "clean" clothes. After you remove the laundry, leave the door ajar. Even an inch makes a significant difference.</p>

    <h3>3. Clean the Detergent Drawer</h3>
    <p>The detergent, fabric softener, and pre-soak compartments accumulate residue that can grow mold and cause dispensing problems. Pull the drawer all the way out (most slide out completely) and wash it in warm soapy water. Do this monthly.</p>

    <h3>4. Run a Monthly Cleaning Cycle</h3>
    <p>Most modern washers have a dedicated "Clean Washer" or "Tub Clean" cycle. Run it monthly with a washer cleaning tablet or a cup of white vinegar + half a cup of baking soda. This removes soap scum, mineral deposits, and bacteria from the drum and internal components.</p>

    <div class="highlight-box"><p><strong>Pro tip:</strong> Never use more detergent than recommended. Excess suds don't clean better — they leave residue on clothes, build up in the drum, and make moisture problems worse. High-efficiency (HE) detergent is required for HE machines.</p></div>

    <h2>Top-Load Washer Maintenance</h2>

    <h3>5. Check and Clean the Lint Filter</h3>
    <p>Many top-load washers have a lint filter that requires periodic cleaning — but unlike dryer lint traps, most people don't know it exists. It's usually located inside the drum (near the agitator or in a corner), in the drainage pump, or in the drain hose. Check your owner's manual. A clogged lint filter reduces wash performance and strains the drain pump.</p>

    <h3>6. Avoid Overloading</h3>
    <p>Overstuffing the washer doesn't just reduce washing effectiveness — it strains the drum bearings, transmission (on agitator models), and motor. Over time, this accelerates wear dramatically. Fill the drum no more than 3/4 full, and make sure items can tumble freely.</p>

    <h2>Universal Washer Maintenance</h2>

    <h3>7. Inspect the Fill Hoses Every Year</h3>
    <p>The rubber hoses connecting your washer to the water supply are often forgotten — until they burst and cause thousands of dollars in water damage. Check them annually for bulging, cracking, or brittleness. Replace rubber hoses every 5 years, or immediately if you see any damage. Consider upgrading to braided stainless steel hoses (~$15–20) which are far more durable.</p>

    <h3>8. Level the Machine</h3>
    <p>An unlevel washing machine vibrates excessively during the spin cycle, which wears out bearings, shock absorbers, and the drum suspension system prematurely. Use a level across the top of the machine. Adjust the leveling feet until it sits perfectly even — all four feet firmly on the floor.</p>

    <h3>9. Keep the Area Around the Washer Clear</h3>
    <p>The washer needs adequate ventilation. Don't stack items on top of or directly against it. Lint and debris under the machine can cause overheating in the motor area and are a fire hazard when combined with dryer proximity.</p>

    <h2>When to Call a Technician</h2>
    <p>Even well-maintained washers eventually need repair. Watch for these red flags and don't wait:</p>
    <ul>
      <li>Water visible on the floor around or under the machine</li>
      <li>The drum doesn't spin, or spins weakly</li>
      <li>The machine won't drain after the cycle</li>
      <li>Error codes on digital display models</li>
      <li>Loud grinding, banging, or squealing during operation</li>
    </ul>
    <p>Prime Appliance Repair handles washing machine repairs for all major brands across Clovis, Fresno, and the Central Valley. <a href="/book-an-appointment/" style="color:var(--primary);font-weight:600;">Book a service appointment</a> or call <a href="tel:5596003037" style="color:var(--primary);font-weight:600;">(559) 600-3037</a>.</p>"""
  },

  {
    "slug": "repair-vs-replace",
    "title": "Repair vs. Replace: How to Make the Right Call for Your Appliance",
    "meta": "Should you repair your broken appliance or replace it? Use this practical guide to make the financially smart decision every time.",
    "category": "Appliance Problems & Fixes",
    "category_slug": "appliance-problems-fixes",
    "date": "April 3, 2026",
    "read_time": "5 min",
    "img": "https://appliancerepairclovis.com/wp-content/uploads/2026/04/vecteezy_senior-technician-fixing-dishwasher-at-kitchen_42863819.jpg",
    "content": """    <p>When an appliance breaks, most people immediately Google "replace refrigerator" or "new washing machine deals" — because that feels like the decisive, modern thing to do. But for the majority of appliance failures, especially for units under 10 years old, repair is significantly less expensive and the financially smarter choice.</p>

    <p>The problem is that most homeowners don't have a clear framework for making this decision. Here's the one we use and recommend.</p>

    <h2>The Three-Factor Decision Framework</h2>

    <h3>Factor 1: The Age Rule</h3>
    <p>Every appliance has an expected lifespan. If your appliance has already lived most of that life, putting money into a repair makes less sense than if it's still relatively young.</p>
    <ul>
      <li>Refrigerator: 13–17 years</li>
      <li>Washer: 10–14 years</li>
      <li>Dryer: 12–18 years</li>
      <li>Dishwasher: 9–12 years</li>
      <li>Oven/Range: 13–20 years</li>
      <li>Microwave: 9–12 years</li>
    </ul>
    <p>If your appliance is in the <strong>first 60–70% of its expected lifespan</strong>, repair almost always wins on cost. If it's in the final 30%, weigh more carefully.</p>

    <h3>Factor 2: The 50% Rule</h3>
    <p>Compare the repair cost to the cost of an equivalent replacement:</p>
    <ul>
      <li>If repair cost is <strong>under 50%</strong> of replacement cost → repair</li>
      <li>If repair cost is <strong>50–75%</strong> of replacement cost → depends on age and condition</li>
      <li>If repair cost is <strong>over 75%</strong> of replacement cost → lean toward replace</li>
    </ul>

    <div class="highlight-box"><p><strong>Example:</strong> 7-year-old dryer, repair estimate $200, comparable new dryer $700. Repair cost = 29% of replacement. Decision: repair easily.</p></div>
    <div class="highlight-box"><p><strong>Example:</strong> 13-year-old dishwasher, repair estimate $380, comparable new dishwasher $500. Repair cost = 76% of replacement, and the appliance is near end of life. Decision: replace.</p></div>

    <h3>Factor 3: Repair History</h3>
    <p>Has the appliance required multiple repairs in recent years? If you've already spent $300 on repairs in the past 18 months and you're now facing another $250 repair, that changes the math. At some point, a chronically troubled appliance signals systemic decline — not just an isolated issue.</p>
    <p>However, one or two repairs over the life of an appliance is completely normal — not a sign of a "bad" unit.</p>

    <h2>When to Always Repair</h2>
    <ul>
      <li>The appliance is under manufacturer or extended warranty</li>
      <li>The appliance is less than 5 years old</li>
      <li>It's a high-end appliance (Sub-Zero, Viking, Wolf, Miele) — repair almost always beats replacement cost</li>
      <li>The repair addresses a single, clearly identified component failure</li>
      <li>Repair cost is under 30% of replacement cost</li>
    </ul>

    <h2>When to Lean Toward Replace</h2>
    <ul>
      <li>Appliance is past or near its expected lifespan</li>
      <li>Compressor failure on an older refrigerator (compressor repairs are expensive and the underlying unit may fail again soon)</li>
      <li>Control board failure on an older unit (costly repair that doesn't address underlying age-related degradation)</li>
      <li>You've had 3+ repairs in the past 2 years</li>
      <li>Replacement would offer significantly better energy efficiency (new refrigerators use up to 40% less energy than 15-year-old units)</li>
    </ul>

    <h2>The Energy Efficiency Factor</h2>
    <p>Older appliances — especially refrigerators — can cost $50–$100 more per year to operate than newer ENERGY STAR models. Over 5 years, that's $250–$500 in extra utility costs. If you're repairing a 15-year-old refrigerator, factor in those ongoing operating costs alongside the repair bill.</p>

    <h2>Get a Diagnosis First</h2>
    <p>You can't make this decision without knowing the actual repair cost — and many people assume the worst before getting a professional opinion. We regularly diagnose "dead" appliances that need a $60 part and 30 minutes of labor.</p>
    <p>Our service call fee is credited toward the repair if you proceed — so there's no risk in getting the facts before you decide. <a href="/book-an-appointment/" style="color:var(--primary);font-weight:600;">Schedule a diagnostic here</a> or call <a href="tel:5596003037" style="color:var(--primary);font-weight:600;">(559) 600-3037</a>.</p>"""
  },
]

# ─────────────────────────────────────────────
# CATEGORY PAGES
# ─────────────────────────────────────────────

def post_card(href, img, alt, cat, title, date, excerpt):
    return f"""      <a href="{href}" class="blog-list-card">
        <img src="{img}" alt="{alt}" loading="lazy">
        <div class="blog-list-card-body">
          <span class="blog-cat">{cat}</span>
          <h3>{title}</h3>
          <p style="font-size:13px;color:#848484;margin-bottom:8px;">{date}</p>
          <p>{excerpt}</p>
          <span class="read-more">Read More →</span>
        </div>
      </a>"""

categories = [
  {
    "slug": "appliance-problems-fixes",
    "title": "Appliance Problems & Fixes",
    "meta": "Guides on common appliance problems and how to fix them. From refrigerators running warm to washers that won't spin — helpful advice from Prime Appliance Repair.",
    "posts": [
      post_card("/your-fridge-is-lying-to-you/",
        "https://appliancerepairclovis.com/wp-content/uploads/2026/04/vecteezy_woman-looking-disappointed-at-an-empty-fridge-feeling_69408907.jpg",
        "Your Fridge Is Lying to You", "Appliance Problems &amp; Fixes",
        "Your Fridge Is Lying to You", "April 18, 2026",
        "It looks fine. The light turns on. It hums. But your fridge may be quietly failing — here's how to tell."),
      post_card("/when-everything-still-works-but-somethings-clearly-wrong/",
        "https://appliancerepairclovis.com/wp-content/uploads/2026/04/9652c7398ec0b54a986526ec323ce798.jpg",
        "When Everything Still Works", "Appliance Problems &amp; Fixes",
        "When Everything \"Still Works\"… But Something's Clearly Wrong", "April 11, 2026",
        "That nagging feeling your appliance isn't quite right — even though it runs — is usually worth acting on."),
      post_card("/why-your-dryer-takes-too-long-to-dry-clothes/",
        "https://appliancerepairclovis.com/wp-content/uploads/2026/04/vecteezy_a-broken-washing-machine-with-opened-door-dirty-clothes_58009100.jpg",
        "Dryer Takes Too Long", "Appliance Problems &amp; Fixes",
        "Why Your Dryer Takes Too Long to Dry Clothes", "April 9, 2026",
        "Running two cycles to dry one load? Here are all the causes — from free DIY fixes to parts that need replacing."),
      post_card("/repair-vs-replace/",
        "https://appliancerepairclovis.com/wp-content/uploads/2026/04/vecteezy_senior-technician-fixing-dishwasher-at-kitchen_42863819.jpg",
        "Repair vs Replace", "Appliance Problems &amp; Fixes",
        "Repair vs. Replace: How to Make the Right Call", "April 3, 2026",
        "A practical framework to decide whether repairing your broken appliance or buying new is the smarter financial move."),
    ]
  },
  {
    "slug": "repair-cost-guides",
    "title": "Repair Cost Guides",
    "meta": "Honest appliance repair cost guides for 2026. What does refrigerator repair cost? Washer repair? Dryer repair? Get the numbers before you call anyone.",
    "posts": [
      post_card("/appliance-repair-cost-guide/",
        "https://appliancerepairclovis.com/wp-content/uploads/2026/04/vecteezy_technician-or-worker-in-uniform-installs-dishwasher-into-the_35202703-1.jpg",
        "Appliance Repair Cost Guide", "Repair Cost Guides",
        "Appliance Repair Cost Guide: What to Expect in 2026", "April 16, 2026",
        "Typical repair costs for refrigerators, washers, dryers, dishwashers, and ovens — plus the 50% rule for deciding whether to repair or replace."),
    ]
  },
  {
    "slug": "maintenance-insider-tips",
    "title": "Maintenance & Insider Tips",
    "meta": "Practical appliance maintenance tips from professional repair technicians. Keep your appliances running longer, avoid costly repairs, and save on energy.",
    "posts": [
      post_card("/washer-maintenance-tips-most-people-ignore/",
        "https://appliancerepairclovis.com/wp-content/uploads/2026/04/vecteezy_the-plumber-tries-to-repair-a-broken-washing-machine_58009083.jpg",
        "Washer Maintenance Tips", "Maintenance &amp; Tips",
        "Washer Maintenance Tips Most People Ignore", "April 6, 2026",
        "Simple habits that can prevent mold, odors, and costly washer repairs — from cleaning the door gasket to inspecting fill hoses."),
    ]
  },
]

# ─────────────────────────────────────────────
# WRITE FILES
# ─────────────────────────────────────────────

for post in posts:
    out_dir = os.path.join(BASE, post["slug"])
    os.makedirs(out_dir, exist_ok=True)
    html = blog_page(
        post["slug"], post["title"], post["meta"],
        post["category"], post["category_slug"],
        post["date"], post["read_time"],
        post["img"], post["content"]
    )
    out_path = os.path.join(out_dir, "index.html")
    with open(out_path, "w") as f:
        f.write(html)
    print(f"✅ /{post['slug']}/index.html")

for cat in categories:
    out_dir = os.path.join(BASE, "category", cat["slug"])
    os.makedirs(out_dir, exist_ok=True)
    posts_html = "\n".join(cat["posts"])
    html = category_page(cat["slug"], cat["title"], cat["meta"], posts_html)
    out_path = os.path.join(out_dir, "index.html")
    with open(out_path, "w") as f:
        f.write(html)
    print(f"✅ /category/{cat['slug']}/index.html")

print("\n✅ All blog + category pages done!")
