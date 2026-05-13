import os
BASE = "/home/user/webapp/static-site"

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
    <p>Don't wait — call now for same-day service or schedule your appointment online. We're here to help!</p>
    <div class="cta-banner-btns">
      <a href="tel:5597650303" class="btn-white">📞 (559) 765-0303</a>
      <a href="/book-an-appointment/" class="btn-accent">Book Appointment</a>
    </div>
  </div>
</section>'''

def write(path, html):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(html)
    print(f"✅ {path.replace(BASE,'')}")

# ════════════════════════════════════════════
# HOMEPAGE
# ════════════════════════════════════════════
homepage = head("Clovis Appliance Repair | (559) 765-0303 | Customer Favorite",
  "Clovis Appliance Repair — fast, reliable service for refrigerators, washers, dryers, ovens & more. Call (559) 765-0303 for same-day service.",
  "/") + HEADER + '''
<section class="hero">
  <div class="hero-inner">
    <div class="hero-content">
      <h1>Appliance Repair You Can Count On</h1>
      <p>Fast, professional service for all major appliances.<br>Serving Fresno, Clovis &amp; surrounding areas.</p>
      <div class="hero-btns">
        <a href="tel:5597650303" class="btn-white">📞 (559) 765-0303</a>
        <a href="/book-an-appointment/" class="btn-accent">Book Appointment</a>
      </div>
    </div>
  </div>
</section>

<!-- Brand logos strip -->
<section class="brands-strip">
  <div class="brands-inner">
    <div style="text-align:center;font-family:'Poppins',sans-serif;font-size:13px;font-weight:600;color:#555;">Whirlpool</div>
    <div style="text-align:center;font-family:'Poppins',sans-serif;font-size:13px;font-weight:600;color:#555;">Samsung</div>
    <div style="text-align:center;font-family:'Poppins',sans-serif;font-size:13px;font-weight:600;color:#555;">LG</div>
    <div style="text-align:center;font-family:'Poppins',sans-serif;font-size:13px;font-weight:600;color:#555;">GE</div>
    <div style="text-align:center;font-family:'Poppins',sans-serif;font-size:13px;font-weight:600;color:#555;">Maytag</div>
    <div style="text-align:center;font-family:'Poppins',sans-serif;font-size:13px;font-weight:600;color:#555;">Bosch</div>
    <div style="text-align:center;font-family:'Poppins',sans-serif;font-size:13px;font-weight:600;color:#555;">KitchenAid</div>
    <div style="text-align:center;font-family:'Poppins',sans-serif;font-size:13px;font-weight:600;color:#555;">Sub-Zero</div>
    <div style="text-align:center;font-family:'Poppins',sans-serif;font-size:13px;font-weight:600;color:#555;">Viking</div>
    <div style="text-align:center;font-family:'Poppins',sans-serif;font-size:13px;font-weight:600;color:#555;">Frigidaire</div>
  </div>
</section>

<!-- Services Grid -->
<section class="services-section">
  <div class="container">
    <h2 class="section-title">Appliance Repair Services</h2>
    <p class="section-subtitle">Professional repair for all major household appliances. Fast, reliable, with warranty on parts and labor.</p>
    <div class="services-grid">
      <a href="/refrigerator-repair-clovis-ca/" class="service-card">
        <div style="font-size:52px;">🧊</div>
        <h5>Refrigerator Repair</h5>
      </a>
      <a href="/washer-repair-clovis-ca/" class="service-card">
        <div style="font-size:52px;">🫧</div>
        <h5>Washer Repair</h5>
      </a>
      <a href="/dryer-repair-clovis-ca/" class="service-card">
        <div style="font-size:52px;">🌀</div>
        <h5>Dryer Repair</h5>
      </a>
      <a href="/dishwasher-repair-clovis-ca/" class="service-card">
        <div style="font-size:52px;">🍽️</div>
        <h5>Dishwasher Repair</h5>
      </a>
      <a href="/oven-repair-clovis-ca/" class="service-card">
        <div style="font-size:52px;">🔥</div>
        <h5>Oven &amp; Stove Repair</h5>
      </a>
      <a href="/microwave-repair-clovis-ca/" class="service-card">
        <div style="font-size:52px;">📡</div>
        <h5>Microwave Repair</h5>
      </a>
      <a href="/freezer-repair-clovis-ca/" class="service-card">
        <div style="font-size:52px;">❄️</div>
        <h5>Freezer Repair</h5>
      </a>
      <a href="/garbage-disposal-repair-clovis-ca/" class="service-card">
        <div style="font-size:52px;">⚙️</div>
        <h5>Garbage Disposal</h5>
      </a>
    </div>
  </div>
</section>

<!-- Why Choose Us -->
<section class="why-section">
  <div class="why-inner">
    <div class="why-left">
      <h2>Why Homeowners Trust Us</h2>
      <p>We've been working in appliance repair since 2009, starting small and growing steadily. What began as a local service has expanded into a trusted company serving homeowners across Fresno, Clovis, Madera, and surrounding areas.</p>
      <p>From day one, we've focused on being honest with our customers, responding quickly, doing quality work, and standing behind every job.</p>
      <div class="why-feature">
        <span style="font-size:26px;">🔍</span>
        <div class="why-feature-text">
          <h5>Free Diagnostics</h5>
          <p>We provide free, thorough diagnostics so you know exactly what's wrong and what it will cost to fix.</p>
        </div>
      </div>
      <div class="why-feature">
        <span style="font-size:26px;">💰</span>
        <div class="why-feature-text">
          <h5>Upfront Pricing</h5>
          <p>No surprises. You'll know the full cost before we start any work.</p>
        </div>
      </div>
      <div class="why-feature">
        <span style="font-size:26px;">🛡️</span>
        <div class="why-feature-text">
          <h5>Warranty on Every Repair</h5>
          <p>All repairs come with a warranty on parts and labor. If something goes wrong, we'll make it right.</p>
        </div>
      </div>
      <div class="why-feature">
        <span style="font-size:26px;">⚡</span>
        <div class="why-feature-text">
          <h5>Same-Day or Next-Day Service</h5>
          <p>We work around your schedule with convenient appointment times.</p>
        </div>
      </div>
      <div style="margin-top:28px;display:flex;gap:14px;flex-wrap:wrap;">
        <a href="tel:5597650303" class="btn-purple">📞 (559) 765-0303</a>
        <a href="/book-an-appointment/" class="btn-accent">Book Appointment</a>
      </div>
    </div>
    <div class="why-right">
      <div class="contact-box">
        <h4>Get Service Today</h4>
        <p style="font-size:15px;color:#848484;margin-bottom:10px;">Fill in your details and our team will contact you to confirm.</p>
        <div class="contact-field">📍 Your Address</div>
        <div class="contact-field">📞 Phone Number</div>
        <div class="contact-field">🔧 Appliance Type</div>
        <div class="contact-field">📝 Describe the Issue</div>
        <a href="/book-an-appointment/" class="btn-accent" style="width:100%;margin-top:6px;">
          Book Appointment Online
        </a>
      </div>
    </div>
  </div>
</section>

<!-- Features -->
<section class="features-row">
  <div class="container">
    <h2 class="section-title" style="text-align:center;">How We Work</h2>
    <div class="features-grid">
      <div class="feature-item">
        <div class="feature-icon">📋</div>
        <h4>Free Diagnostics</h4>
        <p>We provide free, thorough diagnostics so you know exactly what's wrong and what it will cost to fix.</p>
      </div>
      <div class="feature-item">
        <div class="feature-icon">💵</div>
        <h4>Upfront Pricing</h4>
        <p>No surprises. You'll know the full cost before we start any work. Our quotes are clear and comprehensive.</p>
      </div>
      <div class="feature-item">
        <div class="feature-icon">🛡️</div>
        <h4>Warranty</h4>
        <p>All repairs come with a warranty on parts and labor. If something goes wrong, we'll make it right.</p>
      </div>
      <div class="feature-item">
        <div class="feature-icon">🏷️</div>
        <h4>All Major Brands</h4>
        <p>We service all major appliance brands including Whirlpool, GE, Samsung, LG, Maytag, and many more.</p>
      </div>
      <div class="feature-item">
        <div class="feature-icon">✨</div>
        <h4>Clean &amp; Professional</h4>
        <p>Our technicians arrive in uniform, respect your home, and clean up completely after every job.</p>
      </div>
      <div class="feature-item">
        <div class="feature-icon">📅</div>
        <h4>Flexible Scheduling</h4>
        <p>We work around your schedule with convenient appointment times and same-day service when available.</p>
      </div>
    </div>
  </div>
</section>

<!-- Blog Section -->
<section class="blog-section">
  <div class="container">
    <h2 class="section-title">Recent Articles</h2>
    <p class="section-subtitle">Tips, guides, and news to help you keep your appliances running at their best.</p>
    <div class="blog-grid">
      <a href="/your-fridge-is-lying-to-you/" class="blog-card">
        <img src="https://appliancerepairclovis.com/wp-content/uploads/2026/04/vecteezy_woman-looking-disappointed-at-an-empty-fridge-feeling_69408907.jpg" alt="Your Fridge Is Lying to You" loading="lazy">
        <div class="blog-card-body">
          <span class="blog-cat">Appliance Problems &amp; Fixes</span>
          <p class="blog-meta">April 18, 2026 · 3 min read</p>
          <h4>Your Fridge Is Lying to You</h4>
          <p>It looks fine. The light turns on. It makes noise. It's cold… kind of. So you don't think about it much...</p>
          <span class="blog-read-more">Read More →</span>
        </div>
      </a>
      <a href="/appliance-repair-cost-guide/" class="blog-card">
        <img src="https://appliancerepairclovis.com/wp-content/uploads/2026/04/vecteezy_technician-or-worker-in-uniform-installs-dishwasher-into-the_35202703-1.jpg" alt="Appliance Repair Cost Guide" loading="lazy">
        <div class="blog-card-body">
          <span class="blog-cat">Repair Cost &amp; Guides</span>
          <p class="blog-meta">April 16, 2026 · 4 min read</p>
          <h4>Appliance Repair Cost Guide: What to Expect and How to Decide</h4>
          <p>One of the first questions people ask when an appliance breaks is simple: "How much does appliance repair cost?"</p>
          <span class="blog-read-more">Read More →</span>
        </div>
      </a>
      <a href="/when-everything-still-works-but-somethings-clearly-wrong/" class="blog-card">
        <img src="https://appliancerepairclovis.com/wp-content/uploads/2026/04/9652c7398ec0b54a986526ec323ce798.jpg" alt="When Everything Still Works" loading="lazy">
        <div class="blog-card-body">
          <span class="blog-cat">Appliance Problems &amp; Fixes</span>
          <p class="blog-meta">April 11, 2026 · 2 min read</p>
          <h4>When Everything "Still Works"... But Something's Clearly Wrong</h4>
          <p>There's a moment every homeowner hits. The appliance is technically still running, but something feels off...</p>
          <span class="blog-read-more">Read More →</span>
        </div>
      </a>
    </div>
  </div>
</section>

<!-- Area Section -->
<section class="area-section">
  <div class="container">
    <h3>Proudly Serving Fresno &amp; Surrounding Areas</h3>
    <p>We provide fast, reliable appliance repair services throughout Fresno, Clovis, Sanger, Fowler, Madera, Friant, and nearby communities. If you're not sure whether we service your area, give us a call!</p>
    <a href="tel:5597650303" class="btn-purple">📞 Call to Confirm Service Area</a>
  </div>
</section>
''' + CTA_BANNER + FOOTER

write(f"{BASE}/index.html", homepage)

# ════════════════════════════════════════════
# SERVICES PAGE
# ════════════════════════════════════════════
services_page = head("Appliance Repair Services | Prime Appliance Repair Clovis",
  "Professional appliance repair services in Clovis and Fresno. We repair refrigerators, washers, dryers, ovens, dishwashers & more. Call (559) 765-0303.",
  "/services/") + HEADER + '''
<section class="page-hero">
  <div class="container">
    <h1>Professional Appliance Repair for Every Home</h1>
    <p>We repair all major household appliances. Fast, reliable service with warranty on parts and labor. Same-day appointments available.</p>
    <div class="page-hero-btns">
      <a href="tel:5597650303" class="btn-white">📞 (559) 765-0303</a>
      <a href="/book-an-appointment/" class="btn-accent">Book Online</a>
    </div>
  </div>
</section>

<section class="services-page">
  <div class="container">
    <div class="service-card-lg">
      <div class="service-card-lg-icon">🧊</div>
      <div class="service-card-lg-body">
        <h3>Refrigerator Repair</h3>
        <p>Keep your food fresh and safe with professional refrigerator repair.</p>
        <ul>
          <li>Not cooling or freezing properly</li>
          <li>Water leaking inside or outside</li>
          <li>Ice maker not working</li>
          <li>Strange noises or vibrations</li>
          <li>Door seal issues</li>
          <li>Compressor problems</li>
          <li>Freezer frost buildup</li>
        </ul>
        <a href="/refrigerator-repair-clovis-ca/" class="btn-purple">Get Refrigerator Repair</a>
      </div>
    </div>
    <div class="service-card-lg">
      <div class="service-card-lg-icon">🫧</div>
      <div class="service-card-lg-body">
        <h3>Washer Repair</h3>
        <p>Get your laundry routine back on track with fast washer repairs.</p>
        <ul>
          <li>Won't spin or agitate</li>
          <li>Water not draining</li>
          <li>Leaking water on floor</li>
          <li>Won't start or power on</li>
          <li>Loud banging or grinding noise</li>
          <li>Not filling with water</li>
          <li>Shaking excessively during cycle</li>
        </ul>
        <a href="/washer-repair-clovis-ca/" class="btn-purple">Get Washer Repair</a>
      </div>
    </div>
    <div class="service-card-lg">
      <div class="service-card-lg-icon">🌀</div>
      <div class="service-card-lg-body">
        <h3>Dryer Repair</h3>
        <p>Efficient dryer repair to get your clothes dry and ready fast.</p>
        <ul>
          <li>Not heating or drying clothes</li>
          <li>Taking too long to dry</li>
          <li>Won't start or turn on</li>
          <li>Squeaking or thumping sounds</li>
          <li>Drum not turning</li>
          <li>Burning smell during use</li>
          <li>Door won't close properly</li>
        </ul>
        <a href="/dryer-repair-clovis-ca/" class="btn-purple">Get Dryer Repair</a>
      </div>
    </div>
    <div class="service-card-lg">
      <div class="service-card-lg-icon">🍽️</div>
      <div class="service-card-lg-body">
        <h3>Dishwasher Repair</h3>
        <p>Clean dishes every time with expert dishwasher repair service.</p>
        <ul>
          <li>Not cleaning dishes properly</li>
          <li>Water not draining</li>
          <li>Leaking water underneath</li>
          <li>Won't fill with water</li>
          <li>Not drying dishes</li>
          <li>Strange noises during wash</li>
          <li>Door latch broken</li>
        </ul>
        <a href="/dishwasher-repair-clovis-ca/" class="btn-purple">Get Dishwasher Repair</a>
      </div>
    </div>
    <div class="service-card-lg">
      <div class="service-card-lg-icon">🔥</div>
      <div class="service-card-lg-body">
        <h3>Oven &amp; Stove Repair</h3>
        <p>Get back to cooking with professional oven and stove repairs.</p>
        <ul>
          <li>Not heating or heating unevenly</li>
          <li>Burners not igniting</li>
          <li>Oven door won't close</li>
          <li>Temperature not accurate</li>
          <li>Self-cleaning cycle not working</li>
          <li>Gas smell or ignition issues</li>
          <li>Control panel errors</li>
        </ul>
        <a href="/oven-repair-clovis-ca/" class="btn-purple">Get Oven Repair</a>
      </div>
    </div>
    <div class="service-card-lg">
      <div class="service-card-lg-icon">📡</div>
      <div class="service-card-lg-body">
        <h3>Microwave Repair</h3>
        <p>Quick and safe microwave repairs for convenient meal prep.</p>
        <ul>
          <li>Not heating food</li>
          <li>Turntable not spinning</li>
          <li>Sparking inside</li>
          <li>Door not closing properly</li>
          <li>Control panel not responding</li>
          <li>Making loud humming noise</li>
          <li>Display not working</li>
        </ul>
        <a href="/microwave-repair-clovis-ca/" class="btn-purple">Get Microwave Repair</a>
      </div>
    </div>
    <div class="service-card-lg">
      <div class="service-card-lg-icon">⚙️</div>
      <div class="service-card-lg-body">
        <h3>Garbage Disposal Repair</h3>
        <p>Fast disposal repairs to keep your kitchen sink functioning smoothly.</p>
        <ul>
          <li>Not turning on or humming</li>
          <li>Jammed or stuck</li>
          <li>Leaking water underneath</li>
          <li>Making loud grinding noises</li>
          <li>Not draining properly</li>
          <li>Reset button keeps tripping</li>
          <li>Foul odors coming from disposal</li>
        </ul>
        <a href="/garbage-disposal-repair-clovis-ca/" class="btn-purple">Get Disposal Repair</a>
      </div>
    </div>
    <div class="service-card-lg">
      <div class="service-card-lg-icon">❄️</div>
      <div class="service-card-lg-body">
        <h3>Freezer Repair</h3>
        <p>Keep frozen food safe with reliable freezer repair services.</p>
        <ul>
          <li>Not freezing properly</li>
          <li>Excessive frost or ice buildup</li>
          <li>Temperature fluctuating</li>
          <li>Strange noises or sounds</li>
          <li>Door seal issues</li>
          <li>Compressor problems</li>
          <li>Water leaking inside or outside</li>
        </ul>
        <a href="/freezer-repair-clovis-ca/" class="btn-purple">Get Freezer Repair</a>
      </div>
    </div>
  </div>
</section>

<section class="features-row">
  <div class="container">
    <h2 class="section-title" style="text-align:center;margin-bottom:40px;">Why Choose Prime Appliance Repair?</h2>
    <div class="features-grid">
      <div class="feature-item"><div class="feature-icon">⚡</div><h4>Same-Day Service</h4><p>Need urgent repair? We offer same-day appointments so you're never without your appliances for long.</p></div>
      <div class="feature-item"><div class="feature-icon">🛡️</div><h4>Warranty</h4><p>All repairs backed by our comprehensive warranty on parts and labor for your peace of mind.</p></div>
      <div class="feature-item"><div class="feature-icon">🏆</div><h4>Certified Technicians</h4><p>Factory-trained and certified experts with years of experience repairing all major appliance brands.</p></div>
      <div class="feature-item"><div class="feature-icon">💵</div><h4>Upfront Pricing</h4><p>No surprises or hidden fees. You'll know the exact cost before we start any repair work.</p></div>
      <div class="feature-item"><div class="feature-icon">🔩</div><h4>Quality Parts</h4><p>We use only OEM and manufacturer-approved parts to ensure lasting repairs and optimal performance.</p></div>
      <div class="feature-item"><div class="feature-icon">🏡</div><h4>Local &amp; Trusted</h4><p>Proud to serve Fresno and surrounding areas with honest, reliable service our community depends on.</p></div>
    </div>
  </div>
</section>

<section class="area-section">
  <div class="container">
    <h3>Proudly Serving Fresno &amp; Surrounding Areas</h3>
    <p>We provide fast, reliable appliance repair services throughout Fresno, Clovis, Sanger, Fowler, and nearby communities. If you're not sure whether we service your area, give us a call!</p>
    <a href="tel:5597650303" class="btn-purple">📞 Call to Confirm Service Area</a>
  </div>
</section>
''' + CTA_BANNER + FOOTER

write(f"{BASE}/services/index.html", services_page)

# ════════════════════════════════════════════
# ABOUT US
# ════════════════════════════════════════════
about_page = head("About Us | Prime Appliance Repair Clovis",
  "Learn about Prime Appliance Repair Services — serving Fresno and Clovis since 2009. Expert, honest, reliable appliance repair.",
  "/about-us/") + HEADER + '''
<section class="page-hero">
  <div class="container">
    <h1>Expert Appliance Repair Services You Can Count On</h1>
    <p>Serving Fresno and surrounding areas with professional, reliable appliance repair since 2009. We're dedicated to keeping your home running smoothly.</p>
    <div style="display:flex;gap:32px;justify-content:center;flex-wrap:wrap;margin-top:28px;">
      <div style="text-align:center;"><div style="font-size:32px;font-weight:700;color:#cefe00;font-family:'Poppins',sans-serif;">50,000+</div><div style="font-size:14px;color:rgba(255,255,255,0.8);">Satisfied Customers</div></div>
      <div style="text-align:center;"><div style="font-size:32px;font-weight:700;color:#cefe00;font-family:'Poppins',sans-serif;">Same Day</div><div style="font-size:14px;color:rgba(255,255,255,0.8);">Service Available</div></div>
      <div style="text-align:center;"><div style="font-size:32px;font-weight:700;color:#cefe00;font-family:'Poppins',sans-serif;">100%</div><div style="font-size:14px;color:rgba(255,255,255,0.8);">Satisfaction Guarantee</div></div>
    </div>
  </div>
</section>

<section class="content-section">
  <div style="max-width:1120px;margin:0 auto;padding:70px 20px;">
    <div style="max-width:760px;margin:0 auto 60px;">
      <h2 style="font-family:'Poppins',sans-serif;font-size:36px;font-weight:400;color:#0b2936;margin-bottom:20px;">Built on Trust, Driven by Excellence</h2>
      <p style="font-size:17px;color:#404040;line-height:1.8;margin-bottom:16px;">We've been working in appliance repair since 2009, starting small and growing steadily over the years. What began as a local service has expanded into a trusted company serving homeowners across Fresno, Clovis, Madera, and surrounding areas. Most of our growth has come from word of mouth — customers who appreciate honest service and reliable results.</p>
      <p style="font-size:17px;color:#404040;line-height:1.8;margin-bottom:16px;">From day one, we've focused on a few simple things: being honest with our customers, responding quickly, doing quality work, and standing behind every job. We believe repairs should be done right the first time, with clear communication and no unnecessary upselling.</p>
      <p style="font-size:17px;color:#404040;line-height:1.8;">Today, we handle a full range of services, including appliance repair, installation, and routine maintenance. When you choose us, you're not just getting a repair service — you're working with a team that genuinely cares about keeping your home running smoothly.</p>
    </div>

    <div class="features-grid">
      <div class="feature-item"><div class="feature-icon">🤝</div><h4>Honest &amp; Transparent</h4><p>No hidden fees, no surprises. We provide upfront pricing and clear explanations for every repair recommendation.</p></div>
      <div class="feature-item"><div class="feature-icon">⚡</div><h4>Fast &amp; Reliable</h4><p>Same-day or next-day service available. We arrive on time, work efficiently, and get your appliances back in working order quickly.</p></div>
      <div class="feature-item"><div class="feature-icon">🏆</div><h4>Certified Experts</h4><p>Our technicians are factory-trained and certified to repair all major appliance brands with precision and care.</p></div>
      <div class="feature-item"><div class="feature-icon">❤️</div><h4>Customer Focused</h4><p>Your satisfaction is our priority. We listen, we care, and we go the extra mile to ensure you're completely happy.</p></div>
      <div class="feature-item"><div class="feature-icon">🔩</div><h4>Quality Parts</h4><p>We use only high-quality OEM and manufacturer-approved parts backed by our comprehensive warranty.</p></div>
      <div class="feature-item"><div class="feature-icon">🏡</div><h4>Local &amp; Trusted</h4><p>We're your neighbors in Fresno. Supporting local businesses and building lasting relationships with our community.</p></div>
    </div>

    <div style="margin-top:70px;">
      <h2 style="font-family:'Poppins',sans-serif;font-size:36px;font-weight:400;color:#0b2936;text-align:center;margin-bottom:40px;">Our Process</h2>
      <div class="about-steps">
        <div class="about-step"><div class="step-num">01</div><div class="step-body"><h5>Free Diagnostics</h5><p>We provide free, thorough diagnostics so you know exactly what's wrong and what it will cost to fix.</p></div></div>
        <div class="about-step"><div class="step-num">02</div><div class="step-body"><h5>Upfront Pricing</h5><p>No surprises. You'll know the full cost before we start any work. Our quotes are clear and comprehensive.</p></div></div>
        <div class="about-step"><div class="step-num">03</div><div class="step-body"><h5>Warranty</h5><p>All repairs come with a warranty on parts and labor. If something goes wrong, we'll make it right.</p></div></div>
        <div class="about-step"><div class="step-num">04</div><div class="step-body"><h5>All Major Brands</h5><p>We service all major appliance brands including Whirlpool, GE, Samsung, LG, Maytag, and many more.</p></div></div>
        <div class="about-step"><div class="step-num">05</div><div class="step-body"><h5>Clean &amp; Professional</h5><p>Our technicians arrive in uniform, respect your home, and clean up completely after every job.</p></div></div>
        <div class="about-step"><div class="step-num">06</div><div class="step-body"><h5>Flexible Scheduling</h5><p>We work around your schedule with convenient appointment times and same-day service when available.</p></div></div>
      </div>
    </div>
  </div>
</section>
''' + CTA_BANNER + FOOTER

write(f"{BASE}/about-us/index.html", about_page)

# ════════════════════════════════════════════
# CONTACT US
# ════════════════════════════════════════════
contact_page = head("Contact Us | Prime Appliance Repair Clovis",
  "Contact Prime Appliance Repair Services. Call (559) 765-0303 or book online. Serving Fresno, Clovis & surrounding areas.",
  "/contact-us/") + HEADER + '''
<section class="page-hero">
  <div class="container">
    <h1>Contact Us</h1>
    <p>Where broken appliances meet their match, and your peace of mind is just a service call away!</p>
    <div class="page-hero-btns" style="margin-top:20px;">
      <a href="tel:5597650303" class="btn-white">📞 (559) 765-0303</a>
      <a href="/book-an-appointment/" class="btn-accent">Book Appointment</a>
    </div>
  </div>
</section>

<section style="padding:70px 0;">
  <div style="max-width:1120px;margin:0 auto;padding:0 20px;">
    <div class="contact-grid">
      <div class="contact-info">
        <h3>Get In Touch</h3>
        <p style="font-size:16px;color:#848484;margin-bottom:28px;">We service Fresno, Clovis, and surrounding areas. We work with all major appliance brands and models, and we're here to make the repair process smooth, stress-free, and even a little enjoyable.</p>
        <div class="contact-info-item">
          <span class="icon">📞</span>
          <div><h5>Phone</h5><a href="tel:5597650303">(559) 765-0303</a></div>
        </div>
        <div class="contact-info-item">
          <span class="icon">✉️</span>
          <div><h5>Email</h5><a href="mailto:appliancerepairserviceus@gmail.com">appliancerepairserviceus@gmail.com</a></div>
        </div>
        <div class="contact-info-item">
          <span class="icon">📍</span>
          <div><h5>Service Area</h5><p>Fresno, Clovis, Madera, Sanger, Fowler, Friant &amp; surrounding areas</p></div>
        </div>
        <div class="contact-info-item">
          <span class="icon">🕐</span>
          <div><h5>Hours</h5><p>Monday – Saturday: 8am – 6pm<br>Sunday: By appointment</p></div>
        </div>
      </div>
      <div class="contact-form">
        <h3>Send Us a Message</h3>
        <form action="/book-an-appointment/" method="get">
          <div class="form-row">
            <div class="form-group"><label>First Name</label><input type="text" placeholder="John"></div>
            <div class="form-group"><label>Last Name</label><input type="text" placeholder="Smith"></div>
          </div>
          <div class="form-group"><label>Phone Number</label><input type="tel" placeholder="(559) 000-0000"></div>
          <div class="form-group"><label>Email</label><input type="email" placeholder="john@email.com"></div>
          <div class="form-group"><label>Appliance Type</label>
            <select>
              <option>Select appliance...</option>
              <option>Refrigerator</option><option>Washer</option><option>Dryer</option>
              <option>Dishwasher</option><option>Oven / Stove</option><option>Microwave</option>
              <option>Freezer</option><option>Other</option>
            </select>
          </div>
          <div class="form-group"><label>Describe the Issue</label><textarea placeholder="Tell us what's happening with your appliance..."></textarea></div>
          <button type="submit" class="btn-accent" style="width:100%;border:none;cursor:pointer;font-size:16px;">Send Message</button>
        </form>
      </div>
    </div>
  </div>
</section>

<section class="brands-section">
  <div class="container">
    <h3>Appliance Brands We Service</h3>
    <p>Here is a comprehensive list of appliance brands that we service regularly. If you don't see your brand listed, feel free to contact us directly.</p>
    <div class="brands-grid">
      <div class="brand-item">Whirlpool</div><div class="brand-item">Samsung</div><div class="brand-item">LG</div>
      <div class="brand-item">GE</div><div class="brand-item">Maytag</div><div class="brand-item">Bosch</div>
      <div class="brand-item">KitchenAid</div><div class="brand-item">Frigidaire</div><div class="brand-item">Sub-Zero</div>
      <div class="brand-item">Viking</div><div class="brand-item">Thermador</div><div class="brand-item">Electrolux</div>
      <div class="brand-item">Kenmore</div><div class="brand-item">Amana</div><div class="brand-item">Miele</div>
    </div>
  </div>
</section>
''' + CTA_BANNER + FOOTER

write(f"{BASE}/contact-us/index.html", contact_page)

# ════════════════════════════════════════════
# BOOK AN APPOINTMENT
# ════════════════════════════════════════════
book_page = head("Book an Appointment | Prime Appliance Repair Clovis",
  "Book your appliance repair appointment online. Quick and easy — fill in your details and we'll confirm same-day. Call (559) 765-0303.",
  "/book-an-appointment/") + HEADER + '''
<section class="page-hero">
  <div class="container">
    <h1>Book an Appointment Online</h1>
    <p>Quick and easy — fill in your details and our team will contact you as soon as possible to confirm.</p>
  </div>
</section>
<section class="book-section">
  <div class="book-inner">
    <div class="book-form">
      <h2>Schedule Your Repair</h2>
      <p>Fill out the form below and we'll reach out to confirm your appointment time.</p>
      <form>
        <div class="form-row">
          <div class="form-group"><label>First Name *</label><input type="text" placeholder="John" required></div>
          <div class="form-group"><label>Last Name *</label><input type="text" placeholder="Smith" required></div>
        </div>
        <div class="form-group"><label>Phone Number *</label><input type="tel" placeholder="(559) 000-0000" required></div>
        <div class="form-group"><label>Email Address</label><input type="email" placeholder="john@email.com"></div>
        <div class="form-group"><label>Service Address *</label><input type="text" placeholder="123 Main St, Clovis, CA" required></div>
        <div class="form-group"><label>Appliance Type *</label>
          <select required>
            <option value="">Select appliance...</option>
            <option>Refrigerator</option><option>Washer</option><option>Dryer</option>
            <option>Dishwasher</option><option>Oven / Stove</option><option>Microwave</option>
            <option>Freezer</option><option>Wine Cooler</option><option>Ice Maker</option>
            <option>Garbage Disposal</option><option>Other</option>
          </select>
        </div>
        <div class="form-group"><label>Appliance Brand</label><input type="text" placeholder="e.g. Samsung, Whirlpool, LG..."></div>
        <div class="form-group"><label>Preferred Date</label><input type="date"></div>
        <div class="form-group"><label>Describe the Problem *</label><textarea placeholder="Tell us what's happening with your appliance..." required></textarea></div>
        <button type="submit" class="btn-accent" style="width:100%;border:none;cursor:pointer;font-size:16px;padding:14px;">Book Appointment</button>
      </form>
      <p style="font-size:13px;color:#848484;text-align:center;margin-top:14px;">Or call us directly: <a href="tel:5597650303" style="color:#4831B0;font-weight:600;">(559) 765-0303</a></p>
    </div>
  </div>
</section>
''' + CTA_BANNER + FOOTER

write(f"{BASE}/book-an-appointment/index.html", book_page)
# Also create /book-appointment/ redirect
import shutil
os.makedirs(f"{BASE}/book-appointment", exist_ok=True)
shutil.copy(f"{BASE}/book-an-appointment/index.html", f"{BASE}/book-appointment/index.html")
print("✅ /book-appointment/ (copy)")

# ════════════════════════════════════════════
# PRIVACY POLICY
# ════════════════════════════════════════════
privacy_page = head("Privacy Policy | Prime Appliance Repair",
  "Privacy Policy for Prime Appliance Repair Services.",
  "/privacy-policy/") + HEADER + '''
<section class="page-hero">
  <div class="container"><h1>Privacy Policy</h1></div>
</section>
<section style="padding:70px 0;">
  <div style="max-width:800px;margin:0 auto;padding:0 20px;">
    <p style="color:#848484;margin-bottom:24px;">Last updated: January 1, 2026</p>
    <h2 style="font-family:'Poppins',sans-serif;font-size:24px;color:#0b2936;margin:28px 0 12px;">Information We Collect</h2>
    <p style="font-size:16px;color:#404040;line-height:1.8;">We collect information you provide directly to us, such as your name, phone number, email address, and service address when you book an appointment or contact us.</p>
    <h2 style="font-family:'Poppins',sans-serif;font-size:24px;color:#0b2936;margin:28px 0 12px;">How We Use Your Information</h2>
    <p style="font-size:16px;color:#404040;line-height:1.8;">We use the information we collect to schedule and provide appliance repair services, communicate with you about your appointment, and improve our services.</p>
    <h2 style="font-family:'Poppins',sans-serif;font-size:24px;color:#0b2936;margin:28px 0 12px;">Information Sharing</h2>
    <p style="font-size:16px;color:#404040;line-height:1.8;">We do not sell, trade, or otherwise transfer your personal information to third parties without your consent, except as required by law.</p>
    <h2 style="font-family:'Poppins',sans-serif;font-size:24px;color:#0b2936;margin:28px 0 12px;">Contact Us</h2>
    <p style="font-size:16px;color:#404040;line-height:1.8;">If you have questions about this Privacy Policy, please contact us at <a href="tel:5597650303" style="color:#4831B0;">(559) 765-0303</a> or <a href="mailto:appliancerepairserviceus@gmail.com" style="color:#4831B0;">appliancerepairserviceus@gmail.com</a>.</p>
  </div>
</section>
''' + FOOTER

write(f"{BASE}/privacy-policy/index.html", privacy_page)

# ════════════════════════════════════════════
# BLOG INDEX
# ════════════════════════════════════════════
blog_page = head("Blog | Prime Appliance Repair Clovis",
  "Tips, guides, and news to help you keep your appliances running at their best. From Prime Appliance Repair Services.",
  "/blog-2/") + HEADER + '''
<section class="page-hero">
  <div class="container">
    <h1>Our Blog</h1>
    <p>Tips, guides, and news to help you keep your appliances running at their best.</p>
  </div>
</section>
<section style="padding:70px 0;">
  <div style="max-width:1120px;margin:0 auto;padding:0 20px;">
    <div style="display:flex;gap:16px;flex-wrap:wrap;margin-bottom:36px;">
      <a href="/blog-2/" style="display:inline-block;padding:8px 20px;background:#4831B0;color:#fff;border-radius:20px;font-size:14px;font-weight:600;">All Posts</a>
      <a href="/category/appliance-problems-fixes/" style="display:inline-block;padding:8px 20px;background:#f5f5f5;color:#404040;border-radius:20px;font-size:14px;">Appliance Problems &amp; Fixes</a>
      <a href="/category/repair-cost-guides/" style="display:inline-block;padding:8px 20px;background:#f5f5f5;color:#404040;border-radius:20px;font-size:14px;">Repair Cost Guides</a>
      <a href="/category/maintenance-insider-tips/" style="display:inline-block;padding:8px 20px;background:#f5f5f5;color:#404040;border-radius:20px;font-size:14px;">Maintenance &amp; Tips</a>
    </div>
    <div class="blog-page-grid">
      <a href="/your-fridge-is-lying-to-you/" class="blog-list-card">
        <img src="https://appliancerepairclovis.com/wp-content/uploads/2026/04/vecteezy_woman-looking-disappointed-at-an-empty-fridge-feeling_69408907.jpg" alt="Your Fridge Is Lying to You" loading="lazy">
        <div class="blog-list-card-body">
          <span class="blog-cat">Appliance Problems &amp; Fixes</span>
          <h3>Your Fridge Is Lying to You</h3>
          <p style="font-size:13px;color:#848484;margin-bottom:8px;">April 18, 2026 · 3 min read</p>
          <p>It looks fine. The light turns on. It makes noise. It's cold… kind of. So you don't think about it much — until you do.</p>
          <span class="read-more">Read More →</span>
        </div>
      </a>
      <a href="/appliance-repair-cost-guide/" class="blog-list-card">
        <img src="https://appliancerepairclovis.com/wp-content/uploads/2026/04/vecteezy_technician-or-worker-in-uniform-installs-dishwasher-into-the_35202703-1.jpg" alt="Appliance Repair Cost Guide" loading="lazy">
        <div class="blog-list-card-body">
          <span class="blog-cat">Repair Cost &amp; Guides</span>
          <h3>Appliance Repair Cost Guide: What to Expect and How to Decide</h3>
          <p style="font-size:13px;color:#848484;margin-bottom:8px;">April 16, 2026 · 4 min read</p>
          <p>One of the first questions people ask when an appliance breaks is: "How much does appliance repair cost?" Here's the honest answer.</p>
          <span class="read-more">Read More →</span>
        </div>
      </a>
      <a href="/when-everything-still-works-but-somethings-clearly-wrong/" class="blog-list-card">
        <img src="https://appliancerepairclovis.com/wp-content/uploads/2026/04/9652c7398ec0b54a986526ec323ce798.jpg" alt="When Everything Still Works" loading="lazy">
        <div class="blog-list-card-body">
          <span class="blog-cat">Appliance Problems &amp; Fixes</span>
          <h3>When Everything "Still Works"... But Something's Clearly Wrong</h3>
          <p style="font-size:13px;color:#848484;margin-bottom:8px;">April 11, 2026 · 2 min read</p>
          <p>There's a moment every homeowner hits. The appliance is technically still running, but something's clearly off.</p>
          <span class="read-more">Read More →</span>
        </div>
      </a>
      <a href="/why-your-dryer-takes-too-long-to-dry-clothes/" class="blog-list-card">
        <img src="https://appliancerepairclovis.com/wp-content/uploads/2026/04/WhatsApp-Image-2026-02-24-at-23.54.01.jpeg" alt="Why Your Dryer Takes Too Long" loading="lazy">
        <div class="blog-list-card-body">
          <span class="blog-cat">Maintenance &amp; Insider Tips</span>
          <h3>Why Your Dryer Takes Too Long to Dry Clothes</h3>
          <p style="font-size:13px;color:#848484;margin-bottom:8px;">April 11, 2026 · 3 min read</p>
          <p>If your dryer is running full cycles but clothes still come out damp, something isn't working the way it should.</p>
          <span class="read-more">Read More →</span>
        </div>
      </a>
      <a href="/washer-maintenance-tips-most-people-ignore/" class="blog-list-card">
        <img src="https://appliancerepairclovis.com/wp-content/uploads/2026/04/WhatsApp-Image-2026-03-21-at-22.45.04-2.jpeg" alt="Washer Maintenance Tips" loading="lazy">
        <div class="blog-list-card-body">
          <span class="blog-cat">Maintenance &amp; Insider Tips</span>
          <h3>Washer Maintenance Tips Most People Ignore</h3>
          <p style="font-size:13px;color:#848484;margin-bottom:8px;">April 11, 2026 · 3 min read</p>
          <p>Most people don't think about maintaining their washer until something goes wrong. Here are the tips that keep it running longer.</p>
          <span class="read-more">Read More →</span>
        </div>
      </a>
      <a href="/repair-vs-replace/" class="blog-list-card">
        <img src="https://appliancerepairclovis.com/wp-content/uploads/2026/04/vecteezy_set-of-tools-for-repair-in-a-case-on-a-white-background_22837730.jpg" alt="Repair vs Replace" loading="lazy">
        <div class="blog-list-card-body">
          <span class="blog-cat">Repair Cost &amp; Guides</span>
          <h3>Repair vs Replace: How to Decide What's Right for Your Appliance</h3>
          <p style="font-size:13px;color:#848484;margin-bottom:8px;">April 11, 2026 · 4 min read</p>
          <p>One of the hardest decisions homeowners face: should you repair the appliance or just replace it?</p>
          <span class="read-more">Read More →</span>
        </div>
      </a>
    </div>
  </div>
</section>
''' + CTA_BANNER + FOOTER

write(f"{BASE}/blog-2/index.html", blog_page)

print("\n✅ Main pages done!")
