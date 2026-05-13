import os

BASE = "/home/user/webapp/static-site"

# ── shared snippets ───────────────────────────────────────────────
def head(title, desc, canonical):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://appliancerepairclovis.com{canonical}">
<link rel="stylesheet" href="/css/style.css">
<link rel="icon" href="https://appliancerepairclovis.com/wp-content/uploads/2022/10/appliance-repair.png">
</head>
<body>'''

HEADER = '''<header>
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
</header>'''

FOOTER = '''<footer>
  <div class="footer-inner">
    <div class="footer-col">
      <h6>Prime Appliance Repair</h6>
      <p>Serving Fresno, Clovis, Madera,<br>Sanger, Fowler &amp; surrounding areas.</p>
      <p style="margin-top:12px;color:#c1c1c1;">📞 <a href="tel:5597650303">(559) 765-0303</a></p>
      <p style="color:#c1c1c1;">✉ <a href="mailto:appliancerepairserviceus@gmail.com">appliancerepairserviceus@gmail.com</a></p>
    </div>
    <div class="footer-col">
      <h6>Services</h6>
      <a href="/refrigerator-repair-clovis-ca/">Refrigerator Repair</a>
      <a href="/washer-repair-clovis-ca/">Washer Repair</a>
      <a href="/dryer-repair-clovis-ca/">Dryer Repair</a>
      <a href="/dishwasher-repair-clovis-ca/">Dishwasher Repair</a>
      <a href="/oven-repair-clovis-ca/">Oven &amp; Stove Repair</a>
      <a href="/microwave-repair-clovis-ca/">Microwave Repair</a>
      <a href="/freezer-repair-clovis-ca/">Freezer Repair</a>
    </div>
    <div class="footer-col">
      <h6>Service Areas</h6>
      <a href="/fresno-appliance-repair/">Fresno</a>
      <a href="/clovis-appliance-repair/">Clovis</a>
      <a href="/madera-appliance-repair/">Madera</a>
      <a href="/sanger-appliance-repair/">Sanger</a>
      <a href="/fowler-appliance-repair/">Fowler</a>
      <a href="/fraint-appliance-repair/">Friant</a>
    </div>
    <div class="footer-col">
      <h6>Company</h6>
      <a href="/about-us/">About Us</a>
      <a href="/blog-2/">Blog</a>
      <a href="/contact-us/">Contact</a>
      <a href="/book-an-appointment/">Book Appointment</a>
      <a href="/privacy-policy/">Privacy Policy</a>
    </div>
  </div>
  <div class="footer-bottom">
    <p>&copy; 2026 Prime Appliance Repair Services. All rights reserved.</p>
    <p><a href="/privacy-policy/" style="color:#c1c1c1;">Privacy Policy</a></p>
  </div>
</footer>
<script src="/js/main.js"></script>
</body>
</html>'''

CTA_BANNER = '''<section class="cta-banner">
  <div class="container">
    <h2>Ready to Fix Your Appliance?</h2>
    <p>Don't wait — call now for same-day service or schedule your appointment online.</p>
    <div class="cta-banner-btns">
      <a href="tel:5597650303" class="btn-white">📞 (559) 765-0303</a>
      <a href="/book-an-appointment/" class="btn-accent">Book Appointment</a>
    </div>
  </div>
</section>'''

SIDEBAR = '''<aside class="content-sidebar">
  <div class="cta-box">
    <h4>Schedule Service Today</h4>
    <p>Same-day &amp; next-day appointments available.</p>
    <a href="tel:5597650303" class="btn-white">📞 (559) 765-0303</a>
    <a href="/book-an-appointment/" class="btn-accent" style="margin-top:8px;">Book Online</a>
  </div>
  <div class="services-sidebar">
    <h5>Our Services</h5>
    <a href="/refrigerator-repair-clovis-ca/">Refrigerator Repair</a>
    <a href="/freezer-repair-clovis-ca/">Freezer Repair</a>
    <a href="/washer-repair-clovis-ca/">Washer Repair</a>
    <a href="/dryer-repair-clovis-ca/">Dryer Repair</a>
    <a href="/dishwasher-repair-clovis-ca/">Dishwasher Repair</a>
    <a href="/oven-repair-clovis-ca/">Oven &amp; Stove Repair</a>
    <a href="/microwave-repair-clovis-ca/">Microwave Repair</a>
    <a href="/wine-cooler-repair-clovis-ca/">Wine Cooler Repair</a>
    <a href="/ice-maker-repair-clovis-ca/">Ice Maker Repair</a>
    <a href="/garbage-disposal-repair-clovis-ca/">Garbage Disposal Repair</a>
  </div>
</aside>'''

BRANDS_SECTION = '''<section class="brands-section">
  <div class="container">
    <h3>Appliance Brands We Service</h3>
    <p>Here is a comprehensive list of appliance brands we service regularly. If you don't see your brand listed, feel free to contact us directly.</p>
    <div class="brands-grid">
      <div class="brand-item">Whirlpool</div>
      <div class="brand-item">Samsung</div>
      <div class="brand-item">LG</div>
      <div class="brand-item">GE</div>
      <div class="brand-item">Maytag</div>
      <div class="brand-item">Bosch</div>
      <div class="brand-item">KitchenAid</div>
      <div class="brand-item">Frigidaire</div>
      <div class="brand-item">Sub-Zero</div>
      <div class="brand-item">Viking</div>
      <div class="brand-item">Thermador</div>
      <div class="brand-item">Electrolux</div>
      <div class="brand-item">Kenmore</div>
      <div class="brand-item">Amana</div>
      <div class="brand-item">Miele</div>
    </div>
  </div>
</section>'''

# ── service page generator ────────────────────────────────────────
def service_page(slug, title, meta_desc, h1, intro, problems_title, problems, process_content, why_items, schedule_text, also_services=None):
    also = ""
    if also_services:
        items = "".join(f"<li>{s}</li>" for s in also_services)
        also = f'''<h2>Complete Appliance Repair</h2><ul>{items}</ul>'''
    problems_li = "".join(f"<li>{p}</li>" for p in problems)
    why_li = "".join(f"<li>{w}</li>" for w in why_items)
    html = head(title, meta_desc, f"/{slug}/") + HEADER + f'''
<section class="page-hero">
  <div class="container">
    <h1>{h1}</h1>
    <p>{intro}</p>
    <div class="page-hero-btns">
      <a href="tel:5597650303" class="btn-white">📞 (559) 765-0303</a>
      <a href="/book-an-appointment/" class="btn-accent">Book Online</a>
    </div>
  </div>
</section>
<section class="content-section">
  <div class="content-inner">
    <main class="content-main">
      <h2>{problems_title}</h2>
      <ul>{problems_li}</ul>
      <h2>Our Repair Process</h2>
      <p>{process_content}</p>
      {also}
      <h2>Why Choose Our Service</h2>
      <ul>{why_li}</ul>
      <h2>Schedule Your Repair</h2>
      <p>{schedule_text}</p>
    </main>
    {SIDEBAR}
  </div>
</section>
{CTA_BANNER}
''' + FOOTER
    path = f"{BASE}/{slug}/index.html"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path,"w").write(html)
    print(f"✅ /{slug}/")

# ── location page generator ───────────────────────────────────────
def location_page(slug, title, meta_desc, h1, hero_sub, body_html):
    html = head(title, meta_desc, f"/{slug}/") + HEADER + f'''
<section class="page-hero">
  <div class="container">
    <h1>{h1}</h1>
    <p>{hero_sub}</p>
    <div class="page-hero-btns">
      <a href="tel:5597650303" class="btn-white">📞 (559) 765-0303</a>
      <a href="/book-an-appointment/" class="btn-accent">Book Online</a>
    </div>
    <p style="margin-top:18px;font-size:15px;color:rgba(255,255,255,0.75);">✔ Same-Day or Next-Day Service Available</p>
  </div>
</section>
<section class="content-section">
  <div class="content-inner">
    <main class="content-main">{body_html}</main>
    {SIDEBAR}
  </div>
</section>
{BRANDS_SECTION}
{CTA_BANNER}
''' + FOOTER
    path = f"{BASE}/{slug}/index.html"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path,"w").write(html)
    print(f"✅ /{slug}/")

# ── simple contact-style page ─────────────────────────────────────
def simple_page(slug, title, meta_desc, h1, body_html):
    html = head(title, meta_desc, f"/{slug}/") + HEADER + f'''
<section class="page-hero">
  <div class="container">
    <h1>{h1}</h1>
    <div class="page-hero-btns" style="margin-top:20px;">
      <a href="tel:5597650303" class="btn-white">📞 (559) 765-0303</a>
      <a href="/book-an-appointment/" class="btn-accent">Book Appointment</a>
    </div>
  </div>
</section>
<section class="content-section">
  <div class="content-inner">
    <main class="content-main">{body_html}</main>
    {SIDEBAR}
  </div>
</section>
{BRANDS_SECTION}
{CTA_BANNER}
''' + FOOTER
    path = f"{BASE}/{slug}/index.html"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path,"w").write(html)
    print(f"✅ /{slug}/")

WHY = ["Experienced and professional technicians","Honest diagnostics — no unnecessary repairs","Warranty on parts and labor","Fast scheduling and reliable service","Service directly at your home"]
ALSO = ["Refrigerators","Washers &amp; dryers","Dishwashers","Ovens &amp; stoves","Microwaves"]

# ════════════════════════════════════════════
# SERVICE PAGES
# ════════════════════════════════════════════
service_page("refrigerator-repair-clovis-ca",
  "Refrigerator Repair Clovis, CA | Prime Appliance Repair",
  "Professional refrigerator repair in Clovis, CA. Fast, reliable service with warranty on parts and labor. Call (559) 765-0303.",
  "Refrigerator Repair in Clovis, CA",
  "A refrigerator that isn't cooling properly can quickly turn into a bigger problem. We provide professional refrigerator repair in Clovis, helping homeowners restore proper cooling and avoid costly replacements.",
  "Common Refrigerator Problems We Fix",
  ["Refrigerator not cooling or not cold enough","Freezer working but fridge is warm","Fridge running constantly or making unusual noise","Water leaking inside or under the unit","Ice maker not working","Water dispenser not dispensing","Frost buildup in freezer"],
  "Every service starts with a full inspection to find the exact cause of the issue. Once we identify the problem, we explain the solution clearly and proceed with the repair using quality parts. Our goal is to fix the issue correctly the first time, so your refrigerator works reliably again.",
  WHY,
  "If your refrigerator isn't working like it should, don't wait for it to stop completely. Call today or schedule your refrigerator repair in Clovis and get your kitchen back to normal.",
  ALSO)

service_page("washer-repair-clovis-ca",
  "Washer Repair Clovis, CA | Prime Appliance Repair",
  "Fast, reliable washer repair in Clovis, CA. In-home service with warranty. Same-day appointments available. Call (559) 765-0303.",
  "Washer Repair in Clovis, CA",
  "When your washer starts acting differently, it's usually not random — it's a sign something inside isn't working as it should. We provide dependable washer repair in Clovis, delivering in-home service designed to restore proper performance quickly.",
  "Signs Your Washer Needs Service",
  ["Clothes still wet after the cycle","Washer struggling to spin evenly","Water draining slowly or not fully","Soap or residue left on clothes","Cycles running longer than usual","New or unusual noises during operation","Won't start or power on"],
  "Instead of replacing parts blindly, we perform a full diagnostic to identify exactly what's affecting your washer's performance. Once the issue is confirmed, we explain the solution clearly and complete the repair using reliable parts.",
  WHY,
  "If your washer isn't performing the way it used to, it's time to have it checked. Call today to schedule washer repair in Clovis.",
  ALSO)

service_page("dryer-repair-clovis-ca",
  "Dryer Repair Clovis, CA | Prime Appliance Repair",
  "Expert dryer repair in Clovis, CA. Fast in-home service, warranty on parts and labor. Call (559) 765-0303 for same-day service.",
  "Dryer Repair in Clovis, CA",
  "A dryer that isn't heating or takes forever to dry clothes disrupts your daily routine. We provide expert dryer repair in Clovis with fast in-home service and warranty on every repair.",
  "Common Dryer Problems We Fix",
  ["Dryer not heating","Clothes taking too long to dry","Dryer stops mid-cycle","Loud noises or vibrations","Drum not spinning","Burning smell or overheating","Door won't close properly"],
  "Every dryer repair starts with a full inspection to identify the exact issue. Once diagnosed, we explain the problem clearly and complete the repair using quality parts. This helps avoid repeat issues and ensures your dryer works safely and efficiently.",
  WHY,
  "If your dryer isn't performing like it should, professional service can restore efficiency and reliability. Call today to schedule dryer repair in Clovis.",
  ALSO)

service_page("dishwasher-repair-clovis-ca",
  "Dishwasher Repair Clovis, CA | Prime Appliance Repair",
  "Reliable dishwasher repair in Clovis, CA. In-home service, warranty on parts and labor. Call (559) 765-0303.",
  "Dishwasher Repair in Clovis, CA",
  "A dishwasher should save you time — not leave you with dirty dishes or standing water. We provide reliable dishwasher repair in Clovis, with in-home service focused on restoring proper cleaning performance.",
  "Common Dishwasher Issues We Fix",
  ["Dishes coming out dirty or cloudy","Water not draining after the cycle","Dishwasher taking too long to finish","Leaks under or around the unit","Unusual noises during operation","Dishwasher not starting","Door latch broken"],
  "We start by identifying the exact cause. After a full inspection, we explain what's affecting your dishwasher's performance and complete the repair using quality parts. This helps restore consistent cleaning results and prevents repeat issues.",
  WHY,
  "If your dishwasher isn't delivering clean results, call today to schedule dishwasher repair in Clovis.",
  ALSO)

service_page("oven-repair-clovis-ca",
  "Oven Repair Clovis, CA | Prime Appliance Repair",
  "Professional oven and stove repair in Clovis, CA. Gas & electric. Warranty on parts and labor. Call (559) 765-0303.",
  "Oven &amp; Stove Repair in Clovis, CA",
  "When your oven or range isn't working properly, it disrupts your daily routine. We provide professional oven &amp; range repair in Clovis, helping restore safe, consistent performance with reliable in-home service.",
  "Common Oven &amp; Range Problems We Fix",
  ["Oven not heating or taking too long to preheat","Uneven cooking or inconsistent temperature","Burners not turning on or heating properly","Oven shutting off during use","Gas burners clicking or not igniting","Control panel or knobs not responding","Not heating to correct temperature"],
  "We service both electric and gas ovens and ranges. Instead of guessing, we identify exactly what's causing the issue. After that, we explain the problem clearly and complete the repair using quality parts to ensure lasting results.",
  WHY,
  "If your cooking appliance isn't performing like it should, call today to schedule oven &amp; range repair in Clovis.",
  ALSO)

service_page("stove-repair-clovis-ca",
  "Stove Repair Clovis, CA | Prime Appliance Repair",
  "Dependable stove repair in Clovis, CA. Gas & electric stoves. Warranty included. Call (559) 765-0303.",
  "Stove Repair in Clovis, CA",
  "A stove that doesn't heat properly or respond the way it should can make everyday cooking frustrating. We provide dependable stove repair in Clovis, with in-home service focused on restoring safe and reliable cooking performance.",
  "Common Stove Issues We Handle",
  ["Burners not heating or turning on","Uneven heat during cooking","Gas burners clicking or failing to ignite","Weak or inconsistent flame","Stove turning off unexpectedly","Control knobs or switches not responding","Temperature inaccurate"],
  "We service both gas and electric stoves. From ignition systems and heating elements to switches and internal wiring, proper diagnosis is essential. We identify the exact cause and complete the repair using reliable parts.",
  WHY,
  "If your stove isn't performing the way it should, call today to schedule stove repair in Clovis.",
  ALSO)

service_page("microwave-repair-clovis-ca",
  "Microwave Repair Clovis, CA | Prime Appliance Repair",
  "Fast microwave repair in Clovis, CA. In-home service, all brands. Warranty on parts and labor. Call (559) 765-0303.",
  "Microwave Repair in Clovis, CA",
  "A microwave is one of the most used appliances in the kitchen. We provide reliable microwave repair in Clovis, helping restore safe and efficient operation without the need for replacement.",
  "Common Microwave Problems We Fix",
  ["Microwave not heating","Runs but food stays cold","Turns on and off randomly","Sparks or unusual noises inside","Buttons or touchpad not responding","Microwave not turning on at all","Display not working"],
  "Every microwave repair starts with identifying the exact cause of the issue. Once confirmed, we explain the problem clearly and complete the repair using proper parts and safe procedures. This approach helps avoid unnecessary replacements and ensures long-term results.",
  WHY,
  "If your microwave is not working properly, call today to schedule microwave repair in Clovis.",
  ALSO)

service_page("freezer-repair-clovis-ca",
  "Freezer Repair Clovis, CA | Prime Appliance Repair",
  "Reliable freezer repair in Clovis, CA. Fast in-home service. Warranty on parts and labor. Call (559) 765-0303.",
  "Freezer Repair in Clovis, CA",
  "A freezer that isn't keeping the right temperature can lead to food loss and unnecessary stress. We provide reliable freezer repair in Clovis, with in-home service focused on restoring proper freezing performance.",
  "Signs Your Freezer Needs Repair",
  ["Food not staying fully frozen","Excessive frost or ice buildup","Freezer running constantly","Unusual noises during operation","Water leaking or ice melting inside","Temperature fluctuating"],
  "After a full inspection, we explain what's affecting your freezer and complete the repair using quality parts. Our goal is to restore stable temperature and reliable operation.",
  WHY,
  "If your freezer isn't performing as it should, call today to schedule freezer repair in Clovis.",
  ALSO)

service_page("wine-cooler-repair-clovis-ca",
  "Wine Cooler Repair Clovis, CA | Prime Appliance Repair",
  "Professional wine cooler repair in Clovis and Fresno. All brands. Warranty included. Call (559) 765-0303.",
  "Wine Cooler Repair in Clovis, CA",
  "We provide professional wine cooler repair for homeowners in Clovis and Fresno. Our skilled technicians diagnose and fix issues quickly and efficiently.",
  "Common Wine Cooler Problems",
  ["Not cooling properly","Temperature fluctuating","Unusual noises or vibrations","Unit not turning on","Condenser or compressor issues","Door seal problems"],
  "We start with a full diagnostic to identify the root cause of the problem. Once confirmed, we explain clearly and repair using quality parts with warranty coverage.",
  WHY,
  "Call today to schedule wine cooler repair or contact us directly to confirm we service your area.",
  ALSO)

service_page("ice-maker-repair-clovis-ca",
  "Ice Maker Repair Clovis, CA | Prime Appliance Repair",
  "Ice maker repair in Clovis and Fresno. In-home service, all brands. Call (559) 765-0303.",
  "Ice Maker Repair in Clovis, CA",
  "When your ice maker stops working, it's inconvenient. We provide reliable ice maker repair in Clovis and Fresno, getting your appliance back to producing ice quickly.",
  "Common Ice Maker Problems",
  ["Ice maker not producing ice","Ice cubes too small or hollow","Water dispenser not working","Ice tastes unusual","Unit making loud noises","Leaking water"],
  "We diagnose accurately and repair ice makers on all major brands using quality parts. Our goal is to restore proper ice production quickly and reliably.",
  WHY,
  "Call today to schedule ice maker repair in Clovis.",
  ALSO)

service_page("garbage-disposal-repair-clovis-ca",
  "Garbage Disposal Repair Clovis, CA | Prime Appliance Repair",
  "Fast garbage disposal repair in Clovis, CA. In-home service. Warranty on parts and labor. Call (559) 765-0303.",
  "Garbage Disposal Repair in Clovis, CA",
  "Fast disposal repairs to keep your kitchen sink functioning smoothly. We provide professional garbage disposal repair in Clovis with in-home service.",
  "Common Disposal Problems We Fix",
  ["Not turning on or humming","Jammed or stuck","Leaking water underneath","Making loud grinding noises","Not draining properly","Reset button keeps tripping","Foul odors coming from disposal"],
  "We begin with a full inspection to find the exact cause. Once diagnosed, we explain the problem clearly and complete the repair using reliable parts, ensuring your disposal works properly.",
  WHY,
  "Call today to schedule garbage disposal repair in Clovis.",
  ALSO)

print("\n✅ All service pages done")

# ════════════════════════════════════════════
# LOCATION PAGES
# ════════════════════════════════════════════
def loc_body(services, desc, why):
    svc_li = "".join(f"<li>{s}</li>" for s in services)
    why_li = "".join(f"<li>{w}</li>" for w in why)
    return f'''<p>{desc}</p>
<h2>Appliances We Repair</h2>
<ul>{svc_li}</ul>
<h2>Why Choose Us</h2>
<ul>{why_li}</ul>
<h2>Schedule Your Service</h2>
<p>Call today or schedule online for fast, reliable appliance repair. Same-day or next-day appointments available.</p>'''

SERVICES_LIST = ["Refrigerators &amp; freezers","Washers &amp; dryers","Ovens, ranges &amp; stoves","Dishwashers","Microwaves","Wine coolers &amp; ice makers"]

location_page("fresno-appliance-repair",
  "Appliance Repair Fresno | Prime Appliance Repair",
  "Fast, reliable appliance repair in Fresno. Licensed technicians, same-day or next-day service. Call (559) 765-0303.",
  "Appliance Repair Fresno",
  "Fast, reliable appliance repair in Fresno — licensed technicians, same-day or next-day service available.",
  loc_body(SERVICES_LIST,"Finding trustworthy appliance repair near Fresno shouldn't be complicated. Our goal is to make the process simple from the first call to the completed repair. We work directly at your home, arrive with the tools and parts needed for most common issues, and focus on identifying the real cause of the problem.",WHY))

location_page("fresno-ca-appliance-repair",
  "Fresno CA Appliance Repair | Prime Appliance Repair",
  "Professional appliance repair in Fresno, CA. All major brands. Warranty on parts & labor. Call (559) 765-0303.",
  "Fresno CA Appliance Repair",
  "Fast, reliable appliance repair in Fresno — licensed technicians, same-day or next-day service available.",
  loc_body(SERVICES_LIST,"We specialize in appliance repair in Fresno and surrounding areas, providing reliable service for all major household appliances. When you book our service, you can expect on-time arrival, clear communication, and a full diagnostic to identify the exact problem. We focus on accurate repairs instead of unnecessary part replacements.",WHY))

location_page("appliance-repair-near-fresno-ca-usa",
  "Appliance Repair Near Fresno CA | Prime Appliance Repair",
  "Looking for appliance repair near Fresno? Fast, professional in-home service. Call (559) 765-0303.",
  "Appliance Repair Near Fresno, CA",
  "Professional in-home appliance repair near Fresno, helping homeowners get their appliances back to normal without delays.",
  loc_body(SERVICES_LIST,"When a home appliance stops working, it's never convenient. Whether it's a refrigerator that won't cool, a washer that won't spin, or a dryer that takes forever to finish a cycle, you need a solution that's quick, honest, and done right the first time. We provide professional in-home appliance repair near Fresno.",WHY))

location_page("appliance-repair-near-me",
  "Appliance Repair Near Me | Prime Appliance Repair",
  "Local appliance repair near you in Fresno, Clovis & surrounding areas. Same-day service. Call (559) 765-0303.",
  "Appliance Repair Near Me",
  "Local, professional appliance repair in Fresno and surrounding areas — same-day or next-day service available.",
  loc_body(SERVICES_LIST,"We specialize in appliance repair in Fresno and surrounding areas. When you book our service, you can expect on-time arrival, clear communication, and a full diagnostic to identify the exact problem. We back our work with a warranty on both labor and parts.",WHY))

location_page("home-appliance-repair-fresno-ca",
  "Home Appliance Repair Fresno CA | Prime Appliance Repair",
  "Home appliance repair in Fresno, CA. All major brands and models. Warranty included. Call (559) 765-0303.",
  "Home Appliance Repair Fresno, CA",
  "Fast, stress-free home appliance repair in Fresno. Our technicians come fully prepared and treat your home with care.",
  loc_body(SERVICES_LIST,"We serve Fresno, Clovis, Madera, Friant, and nearby areas. Whether your fridge isn't cooling, your washer stopped spinning, or your oven won't heat up, we handle all major brands and models. We keep things easy, clear, and stress-free from start to finish.",WHY))

location_page("refrigerator-repair-fresno-ca",
  "Refrigerator Repair Fresno CA | Prime Appliance Repair",
  "Expert refrigerator repair in Fresno, CA. All brands, all models. Warranty on parts & labor. Call (559) 765-0303.",
  "Refrigerator Repair Fresno, CA",
  "Professional refrigerator repair in Fresno, CA. We service all types including top freezer, bottom freezer, side-by-side, and French door models.",
  f'''<p>If your refrigerator isn't cooling properly, making unusual noises, or leaking water, it may be time for professional service. We provide reliable refrigerator repair in Fresno, CA, helping restore proper cooling and performance quickly.</p>
<h2>Common Refrigerator Issues We Fix</h2>
<ul><li>Refrigerator not cooling or not cold enough</li><li>Temperature fluctuations</li><li>Faulty compressors</li><li>Defrost system failures</li><li>Ice maker or water dispenser problems</li><li>Water leaking inside or underneath</li></ul>
<h2>Why Choose Our Service</h2>
<ul>{"".join(f"<li>{w}</li>" for w in WHY)}</ul>
<p>For fast and dependable appliance repair in Fresno, we offer convenient scheduling with same-day or next-day appointments when available.</p>''')

location_page("dryer-repair-fresno-ca",
  "Dryer Repair Fresno CA | Prime Appliance Repair",
  "Fast dryer repair in Fresno, CA. All brands. Warranty on parts & labor. Call (559) 765-0303.",
  "Dryer Repair Fresno, CA",
  "Fast, friendly dryer repair in Fresno. Whether your dryer isn't heating, won't start, or is making strange noises, we fix it right.",
  f'''<p>Our dryer repair service is fast, friendly, and stress-free. We work on all major dryer brands and models, and every repair is completed using quality parts. All repairs are backed by a warranty on both parts and labor.</p>
<h2>Common Dryer Problems We Fix</h2>
<ul><li>Dryer not heating</li><li>Clothes taking too long to dry</li><li>Dryer stops mid-cycle</li><li>Loud noises or vibrations</li><li>Drum not spinning</li><li>Burning smell during use</li></ul>
<h2>Why Choose Our Service</h2>
<ul>{"".join(f"<li>{w}</li>" for w in WHY)}</ul>
<p>Give us a call or book your dryer repair online today — and get back to warm, dry laundry without the hassle.</p>''')

location_page("madera-appliance-repair",
  "Appliance Repair Madera | Prime Appliance Repair",
  "Reliable appliance repair in Madera. Fast in-home service, all major brands. Call (559) 765-0303.",
  "Appliance Repair Madera",
  "Reliable in-home appliance repair Madera homeowners can count on for fast, accurate, and long-lasting results.",
  loc_body(SERVICES_LIST,"At Prime Appliance Repair Services, we provide reliable in-home appliance repair in Madera. We service all major household appliances and focus on proper diagnostics first — so you're not paying for unnecessary parts or repeat visits. Whether it's a refrigerator not cooling, a washer not spinning, or an oven heating unevenly, we'll get it back to working condition.",WHY))

location_page("madera-refrigerator-repair",
  "Refrigerator Repair Madera | Prime Appliance Repair",
  "Reliable refrigerator repair in Madera. Fast in-home service, warranty included. Call (559) 765-0303.",
  "Refrigerator Repair in Madera",
  "Reliable refrigerator repair in Madera, offering in-home service to restore proper cooling and keep your appliance running efficiently.",
  f'''<p>A refrigerator that isn't cooling properly can quickly turn into a serious issue. From spoiled food to inconsistent temperatures, even small changes in performance shouldn't be ignored.</p>
<h2>Signs Your Refrigerator Needs Repair</h2>
<ul><li>Fridge not cold enough</li><li>Freezer working, but fridge is warm</li><li>Food spoiling faster than usual</li><li>Refrigerator running constantly</li><li>Water leaking inside or underneath</li><li>Unusual noises during operation</li></ul>
<h2>Why Choose Our Service</h2>
<ul>{"".join(f"<li>{w}</li>" for w in WHY)}</ul>
<p>Call today to schedule refrigerator repair in Madera or request service as part of your appliance repair in Madera needs.</p>''')

location_page("refrigerator-repair-madera-ca",
  "Refrigerator Repair Madera CA | Prime Appliance Repair",
  "Fast refrigerator repair in Madera, CA. All brands, all models. Warranty on parts & labor. Call (559) 765-0303.",
  "Refrigerator Repair Madera, CA",
  "Dependable refrigerator repair in Madera, CA, restoring proper performance and keeping your food fresh.",
  f'''<p>If your refrigerator isn't cooling properly, making unusual noises, or leaking water, it's time for professional help. We offer dependable refrigerator repair in Madera, CA, restoring proper performance and keeping your food fresh.</p>
<h2>What We Fix</h2>
<ul><li>Temperature issues</li><li>Faulty compressor</li><li>Defrost problems</li><li>Ice maker malfunctions</li><li>Water dispenser issues</li><li>All brands and models</li></ul>
<h2>Why Choose Our Service</h2>
<ul>{"".join(f"<li>{w}</li>" for w in WHY)}</ul>
<p>Schedule your refrigerator repair in Madera, CA today and get your appliance running like it should.</p>''')

location_page("sanger-appliance-repair",
  "Appliance Repair Sanger CA | Prime Appliance Repair",
  "Professional appliance repair in Sanger, CA. In-home service, all brands. Call (559) 765-0303.",
  "Appliance Repair in Sanger, CA",
  "Professional appliance repair in Sanger — in-home service designed to get your appliances back to normal quickly.",
  loc_body(SERVICES_LIST,"We provide professional appliance repair in Sanger, offering in-home service designed to get your appliances back to normal quickly and without unnecessary stress. Our approach is simple: we listen, inspect, and fix the issue based on what your appliance actually needs — not assumptions.",WHY))

location_page("clovis-appliance-repair",
  "Appliance Repair Clovis CA | Prime Appliance Repair",
  "Trusted appliance repair in Clovis, CA. All brands. Same-day service. Call (559) 765-0303.",
  "Appliance Repair Clovis, CA",
  "We show up with the right tools, the experience to get the job done, and friendly service you'll feel good about.",
  loc_body(SERVICES_LIST,"When an appliance breaks, it can throw your whole day off. We're here to make the fix feel easy. We proudly service Fresno, Clovis, Madera, and Friant — plus nearby areas. Whether your fridge isn't staying cold, your washer won't spin, or your oven won't heat, we work on all major brands and models.",WHY))

location_page("fowler-appliance-repair",
  "Appliance Repair Fowler CA | Prime Appliance Repair",
  "Fast appliance repair in Fowler, CA. Licensed technicians, same-day or next-day service. Call (559) 765-0303.",
  "Appliance Repair in Fowler, CA",
  "Fast, reliable appliance repair in Fowler — licensed technicians, same-day or next-day service available.",
  loc_body(SERVICES_LIST,"We provide fast, reliable appliance repair to homeowners in Fowler since 2009. Our licensed technicians diagnose and fix all major appliances with honest pricing and warranty on every repair.",WHY))

location_page("fraint-appliance-repair",
  "Appliance Repair Friant CA | Prime Appliance Repair",
  "Fast appliance repair in Friant, CA. Licensed technicians, same-day or next-day service. Call (559) 765-0303.",
  "Appliance Repair in Friant, CA",
  "Fast, reliable appliance repair in Friant — licensed technicians, same-day or next-day service available.",
  loc_body(SERVICES_LIST,"We provide fast, reliable appliance repair to homeowners in Friant since 2009. Our licensed technicians diagnose and fix all major appliances with honest pricing and warranty on every repair.",WHY))

location_page("bosch-appliance-repair-fresno",
  "Bosch Appliance Repair Fresno | Prime Appliance Repair",
  "Expert Bosch appliance repair in Fresno. Dishwashers, ovens, and more. Warranty included. Call (559) 765-0303.",
  "Bosch Appliance Repair Fresno",
  "Expert repair for Bosch appliances in Fresno, Clovis, Madera, and surrounding areas.",
  f'''<p>Bosch appliances are known for their quiet performance, efficiency, and sleek European design. They're built with precision and attention to detail, especially when it comes to dishwashers, ovens, and cooking appliances. Because of that, even small issues can require a careful and knowledgeable approach.</p>
<h2>Common Bosch Issues We Fix</h2>
<ul><li>Dishwashers not draining</li><li>Error codes</li><li>Heating issues</li><li>Units not starting</li><li>Control board problems</li></ul>
<h2>Why Choose Our Service</h2>
<ul>{"".join(f"<li>{w}</li>" for w in WHY)}</ul>
<p>We proudly service Fresno, Clovis, Madera, Friant, and surrounding areas. We keep everything clear, straightforward, and hassle-free.</p>''')

location_page("samsung-appliance-repair-fresno",
  "Samsung Appliance Repair Fresno | Prime Appliance Repair",
  "Samsung appliance repair in Fresno. Refrigerators, washers, dryers & more. Call (559) 765-0303.",
  "Samsung Appliance Repair Fresno",
  "Expert Samsung appliance repair in Fresno, Clovis, and surrounding areas.",
  f'''<p>Samsung appliances are known for their modern design and smart features. From refrigerators with digital displays to high-efficiency washers and dryers, these systems rely on both mechanical parts and advanced electronics.</p>
<h2>Common Samsung Issues We Fix</h2>
<ul><li>Cooling issues and temperature problems</li><li>Error codes</li><li>Drainage problems</li><li>Control board faults</li><li>Ice maker issues</li><li>Display problems</li></ul>
<h2>Why Choose Our Service</h2>
<ul>{"".join(f"<li>{w}</li>" for w in WHY)}</ul>
<p>We proudly service Fresno, Clovis, Madera, Friant, and nearby areas. You'll get clear communication, honest recommendations, and a repair process that's smooth from start to finish.</p>''')

location_page("viking-appliance-repair-fresno",
  "Viking Appliance Repair Fresno | Prime Appliance Repair",
  "Viking appliance repair in Fresno. Expert service for ranges, ovens, and cooktops. Call (559) 765-0303.",
  "Viking Appliance Repair Fresno",
  "Expert Viking appliance repair in Fresno and surrounding areas — professional-grade service for a premium brand.",
  f'''<p>Viking is a high-end brand that brought professional-style cooking into home kitchens. Their ranges, ovens, and cooktops are powerful, durable, and designed for serious performance — which means they need experienced hands when something goes wrong.</p>
<h2>Common Viking Issues We Fix</h2>
<ul><li>Burners not igniting</li><li>Ovens not heating evenly</li><li>Temperature inconsistencies</li><li>Control panel issues</li><li>Gas issues</li></ul>
<h2>Why Choose Our Service</h2>
<ul>{"".join(f"<li>{w}</li>" for w in WHY)}</ul>
<p>We service Fresno, Clovis, Madera, Friant, and surrounding areas with clear communication and reliable results.</p>''')

location_page("subzero-appliance-repair-fresno",
  "Sub-Zero Appliance Repair Fresno | Prime Appliance Repair",
  "Sub-Zero appliance repair in Fresno. Premium refrigerator & built-in kitchen repair. Call (559) 765-0303.",
  "Sub-Zero Appliance Repair Fresno",
  "Specialized Sub-Zero appliance repair in Fresno — premium brand expertise for lasting results.",
  f'''<p>Sub-Zero is a premium brand known for high-end refrigerators and built-in kitchen systems. Founded in 1945, Sub-Zero built its reputation on advanced cooling technology, dual refrigeration systems, and long-lasting quality. These appliances require the right knowledge and care when something goes wrong.</p>
<h2>Common Sub-Zero Issues We Fix</h2>
<ul><li>Temperature issues</li><li>Sealed system repairs</li><li>Built-in unit servicing</li><li>Condenser maintenance</li><li>Ice maker problems</li></ul>
<h2>Why Choose Our Service</h2>
<ul>{"".join(f"<li>{w}</li>" for w in WHY)}</ul>
<p>We keep everything clear, honest, and easy from start to finish. Your comfort comes first.</p>''')

print("✅ All location pages done")

