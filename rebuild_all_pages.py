#!/usr/bin/env python3
"""
rebuild_all_pages.py
Rebuilds every non-homepage HTML file under docs/ to match the
Prime Appliance Repair design system (Inter font, #2b3340 dark,
#d4f000 accent, rounded navbar, dark footer, consistent inner-page
hero, etc.).

Run from /home/user/webapp:
    python3 rebuild_all_pages.py
"""

import os, textwrap

BASE   = "/home/user/webapp/docs"
PHONE  = "(559) 765-0303"
PHONE_RAW = "+15597650303"
EMAIL  = "appliancerepairserviceus@gmail.com"
LOGO   = "https://appliancerepairclovis.com/wp-content/uploads/2026/04/primelogo1.png"
FAVICON= "https://appliancerepairclovis.com/wp-content/uploads/2022/10/appliance-repair.png"
GFONT  = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">'

# ─────────────────────────────────────────────
# SHARED CSS (all inner pages)
# ─────────────────────────────────────────────
SHARED_CSS = """
*,*::before,*::after{box-sizing:border-box;}
html,body{margin:0;padding:0;overflow-x:hidden;scroll-behavior:smooth;}
body{font-family:'Inter','Segoe UI',sans-serif;background:#fafbfc;color:#5a6472;}

/* ── NAVBAR ── */
.site-navbar{
  position:fixed;top:0;left:50%;transform:translateX(-50%);
  width:calc(100% - 64px);max-width:1100px;z-index:1000;
  background:rgba(43,51,64,0.92);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);
  border-radius:16px;margin-top:12px;overflow:visible;
  transition:background .3s,box-shadow .3s,border-radius .3s,margin-top .3s;
}
.site-navbar.scrolled{
  background:rgba(43,51,64,0.99);box-shadow:0 4px 20px rgba(0,0,0,.15);
  border-radius:0 0 16px 16px;margin-top:0;
}
.nav-inner{padding:14px 32px;display:flex;align-items:center;justify-content:space-between;gap:32px;}
.nav-logo a{display:block;text-decoration:none;}
.nav-logo img{height:48px;width:auto;object-fit:contain;display:block;}
.nav-toggle{display:none;flex-direction:column;gap:5px;background:transparent;border:none;cursor:pointer;padding:8px;flex-shrink:0;z-index:10;}
.nav-toggle span{display:block;width:24px;height:2px;background:#fff;border-radius:2px;transition:transform .28s,opacity .28s;}
.nav-toggle[aria-expanded="true"] span:nth-child(1){transform:rotate(45deg) translate(5px,5px);}
.nav-toggle[aria-expanded="true"] span:nth-child(2){opacity:0;}
.nav-toggle[aria-expanded="true"] span:nth-child(3){transform:rotate(-45deg) translate(5px,-5px);}
.nav-menu{display:flex;align-items:center;gap:36px;list-style:none;margin:0;padding:0;flex:1;justify-content:center;}
.nav-menu>li{position:relative;}
.nav-menu>li>a{display:flex;align-items:center;gap:6px;color:rgba(255,255,255,.9);text-decoration:none;font-size:14px;font-weight:600;padding:8px 0;white-space:nowrap;transition:color .2s;}
.nav-menu>li>a:hover,.nav-menu>li.active>a{color:#d4f000;}
.drop-icon{width:13px;height:13px;stroke:currentColor;fill:none;stroke-width:2.5;flex-shrink:0;transition:transform .25s;}
.has-drop:hover .drop-icon{transform:rotate(180deg);}
.drop-menu{
  position:absolute;top:calc(100% + 4px);left:50%;
  transform:translateX(-50%) translateY(-6px);
  background:rgba(36,43,54,.99);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);
  border-radius:12px;padding:10px 0;min-width:210px;list-style:none;margin:0;
  box-shadow:0 8px 32px rgba(0,0,0,.30);
  opacity:0;visibility:hidden;pointer-events:none;
  transition:opacity .28s,transform .28s,visibility .28s;z-index:200;
}
.drop-menu::before{content:'';position:absolute;top:-6px;left:50%;transform:translateX(-50%);border-left:8px solid transparent;border-right:8px solid transparent;border-bottom:6px solid rgba(36,43,54,.99);}
.has-drop::after{content:'';position:absolute;top:100%;left:-24px;right:-24px;height:18px;background:transparent;pointer-events:auto;}
.has-drop:hover .drop-menu{opacity:1;visibility:visible;transform:translateX(-50%) translateY(0);pointer-events:auto;}
.drop-menu li{margin:0;padding:0;}
.drop-menu a{display:block;color:rgba(255,255,255,.85);text-decoration:none;font-size:13px;font-weight:500;padding:10px 22px;white-space:nowrap;transition:background .15s,color .15s,padding-left .18s;}
.drop-menu a:hover{background:rgba(212,240,0,.10);color:#d4f000;padding-left:28px;}
.nav-cta{background:#d4f000!important;color:#1e2432!important;font-weight:700!important;padding:9px 20px!important;border-radius:8px!important;transition:background .2s,transform .2s!important;}
.nav-cta:hover{background:#c5e000!important;color:#1e2432!important;transform:translateY(-1px);}

/* ── INNER PAGE HERO ── */
.inner-hero{
  background:linear-gradient(135deg,#1e2432 0%,#2b3340 60%,#3a4555 100%);
  padding:130px 32px 80px;
  display:flex;justify-content:center;
}
.inner-hero-inner{max-width:1100px;width:100%;}
.inner-hero-badge{
  display:inline-flex;align-items:center;gap:8px;
  background:rgba(212,240,0,.15);border:1px solid rgba(212,240,0,.35);
  border-radius:50px;padding:6px 14px 6px 8px;margin-bottom:20px;
}
.inner-hero-badge-dot{width:8px;height:8px;border-radius:50%;background:#d4f000;animation:pulse 2s infinite;}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1);}50%{opacity:.5;transform:scale(1.3);}}
.inner-hero-badge span{font-size:12px;font-weight:600;color:#d4f000;letter-spacing:1px;text-transform:uppercase;}
.inner-hero h1{font-size:clamp(28px,4vw,52px);font-weight:900;color:#fff;line-height:1.15;margin:0 0 18px;letter-spacing:-.3px;max-width:700px;}
.inner-hero h1 .hi{color:#d4f000;}
.inner-hero p{font-size:clamp(14px,1.5vw,17px);color:rgba(255,255,255,.80);line-height:1.7;max-width:580px;margin:0 0 32px;}
.inner-hero-btns{display:flex;flex-wrap:wrap;gap:14px;align-items:center;}
.btn-hero-primary{display:inline-flex;align-items:center;gap:8px;background:#d4f000;color:#1e2432;font-size:15px;font-weight:700;padding:13px 26px;border-radius:8px;text-decoration:none;border:2px solid #d4f000;transition:background .2s,transform .2s,box-shadow .2s;}
.btn-hero-primary:hover{background:#c5e000;border-color:#c5e000;transform:translateY(-2px);box-shadow:0 8px 24px rgba(212,240,0,.35);}
.btn-hero-primary svg{width:15px;height:15px;stroke:#1e2432;fill:none;stroke-width:2.5;}
.btn-hero-secondary{display:inline-flex;align-items:center;gap:8px;background:transparent;color:#fff;font-size:15px;font-weight:600;padding:13px 26px;border-radius:8px;text-decoration:none;border:2px solid rgba(255,255,255,.5);transition:border-color .2s,background .2s,transform .2s;}
.btn-hero-secondary:hover{border-color:#fff;background:rgba(255,255,255,.10);transform:translateY(-2px);}
.btn-hero-secondary svg{width:15px;height:15px;stroke:#fff;fill:none;stroke-width:2.5;}
.inner-hero-trust{display:flex;align-items:center;gap:20px;flex-wrap:wrap;margin-top:32px;padding-top:24px;border-top:1px solid rgba(255,255,255,.12);}
.trust-chip{display:flex;align-items:center;gap:7px;}
.trust-chip svg{width:15px;height:15px;stroke:#d4f000;fill:none;stroke-width:2.2;flex-shrink:0;}
.trust-chip span{font-size:13px;color:rgba(255,255,255,.75);font-weight:500;}

/* ── BREADCRUMB ── */
.breadcrumb-bar{background:#fff;border-bottom:1px solid #e5e7eb;padding:10px 32px;}
.breadcrumb-inner{max-width:1100px;margin:0 auto;display:flex;align-items:center;gap:6px;flex-wrap:wrap;}
.breadcrumb-inner a,.breadcrumb-inner span{font-size:12px;color:#6b7280;text-decoration:none;}
.breadcrumb-inner a:hover{color:#2b3340;}
.breadcrumb-inner .sep{color:#d1d5db;}
.breadcrumb-inner .cur{color:#2b3340;font-weight:600;}

/* ── SECTION WRAPPERS ── */
.section-outer{display:flex;justify-content:center;padding:48px 32px;}
.section-outer.section-outer--plain{padding:0 32px;}
.section-box{
  max-width:1100px;width:100%;padding:64px 56px;
  background:linear-gradient(160deg,#f0f3f6 0%,#e8ecf0 50%,#eef1f5 100%);
  border-radius:20px;box-shadow:0 4px 32px rgba(68,81,98,.08);
}
.section-badge{display:inline-flex;align-items:center;gap:8px;background:#dce1e7;color:#445162;font-size:11px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;padding:6px 14px;border-radius:50px;margin-bottom:14px;}
.section-badge svg{width:12px;height:12px;stroke:#445162;fill:none;stroke-width:2.5;}
.section-title{font-size:clamp(26px,3.5vw,40px);font-weight:900;color:#2b3340;line-height:1.15;margin:0 0 14px;}
.section-sub{font-size:15px;color:#5a6472;line-height:1.7;max-width:640px;margin:0;}

/* ── CONTENT + SIDEBAR LAYOUT ── */
/* content-wrap is always wrapped in .section-outer > .section-box for consistent gutter */
.content-wrap{width:100%;padding:0;display:grid;grid-template-columns:1fr 300px;gap:52px;align-items:start;}
.prose h2{font-size:clamp(20px,2.5vw,28px);font-weight:800;color:#2b3340;margin:36px 0 14px;line-height:1.25;}
.prose h2:first-child{margin-top:0;}
.prose h3{font-size:18px;font-weight:700;color:#445162;margin:28px 0 10px;}
.prose p{font-size:15px;color:#5a6472;line-height:1.8;margin:0 0 18px;}
.prose ul,.prose ol{margin:0 0 18px 22px;padding:0;}
.prose li{font-size:15px;color:#5a6472;line-height:1.75;margin-bottom:6px;}
.prose strong{color:#2b3340;font-weight:700;}
.prose a{color:#445162;font-weight:600;text-decoration:underline;text-underline-offset:2px;}
.prose a:hover{color:#2b3340;}
.prose .callout{background:#fff;border:1px solid #dde2e8;border-left:4px solid #d4f000;border-radius:0 10px 10px 0;padding:18px 22px;margin:24px 0;}
.prose .callout p{margin:0;font-weight:600;color:#2b3340;}

/* ── SIDEBAR ── */
.sidebar{position:sticky;top:90px;align-self:start;display:flex;flex-direction:column;gap:20px;}
.sidebar-cta{background:#2b3340;border-radius:16px;padding:28px 24px;text-align:center;}
.sidebar-cta h4{font-size:17px;font-weight:800;color:#fff;margin:0 0 10px;}
.sidebar-cta p{font-size:13px;color:rgba(255,255,255,.65);margin:0 0 20px;line-height:1.6;}
.sidebar-btn-primary{display:block;background:#d4f000;color:#1e2432;font-size:14px;font-weight:800;padding:13px;border-radius:8px;text-decoration:none;margin-bottom:10px;transition:background .2s,transform .2s;}
.sidebar-btn-primary:hover{background:#c5e000;transform:translateY(-1px);}
.sidebar-btn-secondary{display:block;background:rgba(255,255,255,.10);color:#fff;font-size:13px;font-weight:600;padding:11px;border-radius:8px;text-decoration:none;transition:background .2s;}
.sidebar-btn-secondary:hover{background:rgba(255,255,255,.18);}
.sidebar-links{background:#fff;border:1px solid #e5e7eb;border-radius:16px;padding:24px;}
.sidebar-links h5{font-size:14px;font-weight:700;color:#2b3340;margin:0 0 14px;padding-bottom:10px;border-bottom:2px solid #d4f000;}
.sidebar-links ul{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:8px;}
.sidebar-links ul li a{font-size:13px;color:#5a6472;text-decoration:none;display:flex;align-items:center;gap:8px;padding:4px 0;transition:color .2s;}
.sidebar-links ul li a::before{content:'';width:5px;height:5px;border-radius:50%;background:#dde2e8;flex-shrink:0;transition:background .2s;}
.sidebar-links ul li a:hover{color:#2b3340;}
.sidebar-links ul li a:hover::before{background:#d4f000;}

/* ── WHY CHOOSE US CARDS ── */
.why-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:40px;}
.process-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;}
.why-card{background:#fff;border:1px solid #e5e7eb;border-radius:16px;padding:28px 22px;transition:box-shadow .25s,border-color .25s,transform .25s;}
.why-card:hover{box-shadow:0 8px 28px rgba(68,81,98,.12);border-color:#445162;transform:translateY(-4px);}
.why-icon{width:46px;height:46px;border-radius:12px;background:#e8ebee;display:flex;align-items:center;justify-content:center;margin-bottom:14px;transition:background .25s;}
.why-card:hover .why-icon{background:#d4f000;}
.why-icon svg{width:20px;height:20px;stroke:#445162;fill:none;stroke-width:2;transition:stroke .25s;}
.why-card:hover .why-icon svg{stroke:#2b3340;}
.why-card h4{font-size:15px;font-weight:700;color:#2b3340;margin:0 0 8px;}
.why-card p{font-size:13px;color:#6b7280;line-height:1.7;margin:0;}

/* ── SERVICES GRID ── */
.services-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;}
.svc-card{background:#fff;border:1px solid #dde2e8;border-radius:14px;padding:22px;display:flex;align-items:center;gap:18px;text-decoration:none;color:inherit;transition:box-shadow .25s,border-color .25s,transform .25s;}
.svc-card:hover{box-shadow:0 8px 28px rgba(68,81,98,.13);border-color:#445162;transform:translateY(-3px);}
.svc-icon-box{flex-shrink:0;width:56px;height:56px;border-radius:12px;background:#f0f3f6;display:flex;align-items:center;justify-content:center;font-size:26px;transition:background .25s;}
.svc-card:hover .svc-icon-box{background:#2b3340;}
.svc-info{flex:1;}
.svc-info h4{font-size:16px;font-weight:800;color:#2b3340;margin:0 0 5px;}
.svc-info p{font-size:13px;color:#5a6472;margin:0;line-height:1.55;}
.svc-arrow{flex-shrink:0;width:30px;height:30px;border-radius:8px;background:#f0f3f6;display:flex;align-items:center;justify-content:center;transition:background .25s,transform .25s;}
.svc-arrow svg{width:16px;height:16px;stroke:#445162;fill:none;stroke-width:2.5;transition:stroke .25s;}
.svc-card:hover .svc-arrow{background:#445162;transform:translateX(4px);}
.svc-card:hover .svc-arrow svg{stroke:#fff;}

/* ── PROBLEMS LIST ── */
.problems-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin:24px 0;}
.problem-item{background:#fff;border:1px solid #e5e7eb;border-radius:10px;padding:14px 16px;display:flex;align-items:flex-start;gap:12px;}
.problem-item svg{width:16px;height:16px;stroke:#d4f000;fill:none;stroke-width:2.5;flex-shrink:0;margin-top:2px;}
.problem-item span{font-size:14px;color:#5a6472;line-height:1.55;}

/* ── STATS BAR ── */
.stats-bar{display:flex;align-items:center;justify-content:center;background:#2b3340;border-radius:16px;padding:32px 40px;margin:48px 0;}
.stat-item{flex:1;display:flex;flex-direction:column;align-items:center;gap:6px;text-align:center;}
.stat-num{font-size:34px;font-weight:900;color:#fff;line-height:1;}
.stat-num em{font-style:normal;color:#d4f000;}
.stat-lbl{font-size:11px;color:rgba(255,255,255,.55);font-weight:600;text-transform:uppercase;letter-spacing:.8px;}
.stat-div{width:1px;height:44px;background:rgba(255,255,255,.12);flex-shrink:0;}

/* ── BOOKING SECTION ── */
.booking-section{display:flex;justify-content:center;padding:56px 32px;background:#fafbfc;}
.booking-section-inner{max-width:1100px;width:100%;}
.booking-top{text-align:center;margin-bottom:40px;}
.booking-badge{display:inline-flex;align-items:center;gap:8px;background:#e8ebee;color:#445162;font-size:11px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;padding:6px 14px;border-radius:50px;margin-bottom:16px;}
.booking-badge svg{width:12px;height:12px;stroke:#445162;fill:none;stroke-width:2.5;}
.booking-title{font-size:clamp(26px,3.5vw,38px);font-weight:900;color:#2b3340;margin:0 0 12px;}
.booking-sub{font-size:15px;color:#6b7280;line-height:1.7;max-width:560px;margin:0 auto;}
.booking-card{background:#fff;border:1px solid #e5e7eb;border-radius:20px;padding:40px;box-shadow:0 4px 24px rgba(68,81,98,.07);}
.bf-row{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:16px;}
.bf-group{display:flex;flex-direction:column;gap:6px;}
.bf-group label{font-size:13px;font-weight:600;color:#2b3340;}
.bf-group input,.bf-group select,.bf-group textarea{width:100%;padding:11px 14px;border:1.5px solid #dde2e8;border-radius:8px;font-size:14px;color:#2b3340;background:#fff;font-family:inherit;outline:none;transition:border-color .2s,box-shadow .2s;}
.bf-group input:focus,.bf-group select:focus,.bf-group textarea:focus{border-color:#445162;box-shadow:0 0 0 3px rgba(68,81,98,.10);}
.bf-full{margin-bottom:16px;}
.bf-group textarea{resize:vertical;min-height:100px;line-height:1.6;}
.bf-foot{display:flex;align-items:center;justify-content:space-between;gap:20px;margin-top:8px;}
.bf-note{display:flex;align-items:center;gap:6px;font-size:13px;color:#6b7280;}
.bf-note svg{width:14px;height:14px;stroke:#445162;fill:none;stroke-width:2;flex-shrink:0;}
.bf-submit{display:inline-flex;align-items:center;gap:8px;background:#d4f000;color:#1e2432;font-size:14px;font-weight:800;padding:13px 28px;border-radius:9px;border:none;cursor:pointer;font-family:inherit;transition:background .2s,transform .2s,box-shadow .2s;}
.bf-submit:hover{background:#c5e000;transform:translateY(-1px);box-shadow:0 6px 20px rgba(212,240,0,.35);}
.bf-submit svg{width:15px;height:15px;stroke:#1e2432;fill:none;stroke-width:2.5;}
.form-msg{margin-top:18px;padding:16px 20px;border-radius:10px;font-size:14px;font-weight:600;display:none;}
.form-msg.success{background:#f0fdf4;border:1px solid #bbf7d0;color:#166534;}
.contact-strip{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-top:20px;}
.cs-card{background:#fff;border:1px solid #e5e7eb;border-radius:14px;padding:16px;display:flex;align-items:center;gap:12px;text-decoration:none;color:inherit;transition:box-shadow .25s,border-color .25s,transform .25s;}
.cs-card:hover{box-shadow:0 6px 20px rgba(68,81,98,.10);border-color:#445162;transform:translateY(-2px);}
.cs-icon{width:40px;height:40px;border-radius:10px;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.cs-icon.phone{background:rgba(212,240,0,.15);}
.cs-icon.email{background:rgba(68,81,98,.10);}
.cs-icon.chat{background:rgba(37,211,102,.12);}
.cs-icon.hours{background:rgba(68,81,98,.08);}
.cs-icon svg{width:18px;height:18px;stroke:#2b3340;fill:none;stroke-width:2;}
.cs-icon.phone svg{stroke:#2b3340;}
.cs-text span{display:block;font-size:11px;color:#9ca3af;font-weight:500;margin-bottom:2px;}
.cs-text strong{display:block;font-size:13px;color:#2b3340;font-weight:700;}

/* ── BLOG CARDS ── */
.blog-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;}
.blog-card{background:#fff;border:1px solid #e5e7eb;border-radius:16px;overflow:hidden;text-decoration:none;color:inherit;transition:box-shadow .25s,transform .25s;}
.blog-card:hover{box-shadow:0 8px 28px rgba(68,81,98,.12);transform:translateY(-4px);}
.blog-thumb{position:relative;height:200px;overflow:hidden;}
.blog-thumb img{width:100%;height:100%;object-fit:cover;transition:transform .4s;}
.blog-card:hover .blog-thumb img{transform:scale(1.04);}
.blog-cat-pill{position:absolute;bottom:12px;left:12px;background:#d4f000;color:#1e2432;font-size:11px;font-weight:700;padding:4px 12px;border-radius:20px;text-transform:uppercase;letter-spacing:.5px;}
.blog-body{padding:22px;}
.blog-meta{display:flex;align-items:center;gap:14px;margin-bottom:10px;}
.blog-meta span{display:flex;align-items:center;gap:5px;font-size:12px;color:#9ca3af;}
.blog-meta svg{width:12px;height:12px;stroke:#9ca3af;fill:none;stroke-width:2;}
.blog-card-title{font-size:16px;font-weight:800;color:#2b3340;margin:0 0 8px;line-height:1.35;}
.blog-card-excerpt{font-size:13px;color:#6b7280;line-height:1.65;margin:0 0 14px;}
.blog-readmore{font-size:13px;font-weight:700;color:#445162;display:flex;align-items:center;gap:5px;}
.blog-readmore svg{width:13px;height:13px;stroke:#445162;fill:none;stroke-width:2.5;transition:transform .2s;}
.blog-card:hover .blog-readmore svg{transform:translateX(4px);}

/* ── BLOG POST ── */
.post-hero{background:linear-gradient(135deg,#1e2432 0%,#2b3340 60%,#3a4555 100%);padding:130px 32px 0;display:flex;justify-content:center;}
.post-hero-inner{max-width:1100px;width:100%;}
.post-cat-pill{display:inline-block;background:#d4f000;color:#1e2432;font-size:11px;font-weight:700;padding:4px 14px;border-radius:20px;text-transform:uppercase;letter-spacing:.5px;margin-bottom:16px;}
.post-hero h1{font-size:clamp(26px,4vw,48px);font-weight:900;color:#fff;line-height:1.2;margin:0 0 16px;max-width:780px;}
.post-meta{display:flex;align-items:center;gap:18px;font-size:13px;color:rgba(255,255,255,.6);flex-wrap:wrap;margin-bottom:40px;}
.post-meta svg{width:13px;height:13px;stroke:rgba(255,255,255,.6);fill:none;stroke-width:2;}
.post-hero-img{width:100%;max-height:440px;object-fit:cover;display:block;margin-top:0;border-radius:12px 12px 0 0;}
.post-layout{max-width:1100px;margin:0 auto;padding:60px 32px;display:grid;grid-template-columns:1fr 300px;gap:48px;align-items:start;}
.post-content h2{font-size:clamp(20px,2.5vw,26px);font-weight:800;color:#2b3340;margin:36px 0 14px;}
.post-content h2:first-child{margin-top:0;}
.post-content h3{font-size:18px;font-weight:700;color:#445162;margin:24px 0 10px;}
.post-content p{font-size:15px;color:#5a6472;line-height:1.82;margin:0 0 18px;}
.post-content ul,.post-content ol{margin:0 0 18px 22px;padding:0;}
.post-content li{font-size:15px;color:#5a6472;line-height:1.75;margin-bottom:6px;}
.post-content strong{color:#2b3340;font-weight:700;}
.post-content .callout{background:#f8f9fa;border:1px solid #dde2e8;border-left:4px solid #d4f000;border-radius:0 10px 10px 0;padding:18px 22px;margin:24px 0;}
.post-content .callout p{margin:0;font-weight:600;color:#2b3340;}
.post-content table{width:100%;border-collapse:collapse;margin:24px 0;font-size:14px;}
.post-content table th{background:#2b3340;color:#fff;padding:12px 16px;text-align:left;font-weight:700;}
.post-content table td{padding:11px 16px;border-bottom:1px solid #e5e7eb;color:#5a6472;}
.post-content table tr:nth-child(even) td{background:#f8f9fa;}
.post-sidebar{position:sticky;top:90px;align-self:start;display:flex;flex-direction:column;gap:20px;}

/* ── CTA BANNER ── */
.cta-banner{
  background:linear-gradient(135deg,#2b3340 0%,#445162 100%);
  padding:64px 32px;display:flex;justify-content:center;
}
.cta-banner-inner{max-width:1100px;width:100%;display:flex;align-items:center;justify-content:space-between;gap:40px;flex-wrap:wrap;}
.cta-banner-text h2{font-size:clamp(22px,3vw,34px);font-weight:900;color:#fff;margin:0 0 10px;}
.cta-banner-text p{font-size:15px;color:rgba(255,255,255,.75);margin:0;line-height:1.6;}
.cta-banner-btns{display:flex;gap:14px;flex-wrap:wrap;flex-shrink:0;}
.btn-cta-primary{display:inline-flex;align-items:center;gap:8px;background:#d4f000;color:#1e2432;font-size:15px;font-weight:800;padding:14px 26px;border-radius:9px;text-decoration:none;transition:background .2s,transform .2s,box-shadow .2s;}
.btn-cta-primary:hover{background:#c5e000;transform:translateY(-2px);box-shadow:0 8px 24px rgba(212,240,0,.35);}
.btn-cta-secondary{display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,.12);color:#fff;font-size:15px;font-weight:700;padding:14px 26px;border-radius:9px;text-decoration:none;border:1.5px solid rgba(255,255,255,.3);transition:background .2s,border-color .2s,transform .2s;}
.btn-cta-secondary:hover{background:rgba(255,255,255,.20);border-color:rgba(255,255,255,.6);transform:translateY(-2px);}
.btn-cta-primary svg,.btn-cta-secondary svg{width:15px;height:15px;fill:none;stroke-width:2.5;stroke:currentColor;}

/* ── FOOTER ── */
.footer-outer{display:flex;justify-content:center;padding:40px 32px 0;}
.footer-wrap{
  max-width:1100px;width:100%;
  background:linear-gradient(160deg,#1e2432 0%,#2b3340 100%);
  border-radius:20px 20px 0 0;padding:56px 48px 32px;
}
.footer-top{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:40px;margin-bottom:40px;padding-bottom:32px;border-bottom:1px solid rgba(255,255,255,.08);}
.footer-logo-img{height:48px;width:auto;display:block;object-fit:contain;margin-bottom:16px;}
.footer-desc{font-size:13px;color:rgba(255,255,255,.50);line-height:1.75;margin:0 0 20px;}
.footer-socials{display:flex;gap:9px;}
.footer-socials a{width:34px;height:34px;border-radius:8px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.10);display:flex;align-items:center;justify-content:center;transition:background .2s,border-color .2s;}
.footer-socials a:hover{background:#445162;border-color:#445162;}
.footer-socials svg{width:14px;height:14px;stroke:rgba(255,255,255,.65);fill:none;stroke-width:2;transition:stroke .2s;}
.footer-socials a:hover svg{stroke:#fff;}
.footer-socials a.fill-icon svg{fill:rgba(255,255,255,.65);stroke:none;}
.footer-socials a.fill-icon:hover svg{fill:#fff;}
.footer-col h4{font-size:13px;font-weight:700;color:#fff;text-transform:uppercase;letter-spacing:1px;margin:0 0 16px;padding-bottom:10px;border-bottom:1px solid rgba(255,255,255,.08);}
.footer-col ul{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:9px;}
.footer-col ul li a{display:flex;align-items:center;gap:7px;font-size:13px;color:rgba(255,255,255,.55);text-decoration:none;transition:color .2s;}
.footer-col ul li a::before{content:'';width:4px;height:4px;border-radius:50%;background:#445162;flex-shrink:0;transition:background .2s;}
.footer-col ul li a:hover{color:#d4f000;}
.footer-col ul li a:hover::before{background:#d4f000;}
.footer-contact-list{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:13px;}
.footer-contact-list li{display:flex;align-items:flex-start;gap:10px;}
.footer-contact-list svg{width:14px;height:14px;stroke:#d4f000;fill:none;stroke-width:2;flex-shrink:0;margin-top:2px;}
.footer-contact-list a,.footer-contact-list span{font-size:13px;color:rgba(255,255,255,.55);text-decoration:none;line-height:1.6;transition:color .2s;}
.footer-contact-list a:hover{color:#d4f000;}
.footer-bottom{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;}
.footer-bottom p{font-size:12px;color:rgba(255,255,255,.30);margin:0;}
.footer-bottom-links{display:flex;gap:18px;}
.footer-bottom-links a{font-size:12px;color:rgba(255,255,255,.30);text-decoration:none;transition:color .2s;}
.footer-bottom-links a:hover{color:#d4f000;}

/* ── FAQ ACCORDION ── */
.faq-list{display:flex;flex-direction:column;gap:10px;}
.faq-item{background:#fff;border:1px solid #dde2e8;border-radius:12px;overflow:hidden;}
.faq-q{width:100%;padding:18px 22px;background:transparent;border:none;display:flex;align-items:center;justify-content:space-between;gap:16px;cursor:pointer;text-align:left;}
.faq-q-text{font-size:15px;font-weight:700;color:#2b3340;}
.faq-q-icon{flex-shrink:0;width:28px;height:28px;border-radius:8px;background:#f0f3f6;display:flex;align-items:center;justify-content:center;transition:background .25s,transform .25s;}
.faq-q-icon svg{width:14px;height:14px;stroke:#445162;fill:none;stroke-width:2.5;transition:transform .25s;}
.faq-item.open .faq-q-icon{background:#d4f000;}
.faq-item.open .faq-q-icon svg{transform:rotate(180deg);stroke:#1e2432;}
.faq-a{max-height:0;overflow:hidden;opacity:0;transition:max-height .35s ease,opacity .35s ease;}
.faq-a-inner{padding:0 22px 18px;}
.faq-a-inner p{font-size:14px;color:#5a6472;line-height:1.75;margin:0;}

/* ── BRANDS GRID ── */
.brands-grid-5{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin-top:32px;}
.brand-tile{background:#fff;border:1px solid #dde2e8;border-radius:10px;padding:20px;display:flex;align-items:center;justify-content:center;min-height:80px;font-size:14px;font-weight:700;color:#445162;transition:box-shadow .25s,border-color .25s,transform .25s;text-align:center;}
.brand-tile:hover{box-shadow:0 6px 20px rgba(68,81,98,.12);border-color:#445162;transform:translateY(-2px);color:#2b3340;}

/* ── RESPONSIVE ── */
@media(max-width:1024px){
  .site-navbar{width:calc(100% - 32px);}
  .nav-inner{padding:12px 20px;}
  .footer-top{grid-template-columns:1fr 1fr;gap:32px;}
  .content-wrap{grid-template-columns:1fr;gap:32px;}
  .sidebar{position:static;}
  .post-layout{grid-template-columns:1fr;padding:48px 24px;}
  .post-sidebar{position:static;}
  .why-grid{grid-template-columns:repeat(2,1fr);}
  .process-grid{grid-template-columns:repeat(2,1fr);}
  .contact-strip{grid-template-columns:repeat(3,1fr);}
  .blog-grid{grid-template-columns:repeat(2,1fr);}
  .bf-row{grid-template-columns:repeat(2,1fr);}
  .brands-grid-5{grid-template-columns:repeat(3,1fr);}
  .section-box{padding:48px 36px;}
}
@media(max-width:768px){
  .site-navbar{position:fixed!important;top:0!important;left:0!important;right:0!important;transform:none!important;width:100%!important;max-width:none!important;border-radius:0!important;margin-top:0!important;}
  .nav-toggle{display:flex;}
  .nav-menu{
    display:flex!important;flex-direction:column;gap:0;
    position:absolute;top:100%;left:0;right:0;
    background:rgba(43,51,64,.98);border-radius:0 0 16px 16px;
    padding:12px 0;
    opacity:0;visibility:hidden;transform:translateY(-8px);
    transition:opacity .28s,transform .28s,visibility .28s;
    pointer-events:none;
  }
  .nav-menu.open{opacity:1;visibility:visible;transform:translateY(0);pointer-events:auto;}
  .nav-menu>li{width:100%;border-bottom:1px solid rgba(255,255,255,.08);}
  .nav-menu>li:last-child{border-bottom:none;}
  .nav-menu>li>a{padding:13px 24px;font-size:15px;width:100%;justify-content:space-between;}
  .drop-menu{position:static;transform:none!important;opacity:1!important;visibility:visible!important;box-shadow:none;background:rgba(255,255,255,.05);border-radius:0;padding:4px 0;pointer-events:auto;display:none;}
  .drop-menu.mob-open{display:block;}
  .drop-menu::before{display:none;}
  .drop-menu a{padding:10px 36px;}
  .has-drop::after{display:none;}
  .inner-hero{padding:100px 20px 60px;}
  .section-outer{padding:20px 16px;}
  .section-outer.section-outer--plain{padding:0 16px;}
  .section-box{padding:36px 24px;}
  .why-grid{grid-template-columns:1fr;}
  .services-grid{grid-template-columns:1fr;}
  .problems-grid{grid-template-columns:1fr;}
  .stats-bar{flex-wrap:wrap;gap:24px;padding:28px 24px;}
  .stat-div{display:none;}
  .contact-strip{grid-template-columns:repeat(2,1fr);}
  .blog-grid{grid-template-columns:1fr;}
  .bf-row{grid-template-columns:1fr;}
  .cta-banner-inner{flex-direction:column;text-align:center;}
  .cta-banner-btns{justify-content:center;}
  .footer-top{grid-template-columns:1fr;}
  .footer-outer{padding:20px 16px 0;}
  .footer-wrap{padding:40px 24px 24px;border-radius:12px 12px 0 0;}
  .breadcrumb-bar{padding:10px 20px;}
  .booking-section{padding:36px 16px;}
  .booking-card{padding:24px 20px;}
  .brands-grid-5{grid-template-columns:repeat(2,1fr);}
  .post-hero{padding:100px 20px 0;}
  .content-wrap{grid-template-columns:1fr;gap:24px;}
  .process-grid{grid-template-columns:1fr!important;}
}
"""

# ─────────────────────────────────────────────
# SHARED JS
# ─────────────────────────────────────────────
SHARED_JS = """
(function(){
  var navbar = document.getElementById('siteNavbar');
  var toggle = document.getElementById('navToggle');
  var menu   = document.getElementById('navMenu');
  var MOBILE = 768;
  function isMob(){ return window.innerWidth <= MOBILE; }

  if(toggle && menu){
    toggle.addEventListener('click',function(e){
      e.stopPropagation();
      var open = menu.classList.contains('open');
      menu.classList.toggle('open',!open);
      toggle.setAttribute('aria-expanded', !open ? 'true' : 'false');
    });
  }

  // Mobile dropdown toggles
  document.querySelectorAll('.has-drop > a').forEach(function(link){
    link.addEventListener('click',function(e){
      if(!isMob()) return;
      e.preventDefault(); e.stopPropagation();
      var dm = link.nextElementSibling;
      if(dm && dm.classList.contains('drop-menu')){
        dm.classList.toggle('mob-open');
      }
    });
  });

  document.addEventListener('click',function(e){
    if(!isMob()) return;
    if(!e.target.closest('#siteNavbar')){ 
      if(menu) menu.classList.remove('open');
      if(toggle) toggle.setAttribute('aria-expanded','false');
    }
  });

  window.addEventListener('scroll',function(){
    if(navbar) navbar.classList.toggle('scrolled', window.pageYOffset > 60);
  },{passive:true});

  // FAQ accordion
  document.querySelectorAll('.faq-q').forEach(function(btn){
    btn.addEventListener('click',function(){
      var item = btn.parentElement;
      var ans  = item.querySelector('.faq-a');
      var isOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(function(el){
        el.classList.remove('open');
        var a = el.querySelector('.faq-a');
        a.style.maxHeight='0'; a.style.opacity='0';
      });
      if(!isOpen){
        item.classList.add('open');
        ans.style.maxHeight = ans.scrollHeight + 'px';
        ans.style.opacity = '1';
      }
    });
  });

  // Booking form
  var form = document.getElementById('bookingForm');
  if(form){
    form.addEventListener('submit',function(e){
      e.preventDefault();
      var msg = document.getElementById('formMsg');
      if(msg){
        msg.className='form-msg success';
        msg.textContent='✅ Thank you! We received your request and will contact you shortly.';
        msg.style.display='block';
        form.reset();
        msg.scrollIntoView({behavior:'smooth',block:'center'});
        setTimeout(function(){ msg.style.display='none'; },9000);
      }
    });
    var ph = form.querySelector('[name="phone"]');
    if(ph){ ph.addEventListener('input',function(e){
      var v=e.target.value.replace(/\\D/g,'');
      if(v.length<=3) v='('+v;
      else if(v.length<=6) v='('+v.slice(0,3)+') '+v.slice(3);
      else v='('+v.slice(0,3)+') '+v.slice(3,6)+'-'+v.slice(6,10);
      e.target.value=v;
    }); }
    var zp = form.querySelector('[name="zip"]');
    if(zp){ zp.addEventListener('input',function(e){ e.target.value=e.target.value.replace(/\\D/g,'').slice(0,5); }); }
  }
}());
"""

# ─────────────────────────────────────────────
# HTML BUILDING BLOCKS
# ─────────────────────────────────────────────

def head(title, desc, canonical):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<link rel="icon" href="{FAVICON}">
{GFONT}
<style>{SHARED_CSS}</style>
</head>
<body>"""

def navbar(active=""):
    services_drop = """
        <ul class="drop-menu">
          <li><a href="/Prime-Clovis/refrigerator-repair-clovis-ca/">Refrigerator Repair</a></li>
          <li><a href="/Prime-Clovis/washer-repair-clovis-ca/">Washer Repair</a></li>
          <li><a href="/Prime-Clovis/dryer-repair-clovis-ca/">Dryer Repair</a></li>
          <li><a href="/Prime-Clovis/dishwasher-repair-clovis-ca/">Dishwasher Repair</a></li>
          <li><a href="/Prime-Clovis/oven-repair-clovis-ca/">Oven &amp; Range Repair</a></li>
          <li><a href="/Prime-Clovis/microwave-repair-clovis-ca/">Microwave Repair</a></li>
          <li><a href="/Prime-Clovis/freezer-repair-clovis-ca/">Freezer Repair</a></li>
          <li><a href="/Prime-Clovis/ice-maker-repair-clovis-ca/">Ice Maker Repair</a></li>
          <li><a href="/Prime-Clovis/wine-cooler-repair-clovis-ca/">Wine Cooler Repair</a></li>
          <li><a href="/Prime-Clovis/garbage-disposal-repair-clovis-ca/">Garbage Disposal</a></li>
        </ul>"""
    areas_drop = """
        <ul class="drop-menu">
          <li><a href="/Prime-Clovis/fresno-appliance-repair/">Fresno</a></li>
          <li><a href="/Prime-Clovis/clovis-appliance-repair/">Clovis</a></li>
          <li><a href="/Prime-Clovis/madera-appliance-repair/">Madera</a></li>
          <li><a href="/Prime-Clovis/sanger-appliance-repair/">Sanger</a></li>
          <li><a href="/Prime-Clovis/fowler-appliance-repair/">Fowler</a></li>
          <li><a href="/Prime-Clovis/fraint-appliance-repair/">Friant</a></li>
        </ul>"""
    active_home    = ' class="active"' if active=="home"    else ""
    active_svc     = ' class="active"' if active=="services" else ""
    active_areas   = ' class="active"' if active=="areas"   else ""
    active_about   = ' class="active"' if active=="about"   else ""
    active_blog    = ' class="active"' if active=="blog"    else ""
    return f"""
<nav class="site-navbar" id="siteNavbar">
  <div class="nav-inner">
    <div class="nav-logo">
      <a href="/Prime-Clovis/"><img src="{LOGO}" alt="Prime Appliance Repair Services" width="160" height="48"></a>
    </div>
    <button class="nav-toggle" id="navToggle" aria-expanded="false" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
    <ul class="nav-menu" id="navMenu">
      <li{active_home}><a href="/Prime-Clovis/">Home</a></li>
      <li class="has-drop{' active' if active=='services' else ''}">
        <a href="/Prime-Clovis/services/" class="has-drop-link">Services
          <svg class="drop-icon" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>
        </a>
        {services_drop}
      </li>
      <li class="has-drop{' active' if active=='areas' else ''}">
        <a href="/Prime-Clovis/fresno-appliance-repair/" class="has-drop-link">Service Areas
          <svg class="drop-icon" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>
        </a>
        {areas_drop}
      </li>
      <li{active_about}><a href="/Prime-Clovis/about-us/">About Us</a></li>
      <li{active_blog}><a href="/Prime-Clovis/blog-2/">Blog</a></li>
      <li><a href="/Prime-Clovis/contact-us/">Contact</a></li>
      <li><a href="/Prime-Clovis/book-an-appointment/" class="nav-cta">Book Online</a></li>
    </ul>
  </div>
</nav>"""

def breadcrumb(crumbs):
    """crumbs = list of (label, url) — last one has no url"""
    parts = []
    for i,(label,url) in enumerate(crumbs):
        if i < len(crumbs)-1:
            parts.append(f'<a href="{url}">{label}</a>')
            parts.append('<span class="sep">›</span>')
        else:
            parts.append(f'<span class="cur">{label}</span>')
    return f"""
<div class="breadcrumb-bar">
  <div class="breadcrumb-inner">
    {''.join(parts)}
  </div>
</div>"""

def inner_hero(badge, h1, p, btns_html="", trust=True, highlight=""):
    trust_html = ""
    if trust:
        trust_html = """
    <div class="inner-hero-trust">
      <div class="trust-chip"><svg viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg><span>Warranty Included</span></div>
      <div class="trust-chip"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg><span>Same-Day Available</span></div>
      <div class="trust-chip"><svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg><span>Certified Technicians</span></div>
    </div>"""
    return f"""
<section class="inner-hero">
  <div class="inner-hero-inner">
    <div class="inner-hero-badge"><div class="inner-hero-badge-dot"></div><span>{badge}</span></div>
    <h1>{h1}</h1>
    <p>{p}</p>
    {btns_html}
    {trust_html}
  </div>
</section>"""

def hero_btns(primary_text="Book Online", primary_href="/Prime-Clovis/book-an-appointment/",
              secondary_text="Call Now", secondary_href=f"tel:{PHONE_RAW}"):
    return f"""
    <div class="inner-hero-btns">
      <a href="{primary_href}" class="btn-hero-primary">
        <svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
        {primary_text}
      </a>
      <a href="{secondary_href}" class="btn-hero-secondary">
        <svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 10.8 19.79 19.79 0 010 2.18 2 2 0 012 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 14.92z"/></svg>
        {secondary_text}
      </a>
    </div>"""

def booking_section():
    return f"""
<section class="booking-section">
  <div class="booking-section-inner">
    <div class="booking-top">
      <div class="booking-badge">
        <svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
        Book Online
      </div>
      <h2 class="booking-title">Book an Appointment Online</h2>
      <p class="booking-sub">Quick and easy — fill in your details and our team will contact you to confirm.</p>
    </div>
    <div class="booking-card">
      <form id="bookingForm">
        <div class="bf-row">
          <div class="bf-group"><label>Full Name</label><input type="text" name="name" placeholder="John Smith" required></div>
          <div class="bf-group"><label>Phone Number</label><input type="tel" name="phone" placeholder="(559) 000-0000" required></div>
          <div class="bf-group"><label>Zip Code</label><input type="text" name="zip" placeholder="93720" required></div>
          <div class="bf-group"><label>Appliance Type</label>
            <select name="appliance" required>
              <option value="">Select...</option>
              <option>Refrigerator</option><option>Washer</option><option>Dryer</option>
              <option>Dishwasher</option><option>Oven / Range</option><option>Microwave</option>
              <option>Freezer</option><option>Ice Maker</option><option>Wine Cooler</option>
              <option>Garbage Disposal</option><option>Other</option>
            </select>
          </div>
        </div>
        <div class="bf-group bf-full"><label>Describe the Issue</label><textarea name="issue" placeholder="Tell us what's happening with your appliance..." required></textarea></div>
        <div class="bf-foot">
          <p class="bf-note"><svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>Your info is safe and never shared.</p>
          <button type="submit" class="bf-submit"><svg viewBox="0 0 24 24"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>Send My Request</button>
        </div>
      </form>
      <div id="formMsg" class="form-msg"></div>
    </div>
    <div class="contact-strip">
      <a class="cs-card" href="tel:{PHONE_RAW}">
        <div class="cs-icon phone"><svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 10.8 19.79 19.79 0 010 2.18 2 2 0 012 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 14.92z"/></svg></div>
        <div class="cs-text"><span>Call Us</span><strong>{PHONE}</strong></div>
      </a>
      <a class="cs-card" href="mailto:{EMAIL}">
        <div class="cs-icon email"><svg viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg></div>
        <div class="cs-text"><span>Email Us</span><strong>appliancerepairserviceus</strong></div>
      </a>
      <a class="cs-card" href="https://wa.me/message/7XVFDXQTK2XSP1" target="_blank">
        <div class="cs-icon chat"><svg viewBox="0 0 24 24"><path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z"/></svg></div>
        <div class="cs-text"><span>WhatsApp</span><strong>Click to Chat</strong></div>
      </a>
      <div class="cs-card">
        <div class="cs-icon hours"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div>
        <div class="cs-text"><span>Mon–Fri</span><strong>7:00 AM – 7:00 PM</strong></div>
      </div>
      <div class="cs-card">
        <div class="cs-icon hours"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div>
        <div class="cs-text"><span>Saturday</span><strong>7:00 AM – 7:00 PM</strong></div>
      </div>
    </div>
  </div>
</section>"""

def cta_banner():
    return f"""
<section class="cta-banner">
  <div class="cta-banner-inner">
    <div class="cta-banner-text">
      <h2>Ready to Fix Your Appliance?</h2>
      <p>Same-day service available. Certified technicians. Warranty on parts and labor.</p>
    </div>
    <div class="cta-banner-btns">
      <a href="tel:{PHONE_RAW}" class="btn-cta-primary">
        <svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 10.8 19.79 19.79 0 010 2.18 2 2 0 012 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 14.92z"/></svg>
        {PHONE}
      </a>
      <a href="/Prime-Clovis/book-an-appointment/" class="btn-cta-secondary">
        <svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
        Book Appointment
      </a>
    </div>
  </div>
</section>"""

def footer():
    return f"""
<div class="footer-outer">
<div class="footer-wrap">
  <div class="footer-top">
    <div class="footer-col">
      <a href="/Prime-Clovis/"><img class="footer-logo-img" src="{LOGO}" alt="Prime Appliance Repair Services"></a>
      <p class="footer-desc">Reliable appliance repair backed by 15+ years of experience. Serving Fresno, Clovis, and the Central Valley with certified technicians.</p>
      <div class="footer-socials">
        <a href="https://www.facebook.com/profile.php?id=61580997082846" aria-label="Facebook">
          <svg viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg>
        </a>
        <a href="https://www.instagram.com/prime.appliancerepair" aria-label="Instagram">
          <svg viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
        </a>
        <a href="https://x.com/primeapplrepair" aria-label="X" class="fill-icon">
          <svg viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
        </a>
        <a href="https://maps.app.goo.gl/gfwd4sV6wbQkwE5C9" aria-label="Google" class="fill-icon">
          <svg viewBox="0 0 24 24"><path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/><path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/><path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/><path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/></svg>
        </a>
      </div>
    </div>
    <div class="footer-col">
      <h4>Quick Links</h4>
      <ul>
        <li><a href="/Prime-Clovis/">Home</a></li>
        <li><a href="/Prime-Clovis/about-us/">About Us</a></li>
        <li><a href="/Prime-Clovis/services/">Services</a></li>
        <li><a href="/Prime-Clovis/blog-2/">Blog</a></li>
        <li><a href="/Prime-Clovis/contact-us/">Contact</a></li>
        <li><a href="/Prime-Clovis/book-an-appointment/">Book Appointment</a></li>
        <li><a href="/Prime-Clovis/privacy-policy/">Privacy Policy</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Appliances We Fix</h4>
      <ul>
        <li><a href="/Prime-Clovis/refrigerator-repair-clovis-ca/">Refrigerator Repair</a></li>
        <li><a href="/Prime-Clovis/washer-repair-clovis-ca/">Washer Repair</a></li>
        <li><a href="/Prime-Clovis/dryer-repair-clovis-ca/">Dryer Repair</a></li>
        <li><a href="/Prime-Clovis/dishwasher-repair-clovis-ca/">Dishwasher Repair</a></li>
        <li><a href="/Prime-Clovis/oven-repair-clovis-ca/">Oven &amp; Range Repair</a></li>
        <li><a href="/Prime-Clovis/microwave-repair-clovis-ca/">Microwave Repair</a></li>
        <li><a href="/Prime-Clovis/freezer-repair-clovis-ca/">Freezer Repair</a></li>
        <li><a href="/Prime-Clovis/ice-maker-repair-clovis-ca/">Ice Maker Repair</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Contact</h4>
      <ul class="footer-contact-list">
        <li><svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 10.8 19.79 19.79 0 010 2.18 2 2 0 012 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 14.92z"/></svg><a href="tel:{PHONE_RAW}">{PHONE}</a></li>
        <li><svg viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><svg viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg><span>Fresno &amp; Clovis, CA</span></li>
        <li><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg><span>Mon–Sat: 7AM–7PM</span></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <p>&copy; 2026 Prime Appliance Repair Services. All rights reserved.</p>
    <div class="footer-bottom-links">
      <a href="/Prime-Clovis/privacy-policy/">Privacy Policy</a>
    </div>
  </div>
</div>
</div>
<script>{SHARED_JS}</script>
</body></html>"""

def sidebar_services():
    return """
<div class="sidebar">
  <div class="sidebar-cta">
    <h4>Schedule Service Today</h4>
    <p>Same-day &amp; next-day appointments available.</p>
    <a href="/Prime-Clovis/book-an-appointment/" class="sidebar-btn-primary">Book Online</a>
    <a href="tel:+15597650303" class="sidebar-btn-secondary">&#x260E; (559) 765-0303</a>
  </div>
  <div class="sidebar-links">
    <h5>Our Services</h5>
    <ul>
      <li><a href="/Prime-Clovis/refrigerator-repair-clovis-ca/">Refrigerator Repair</a></li>
      <li><a href="/Prime-Clovis/freezer-repair-clovis-ca/">Freezer Repair</a></li>
      <li><a href="/Prime-Clovis/washer-repair-clovis-ca/">Washer Repair</a></li>
      <li><a href="/Prime-Clovis/dryer-repair-clovis-ca/">Dryer Repair</a></li>
      <li><a href="/Prime-Clovis/dishwasher-repair-clovis-ca/">Dishwasher Repair</a></li>
      <li><a href="/Prime-Clovis/oven-repair-clovis-ca/">Oven &amp; Range Repair</a></li>
      <li><a href="/Prime-Clovis/stove-repair-clovis-ca/">Stove Repair</a></li>
      <li><a href="/Prime-Clovis/microwave-repair-clovis-ca/">Microwave Repair</a></li>
      <li><a href="/Prime-Clovis/wine-cooler-repair-clovis-ca/">Wine Cooler Repair</a></li>
      <li><a href="/Prime-Clovis/ice-maker-repair-clovis-ca/">Ice Maker Repair</a></li>
      <li><a href="/Prime-Clovis/garbage-disposal-repair-clovis-ca/">Garbage Disposal</a></li>
    </ul>
  </div>
  <div class="sidebar-links">
    <h5>Service Areas</h5>
    <ul>
      <li><a href="/Prime-Clovis/fresno-appliance-repair/">Fresno</a></li>
      <li><a href="/Prime-Clovis/clovis-appliance-repair/">Clovis</a></li>
      <li><a href="/Prime-Clovis/madera-appliance-repair/">Madera</a></li>
      <li><a href="/Prime-Clovis/sanger-appliance-repair/">Sanger</a></li>
      <li><a href="/Prime-Clovis/fowler-appliance-repair/">Fowler</a></li>
      <li><a href="/Prime-Clovis/fraint-appliance-repair/">Friant</a></li>
    </ul>
  </div>
</div>"""

def why_cards():
    items = [
        ("M22 11.08V12a10 10 0 11-5.93-9.14M22 4L12 14.01l-3-2.99","polyline points='22 4 12 14.01 9 11.01'","Same-Day Service","Same-day or next-day appointments — we know a broken appliance can't wait."),
        ("M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z","","Parts &amp; Labor Warranty","Every repair backed by a warranty. If it's not right, we'll make it right at no extra cost."),
        ("M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0zM12 9v4M12 17h.01","","Upfront Pricing","We give you a clear quote before starting. No hidden fees. No surprises. Ever."),
        ("M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2M9 7a4 4 0 100 8 4 4 0 000-8z","","Certified Technicians","Factory-trained technicians experienced with all major appliance brands."),
        ("M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z","","Quality OEM Parts","We use only manufacturer-approved parts for lasting repairs and peak performance."),
        ("M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z M9 22V12h6v10","","Local &amp; Trusted","Proudly serving Fresno, Clovis, and the Central Valley since 2009."),
    ]
    cards = ""
    for (path, extra, title, desc) in items:
        svg = f'<svg viewBox="0 0 24 24"><path d="{path}"/></svg>' if not extra else f'<svg viewBox="0 0 24 24"><path d="{path}"/></svg>'
        cards += f"""
    <div class="why-card">
      <div class="why-icon">{svg}</div>
      <h4>{title}</h4>
      <p>{desc}</p>
    </div>"""
    return f'<div class="why-grid">{cards}</div>'

def write_page(path, html):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✓ {path.replace(BASE,'')}")


# ═══════════════════════════════════════════════════════════════
# PAGE BUILDERS
# ═══════════════════════════════════════════════════════════════

# ── ABOUT US ────────────────────────────────────────────────────
def build_about():
    content = head("About Us | Prime Appliance Repair Clovis &amp; Fresno",
                   "Learn about Prime Appliance Repair Services — serving Fresno and Clovis since 2009. Expert, honest, reliable appliance repair.",
                   "https://appliancerepairclovis.com/about-us/")
    content += navbar("about")
    content += inner_hero(
        "About Us",
        "Appliance Repair <span class='hi'>Built on Trust</span>",
        "We've been working in appliance repair since 2009, starting small and growing steadily by doing one thing well: honest work, done right.",
        hero_btns("Book Online", "/Prime-Clovis/book-an-appointment/", f"Call {PHONE}", f"tel:{PHONE_RAW}")
    )
    content += breadcrumb([("Home","/Prime-Clovis/"),("About Us","")])
    content += """
<div class="section-outer">
<div class="section-box">
  <div style="text-align:center;margin-bottom:48px;">
    <div class="section-badge"><svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/></svg>Our Story</div>
    <h2 class="section-title">From a Local Shop to a Trusted Name</h2>
    <p class="section-sub">We started with a simple promise — fast, honest appliance repair — and that hasn't changed since day one.</p>
  </div>
  <div class="content-wrap">
    <div class="prose">
      <p>We've been working in appliance repair since 2009, starting small and growing steadily over the years. What began as a local service has expanded into a trusted company serving homeowners across Fresno, Clovis, Madera, and surrounding areas. Most of our growth has come from word of mouth — customers who appreciate honest service and reliable results.</p>
      <p>From day one, we've focused on a few simple things: being honest with our customers, responding quickly, doing quality work, and standing behind every job. We believe repairs should be done right the first time, with clear communication and no unnecessary upselling.</p>
      <p>Today, we handle a full range of services, including appliance repair, installation, and routine maintenance. When you choose us, you're not just getting a repair service — you're working with a team that genuinely cares about keeping your home running smoothly.</p>
    </div>
    <div>"""
    content += """
      <div class="stats-bar" style="flex-direction:column;gap:24px;padding:32px 24px;">
        <div class="stat-item"><div class="stat-num">15<em>+</em></div><div class="stat-lbl">Years Experience</div></div>
        <div class="stat-div" style="width:60px;height:1px;"></div>
        <div class="stat-item"><div class="stat-num">54<em>k+</em></div><div class="stat-lbl">Repairs Completed</div></div>
        <div class="stat-div" style="width:60px;height:1px;"></div>
        <div class="stat-item"><div class="stat-num">5.0<em>★</em></div><div class="stat-lbl">Average Rating</div></div>
      </div>
    </div>
  </div>
</div>
</div>

<div class="section-outer">
<div class="section-box">
  <div style="text-align:center;margin-bottom:40px;">
    <div class="section-badge"><svg viewBox="0 0 24 24"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/></svg>Why Choose Us</div>
    <h2 class="section-title">What Sets Us Apart</h2>
    <p class="section-sub">Six reasons homeowners in Fresno and Clovis call us first — and keep coming back.</p>
  </div>"""
    content += why_cards()
    content += """
</div>
</div>

<div class="section-outer">
<div class="section-box">
  <div style="text-align:center;margin-bottom:40px;">
    <div class="section-badge"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>Our Process</div>
    <h2 class="section-title">How We Work</h2>
    <p class="section-sub">A straightforward process designed around your time and your peace of mind.</p>
  </div>
  <div class="process-grid">"""
    steps = [
        ("01","No Service Call Fee","We waive the service call fee completely when you move forward with the repair. You only pay for the work done."),
        ("02","Upfront Quote","You'll know the full cost before we touch a single part. Clear, honest, no surprises."),
        ("03","Quality Repair","We use OEM and manufacturer-approved parts and complete the job right the first time."),
        ("04","Warranty Included","Every repair comes with a warranty on both parts and labor for your peace of mind."),
        ("05","Clean &amp; Professional","Technicians arrive in uniform, respect your home, and clean up completely after every job."),
        ("06","Follow-Up","We follow up to make sure everything is working perfectly after the repair."),
    ]
    for num, title, desc in steps:
        content += f"""
    <div style="background:#fff;border:1px solid #e5e7eb;border-radius:14px;padding:28px 22px;">
      <div style="font-size:32px;font-weight:900;color:#d4f000;line-height:1;margin-bottom:12px;">{num}</div>
      <h4 style="font-size:16px;font-weight:800;color:#2b3340;margin:0 0 8px;">{title}</h4>
      <p style="font-size:13px;color:#6b7280;line-height:1.7;margin:0;">{desc}</p>
    </div>"""
    content += """
  </div>
</div>
</div>"""
    content += cta_banner()
    content += booking_section()
    content += footer()
    write_page(f"{BASE}/about-us/index.html", content)


# ── SERVICES ────────────────────────────────────────────────────
def build_services():
    content = head("Appliance Repair Services | Prime Appliance Repair Clovis &amp; Fresno",
                   "Professional appliance repair services in Clovis and Fresno. We repair refrigerators, washers, dryers, ovens, dishwashers & more. Call (559) 765-0303.",
                   "https://appliancerepairclovis.com/services/")
    content += navbar("services")
    content += inner_hero(
        "Our Services",
        "Professional Appliance Repair <span class='hi'>For Every Home</span>",
        "We repair all major household appliances — fast, reliable service with warranty on parts and labor. Same-day appointments available throughout Fresno and Clovis.",
        hero_btns()
    )
    content += breadcrumb([("Home","/Prime-Clovis/"),("Services","")])

    services_data = [
        ("🧊", "Refrigerator Repair", "refrigerator-repair-clovis-ca",
         "Keep your food fresh with expert refrigerator repair.",
         ["Not cooling or too warm","Ice maker not working","Water dispenser issues","Frost buildup in freezer","Compressor problems","Water leaking inside","Strange noises or vibrations"]),
        ("🫧", "Washer Repair", "washer-repair-clovis-ca",
         "Get your laundry routine back on track — fast.",
         ["Won't spin or agitate","Water not draining","Leaking on the floor","Won't start or power on","Loud banging or grinding","Not filling with water","Shaking excessively during cycle"]),
        ("🌀", "Dryer Repair", "dryer-repair-clovis-ca",
         "Efficient dryer repair to get clothes dry and ready fast.",
         ["Not heating or drying clothes","Takes too long to dry","Won't start or turn on","Squeaking or thumping sounds","Drum not turning","Burning smell during use","Door won't close properly"]),
        ("🍽️", "Dishwasher Repair", "dishwasher-repair-clovis-ca",
         "Clean dishes every time with expert dishwasher service.",
         ["Not cleaning dishes properly","Water not draining","Leaking underneath","Won't fill with water","Not drying dishes","Strange noises during wash","Door latch broken"]),
        ("🔥", "Oven &amp; Range Repair", "oven-repair-clovis-ca",
         "Get back to cooking with professional oven and range repairs.",
         ["Not heating or heating unevenly","Burners not igniting","Oven door won't close","Temperature inaccurate","Self-cleaning not working","Gas smell or ignition issues","Control panel errors"]),
        ("📡", "Microwave Repair", "microwave-repair-clovis-ca",
         "Quick and safe microwave repairs for convenient meal prep.",
         ["Not heating food","Turntable not spinning","Sparking inside","Door not closing properly","Control panel not responding","Loud humming noise","Display not working"]),
        ("🔩", "Stove Repair", "stove-repair-clovis-ca",
         "Professional stove repair for gas and electric models.",
         ["Burners won't light or heat","Uneven heating","Igniter problems","Gas smell","Coil element failure","Electronic controls failing","Knob and dial issues"]),
        ("❄️", "Freezer Repair", "freezer-repair-clovis-ca",
         "Keep frozen food safe with reliable freezer repairs.",
         ["Not freezing properly","Excessive frost or ice buildup","Temperature fluctuating","Strange noises","Door seal issues","Compressor problems","Water leaking"]),
        ("🍷", "Wine Cooler Repair", "wine-cooler-repair-clovis-ca",
         "Protect your wine collection with expert cooler service.",
         ["Not cooling properly","Temperature inconsistent","Compressor issues","Condensation inside","Door seal problems","Control panel failure","Strange noises"]),
        ("🧊", "Ice Maker Repair", "ice-maker-repair-clovis-ca",
         "Never run out of ice — fast ice maker repair service.",
         ["Not making ice","Ice cubes too small or malformed","Water leaking","Dispenser not working","Strange taste or odor","Ice maker jammed","Electrical issues"]),
        ("⚙️", "Garbage Disposal Repair", "garbage-disposal-repair-clovis-ca",
         "Keep your kitchen sink running smoothly.",
         ["Not turning on or just humming","Jammed or stuck","Leaking underneath","Loud grinding noises","Not draining properly","Reset button keeps tripping","Foul odors"]),
    ]

    content += """
<div class="section-outer">
<div class="section-box">
  <div style="text-align:center;margin-bottom:44px;">
    <div class="section-badge"><svg viewBox="0 0 24 24"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg>Appliance Services</div>
    <h2 class="section-title">Every Appliance. Every Brand.</h2>
    <p class="section-sub">From refrigerators to garbage disposals, we repair them all with certified technicians and quality parts.</p>
  </div>
  <div style="display:flex;flex-direction:column;gap:20px;">"""

    for icon, name, slug, tagline, issues in services_data:
        issues_html = "".join(f"<li>{i}</li>" for i in issues)
        content += f"""
    <div style="background:#fff;border:1px solid #dde2e8;border-radius:16px;padding:32px;">
      <div style="display:flex;align-items:flex-start;gap:20px;">
        <div style="font-size:36px;flex-shrink:0;margin-top:4px;">{icon}</div>
        <div style="flex:1;">
          <h3 style="font-size:20px;font-weight:800;color:#2b3340;margin:0 0 8px;">{name}</h3>
          <p style="font-size:14px;color:#6b7280;margin:0 0 16px;">{tagline}</p>
          <ul style="display:grid;grid-template-columns:repeat(2,1fr);gap:6px 20px;list-style:none;padding:0;margin:0 0 20px;">{issues_html}</ul>
          <a href="/Prime-Clovis/{slug}/" style="display:inline-flex;align-items:center;gap:6px;background:#2b3340;color:#fff;font-size:14px;font-weight:700;padding:10px 20px;border-radius:8px;text-decoration:none;transition:background .2s;">Learn More →</a>
        </div>
      </div>
    </div>"""

    content += """
  </div>
</div>
</div>"""
    content += """
<div class="section-outer">
<div class="section-box">
  <div style="text-align:center;margin-bottom:40px;">
    <div class="section-badge"><svg viewBox="0 0 24 24"><polyline points="9 11 12 14 22 4"/></svg>Why Choose Us</div>
    <h2 class="section-title">Why Homeowners Choose Prime</h2>
    <p class="section-sub">Certified technicians, honest pricing, and repairs backed by a warranty.</p>
  </div>"""
    content += why_cards()
    content += """
</div>
</div>"""
    content += cta_banner()
    content += booking_section()
    content += footer()
    write_page(f"{BASE}/services/index.html", content)


# ── CONTACT US ──────────────────────────────────────────────────
def build_contact():
    content = head("Contact Us | Prime Appliance Repair Clovis &amp; Fresno",
                   f"Contact Prime Appliance Repair Services. Call {PHONE} or book online. Serving Fresno, Clovis &amp; surrounding areas.",
                   "https://appliancerepairclovis.com/contact-us/")
    content += navbar()
    content += inner_hero(
        "Contact Us",
        "We're Ready to <span class='hi'>Help You Today</span>",
        "Where broken appliances meet their match. Reach out by phone, email, or WhatsApp — we respond fast.",
        hero_btns(f"Call {PHONE}", f"tel:{PHONE_RAW}", "Book Online", "/Prime-Clovis/book-an-appointment/")
    )
    content += breadcrumb([("Home","/Prime-Clovis/"),("Contact Us","")])
    content += f"""
<div class="section-outer">
<div class="section-box">
  <div style="display:grid;grid-template-columns:1fr 420px;gap:52px;align-items:start;">
    <div>
      <div class="section-badge" style="margin-bottom:18px;"><svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 10.8 19.79 19.79 0 010 2.18 2 2 0 012 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 14.92z"/></svg>Get In Touch</div>
      <h2 class="section-title">Let's Talk</h2>
      <p style="font-size:15px;color:#6b7280;line-height:1.75;margin-bottom:32px;">We service Fresno, Clovis, and surrounding areas. We work with all major appliance brands and we're here to make the repair process smooth and stress-free.</p>
      <div style="display:flex;flex-direction:column;gap:20px;">
        <div style="display:flex;align-items:flex-start;gap:16px;background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:18px 20px;">
          <div style="width:40px;height:40px;border-radius:10px;background:rgba(212,240,0,.15);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
            <svg viewBox="0 0 24 24" width="18" height="18" style="stroke:#2b3340;fill:none;stroke-width:2;"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 10.8 19.79 19.79 0 010 2.18 2 2 0 012 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 14.92z"/></svg>
          </div>
          <div><div style="font-size:12px;font-weight:700;color:#9ca3af;text-transform:uppercase;letter-spacing:.8px;margin-bottom:4px;">Phone</div><a href="tel:{PHONE_RAW}" style="font-size:17px;font-weight:800;color:#2b3340;text-decoration:none;">{PHONE}</a></div>
        </div>
        <div style="display:flex;align-items:flex-start;gap:16px;background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:18px 20px;">
          <div style="width:40px;height:40px;border-radius:10px;background:rgba(68,81,98,.10);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
            <svg viewBox="0 0 24 24" width="18" height="18" style="stroke:#2b3340;fill:none;stroke-width:2;"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
          </div>
          <div><div style="font-size:12px;font-weight:700;color:#9ca3af;text-transform:uppercase;letter-spacing:.8px;margin-bottom:4px;">Email</div><a href="mailto:{EMAIL}" style="font-size:15px;font-weight:700;color:#2b3340;text-decoration:none;">{EMAIL}</a></div>
        </div>
        <div style="display:flex;align-items:flex-start;gap:16px;background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:18px 20px;">
          <div style="width:40px;height:40px;border-radius:10px;background:rgba(37,211,102,.12);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
            <svg viewBox="0 0 24 24" width="18" height="18" style="stroke:#2b3340;fill:none;stroke-width:2;"><path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z"/></svg>
          </div>
          <div><div style="font-size:12px;font-weight:700;color:#9ca3af;text-transform:uppercase;letter-spacing:.8px;margin-bottom:4px;">WhatsApp</div><a href="https://wa.me/message/7XVFDXQTK2XSP1" target="_blank" style="font-size:15px;font-weight:700;color:#2b3340;text-decoration:none;">Click to Chat</a></div>
        </div>
        <div style="display:flex;align-items:flex-start;gap:16px;background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:18px 20px;">
          <div style="width:40px;height:40px;border-radius:10px;background:rgba(68,81,98,.08);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
            <svg viewBox="0 0 24 24" width="18" height="18" style="stroke:#2b3340;fill:none;stroke-width:2;"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          </div>
          <div><div style="font-size:12px;font-weight:700;color:#9ca3af;text-transform:uppercase;letter-spacing:.8px;margin-bottom:4px;">Hours</div><span style="font-size:15px;font-weight:700;color:#2b3340;">Mon–Sat: 7:00 AM – 7:00 PM</span></div>
        </div>
        <div style="display:flex;align-items:flex-start;gap:16px;background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:18px 20px;">
          <div style="width:40px;height:40px;border-radius:10px;background:rgba(239,68,68,.08);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
            <svg viewBox="0 0 24 24" width="18" height="18" style="stroke:#2b3340;fill:none;stroke-width:2;"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
          </div>
          <div><div style="font-size:12px;font-weight:700;color:#9ca3af;text-transform:uppercase;letter-spacing:.8px;margin-bottom:4px;">Service Area</div><span style="font-size:15px;font-weight:700;color:#2b3340;">Fresno, Clovis, Madera, Sanger, Fowler, Friant</span></div>
        </div>
      </div>
    </div>
    <div>
      <div style="background:#fff;border:1px solid #e5e7eb;border-radius:16px;padding:36px;">
        <h3 style="font-size:20px;font-weight:800;color:#2b3340;margin:0 0 6px;">Send Us a Message</h3>
        <p style="font-size:13px;color:#6b7280;margin:0 0 24px;">We'll get back to you as soon as possible.</p>
        <form id="bookingForm">
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px;">
            <div class="bf-group"><label>First Name</label><input type="text" name="fname" placeholder="John" required></div>
            <div class="bf-group"><label>Last Name</label><input type="text" name="lname" placeholder="Smith"></div>
          </div>
          <div class="bf-group" style="margin-bottom:14px;"><label>Phone Number</label><input type="tel" name="phone" placeholder="(559) 000-0000" required></div>
          <div class="bf-group" style="margin-bottom:14px;"><label>Email</label><input type="email" name="email" placeholder="john@email.com"></div>
          <div class="bf-group" style="margin-bottom:14px;"><label>Appliance Type</label>
            <select name="appliance">
              <option value="">Select appliance...</option>
              <option>Refrigerator</option><option>Washer</option><option>Dryer</option>
              <option>Dishwasher</option><option>Oven / Range</option><option>Microwave</option>
              <option>Freezer</option><option>Other</option>
            </select>
          </div>
          <div class="bf-group" style="margin-bottom:14px;"><label>Describe the Issue</label><textarea name="issue" placeholder="Tell us what's happening with your appliance..." required></textarea></div>
          <button type="submit" class="bf-submit" style="width:100%;justify-content:center;">
            <svg viewBox="0 0 24 24"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
            Send Message
          </button>
        </form>
        <div id="formMsg" class="form-msg"></div>
      </div>
    </div>
  </div>
</div>
</div>"""
    content += cta_banner()
    content += footer()
    write_page(f"{BASE}/contact-us/index.html", content)


# ── BOOK APPOINTMENT ────────────────────────────────────────────
def build_book():
    content = head("Book an Appointment | Prime Appliance Repair Clovis",
                   f"Book your appliance repair appointment online. Quick and easy — fill in your details and we'll confirm same-day. Call {PHONE}.",
                   "https://appliancerepairclovis.com/book-an-appointment/")
    content += navbar()
    content += inner_hero(
        "Book Online",
        "Schedule Your <span class='hi'>Appliance Repair</span>",
        "Quick and easy — fill in your details and our team will contact you as soon as possible to confirm your appointment time.",
        trust=False
    )
    content += breadcrumb([("Home","/Prime-Clovis/"),("Book an Appointment","")])
    content += f"""
<div class="section-outer">
<div class="section-box">
  <div style="display:grid;grid-template-columns:1fr 300px;gap:52px;align-items:start;">
    <div>
      <h2 class="section-title" style="margin-bottom:8px;">Schedule Your Repair</h2>
      <p style="font-size:15px;color:#6b7280;margin:0 0 32px;line-height:1.7;">Fill out the form below and we'll reach out to confirm your appointment time. Same-day and next-day scheduling available.</p>
      <div style="background:#fff;border:1px solid #e5e7eb;border-radius:16px;padding:36px;">
        <form id="bookingForm">
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px;">
            <div class="bf-group"><label>First Name *</label><input type="text" name="fname" placeholder="John" required></div>
            <div class="bf-group"><label>Last Name *</label><input type="text" name="lname" placeholder="Smith" required></div>
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px;">
            <div class="bf-group"><label>Phone Number *</label><input type="tel" name="phone" placeholder="(559) 000-0000" required></div>
            <div class="bf-group"><label>Email Address</label><input type="email" name="email" placeholder="john@email.com"></div>
          </div>
          <div class="bf-group" style="margin-bottom:14px;"><label>Service Address *</label><input type="text" name="address" placeholder="123 Main St, Clovis, CA" required></div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px;">
            <div class="bf-group"><label>Appliance Type *</label>
              <select name="appliance" required>
                <option value="">Select appliance...</option>
                <option>Refrigerator</option><option>Washer</option><option>Dryer</option>
                <option>Dishwasher</option><option>Oven / Range</option><option>Microwave</option>
                <option>Freezer</option><option>Wine Cooler</option><option>Ice Maker</option>
                <option>Garbage Disposal</option><option>Other</option>
              </select>
            </div>
            <div class="bf-group"><label>Appliance Brand</label><input type="text" name="brand" placeholder="e.g. Samsung, Whirlpool, LG..."></div>
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px;">
            <div class="bf-group"><label>Preferred Date</label><input type="date" name="date"></div>
            <div class="bf-group"><label>Preferred Time</label>
              <select name="time">
                <option value="">Any time</option>
                <option>Morning (7 AM – 12 PM)</option>
                <option>Afternoon (12 PM – 5 PM)</option>
                <option>Evening (5 PM – 7 PM)</option>
              </select>
            </div>
          </div>
          <div class="bf-group" style="margin-bottom:20px;"><label>Describe the Problem *</label><textarea name="issue" placeholder="Tell us what's happening with your appliance..." required></textarea></div>
          <button type="submit" class="bf-submit" style="width:100%;justify-content:center;font-size:15px;padding:15px;">
            <svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
            Book My Appointment
          </button>
        </form>
        <div id="formMsg" class="form-msg"></div>
        <p style="font-size:13px;color:#9ca3af;text-align:center;margin:16px 0 0;">Or call us directly: <a href="tel:{PHONE_RAW}" style="color:#2b3340;font-weight:700;">{PHONE}</a></p>
      </div>
    </div>
    <div class="sidebar">
      <div class="sidebar-cta">
        <h4>Prefer to Call?</h4>
        <p>Talk to our team directly and schedule your appointment in minutes.</p>
        <a href="tel:{PHONE_RAW}" class="sidebar-btn-primary">&#x260E; {PHONE}</a>
        <a href="https://wa.me/message/7XVFDXQTK2XSP1" target="_blank" class="sidebar-btn-secondary">WhatsApp Us</a>
      </div>
      <div class="sidebar-links">
        <h5>What Happens Next?</h5>
        <ul>
          <li><a href="#">1. We review your request</a></li>
          <li><a href="#">2. We call to confirm the time</a></li>
          <li><a href="#">3. Technician arrives at your home</a></li>
          <li><a href="#">4. Diagnosis &amp; upfront quote — service call fee waived if you repair</a></li>
          <li><a href="#">5. Repair is completed same visit</a></li>
        </ul>
      </div>
      <div class="sidebar-links">
        <h5>Why Book With Us?</h5>
        <ul>
          <li><a href="#">Same-day &amp; next-day scheduling</a></li>
          <li><a href="#">Upfront pricing — no surprises</a></li>
          <li><a href="#">Warranty on parts &amp; labor</a></li>
          <li><a href="#">Certified technicians</a></li>
          <li><a href="#">All major brands serviced</a></li>
        </ul>
      </div>
    </div>
  </div>
</div>
</div>"""
    content += cta_banner()
    content += footer()
    write_page(f"{BASE}/book-an-appointment/index.html", content)
    # Also write book-appointment (alias)
    write_page(f"{BASE}/book-appointment/index.html", content)


# ── BLOG LISTING ────────────────────────────────────────────────
BLOG_POSTS = [
    {
        "slug": "your-fridge-is-lying-to-you",
        "title": "Your Fridge Is Lying to You",
        "cat": "Appliance Problems & Fixes",
        "cat_slug": "appliance-problems-fixes",
        "date": "April 18, 2026",
        "read": "4 min read",
        "img": "https://appliancerepairclovis.com/wp-content/uploads/2026/04/vecteezy_woman-looking-disappointed-at-an-empty-fridge-feeling_69408907.jpg",
        "excerpt": "It looks fine. The light turns on. It hums. But your fridge may be quietly failing — here's how to tell before food spoils or your energy bill spikes.",
    },
    {
        "slug": "appliance-repair-cost-guide",
        "title": "Appliance Repair Cost Guide: What to Expect",
        "cat": "Repair Cost Guides",
        "cat_slug": "repair-cost-guides",
        "date": "April 16, 2026",
        "read": "5 min read",
        "img": "https://appliancerepairclovis.com/wp-content/uploads/2026/04/vecteezy_technician-or-worker-in-uniform-installs-dishwasher-into-the_35202703-1.jpg",
        "excerpt": "What does appliance repair cost in 2026? An honest breakdown of typical repair costs for refrigerators, washers, dryers, ovens, and more.",
    },
    {
        "slug": "when-everything-still-works-but-somethings-clearly-wrong",
        "title": "When Everything 'Still Works'… But Something's Clearly Wrong",
        "cat": "Appliance Problems & Fixes",
        "cat_slug": "appliance-problems-fixes",
        "date": "April 11, 2026",
        "read": "3 min read",
        "img": "https://appliancerepairclovis.com/wp-content/uploads/2026/04/9652c7398ec0b54a986526ec323ce798.jpg",
        "excerpt": "There's a moment every homeowner hits. The appliance is technically still running, but something's clearly off. Here's what those signs mean.",
    },
    {
        "slug": "why-your-dryer-takes-too-long-to-dry-clothes",
        "title": "Why Your Dryer Takes Too Long to Dry Clothes",
        "cat": "Maintenance & Insider Tips",
        "cat_slug": "maintenance-insider-tips",
        "date": "April 11, 2026",
        "read": "3 min read",
        "img": "https://appliancerepairclovis.com/wp-content/uploads/2026/04/WhatsApp-Image-2026-02-24-at-23.54.01.jpeg",
        "excerpt": "If your dryer is running full cycles but clothes still come out damp, something isn't working the way it should. Here's what to check first.",
    },
    {
        "slug": "washer-maintenance-tips-most-people-ignore",
        "title": "Washer Maintenance Tips Most People Ignore",
        "cat": "Maintenance & Insider Tips",
        "cat_slug": "maintenance-insider-tips",
        "date": "April 11, 2026",
        "read": "3 min read",
        "img": "https://appliancerepairclovis.com/wp-content/uploads/2026/04/WhatsApp-Image-2026-03-21-at-22.45.04-2.jpeg",
        "excerpt": "Most people don't think about maintaining their washer until something goes wrong. These simple tips can add years to its life.",
    },
    {
        "slug": "repair-vs-replace",
        "title": "Repair vs. Replace: How to Make the Right Call",
        "cat": "Repair Cost Guides",
        "cat_slug": "repair-cost-guides",
        "date": "April 3, 2026",
        "read": "5 min read",
        "img": "https://appliancerepairclovis.com/wp-content/uploads/2026/04/vecteezy_senior-technician-fixing-dishwasher-at-kitchen_42863819.jpg",
        "excerpt": "Should you repair your broken appliance or replace it? Use this practical framework — including the 50% rule — to make the smart decision.",
    },
]

def build_blog():
    content = head("Blog | Prime Appliance Repair Clovis",
                   "Tips, guides, and news to help you keep your appliances running at their best. From Prime Appliance Repair Services.",
                   "https://appliancerepairclovis.com/blog-2/")
    content += navbar("blog")
    content += inner_hero(
        "Our Blog",
        "Appliance Tips &amp; <span class='hi'>Repair Guides</span>",
        "Practical advice to help you keep your appliances running longer, catch problems early, and know when to call a pro.",
        trust=False
    )
    content += breadcrumb([("Home","/Prime-Clovis/"),("Blog","")])

    cat_pills = [
        ("All Posts", "/Prime-Clovis/blog-2/", True),
        ("Appliance Problems & Fixes", "/Prime-Clovis/category/appliance-problems-fixes/", False),
        ("Repair Cost Guides", "/Prime-Clovis/category/repair-cost-guides/", False),
        ("Maintenance & Tips", "/Prime-Clovis/category/maintenance-insider-tips/", False),
    ]
    pills_html = ""
    for label, href, active in cat_pills:
        if active:
            pills_html += f'<a href="{href}" style="display:inline-block;padding:8px 20px;background:#2b3340;color:#fff;border-radius:20px;font-size:13px;font-weight:600;text-decoration:none;">{label}</a>'
        else:
            pills_html += f'<a href="{href}" style="display:inline-block;padding:8px 20px;background:#fff;color:#5a6472;border:1px solid #dde2e8;border-radius:20px;font-size:13px;text-decoration:none;transition:all .2s;">{label}</a>'

    content += f"""
<div class="section-outer">
<div class="section-box">
  <div style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:36px;">{pills_html}</div>
  <div class="blog-grid">"""

    for post in BLOG_POSTS:
        content += f"""
    <a href="/Prime-Clovis/{post['slug']}/" class="blog-card">
      <div class="blog-thumb">
        <img src="{post['img']}" alt="{post['title']}" loading="lazy">
        <span class="blog-cat-pill">{post['cat']}</span>
      </div>
      <div class="blog-body">
        <div class="blog-meta">
          <span><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>{post['date']}</span>
          <span><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>{post['read']}</span>
        </div>
        <h3 class="blog-card-title">{post['title']}</h3>
        <p class="blog-card-excerpt">{post['excerpt']}</p>
        <span class="blog-readmore">Read More <svg viewBox="0 0 24 24"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></span>
      </div>
    </a>"""

    content += """
  </div>
</div>
</div>"""
    content += cta_banner()
    content += booking_section()
    content += footer()
    write_page(f"{BASE}/blog-2/index.html", content)


# ── CATEGORY PAGES ──────────────────────────────────────────────
def build_categories():
    cats = [
        ("appliance-problems-fixes", "Appliance Problems & Fixes",
         "In-depth guides on diagnosing and understanding common appliance issues."),
        ("repair-cost-guides", "Repair Cost Guides",
         "Honest breakdowns of what appliance repairs actually cost in 2026."),
        ("maintenance-insider-tips", "Maintenance & Insider Tips",
         "Pro tips to extend the life of your appliances and avoid costly repairs."),
    ]
    for slug, title, desc in cats:
        filtered = [p for p in BLOG_POSTS if p["cat_slug"] == slug]
        all_posts = filtered if filtered else BLOG_POSTS  # fallback
        content = head(f"{title} | Prime Appliance Repair Blog",
                       desc, f"https://appliancerepairclovis.com/category/{slug}/")
        content += navbar("blog")
        content += inner_hero("Blog Category", f"<span class='hi'>{title}</span>", desc, trust=False)
        content += breadcrumb([("Home","/Prime-Clovis/"),("Blog","/Prime-Clovis/blog-2/"),(title,"")])
        content += f"""
<div class="section-outer">
<div class="section-box">
  <div class="blog-grid">"""
        for post in all_posts:
            content += f"""
    <a href="/Prime-Clovis/{post['slug']}/" class="blog-card">
      <div class="blog-thumb">
        <img src="{post['img']}" alt="{post['title']}" loading="lazy">
        <span class="blog-cat-pill">{post['cat']}</span>
      </div>
      <div class="blog-body">
        <div class="blog-meta">
          <span><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>{post['date']}</span>
          <span><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>{post['read']}</span>
        </div>
        <h3 class="blog-card-title">{post['title']}</h3>
        <p class="blog-card-excerpt">{post['excerpt']}</p>
        <span class="blog-readmore">Read More <svg viewBox="0 0 24 24"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></span>
      </div>
    </a>"""
        content += """
  </div>
</div>
</div>"""
        content += cta_banner()
        content += footer()
        write_page(f"{BASE}/category/{slug}/index.html", content)


# ── BLOG POSTS ──────────────────────────────────────────────────
def build_blog_post_shell(post, body_html):
    other_posts = [p for p in BLOG_POSTS if p["slug"] != post["slug"]][:3]
    content = head(f"{post['title']} | Prime Appliance Repair Clovis",
                   post["excerpt"],
                   f"https://appliancerepairclovis.com/{post['slug']}/")
    content += navbar("blog")
    content += f"""
<section class="post-hero">
  <div class="post-hero-inner">
    <div class="breadcrumb-inner" style="margin-bottom:16px;padding:0;">
      <a href="/Prime-Clovis/" style="font-size:12px;color:rgba(255,255,255,.5);text-decoration:none;">Home</a>
      <span class="sep" style="color:rgba(255,255,255,.3);">›</span>
      <a href="/Prime-Clovis/blog-2/" style="font-size:12px;color:rgba(255,255,255,.5);text-decoration:none;">Blog</a>
      <span class="sep" style="color:rgba(255,255,255,.3);">›</span>
      <span style="font-size:12px;color:rgba(255,255,255,.7);">{post['title']}</span>
    </div>
    <span class="post-cat-pill">{post['cat']}</span>
    <h1>{post['title']}</h1>
    <div class="post-meta">
      <span style="display:flex;align-items:center;gap:5px;"><svg viewBox="0 0 24 24" width="13" height="13" style="stroke:rgba(255,255,255,.6);fill:none;stroke-width:2;"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>{post['date']}</span>
      <span style="display:flex;align-items:center;gap:5px;"><svg viewBox="0 0 24 24" width="13" height="13" style="stroke:rgba(255,255,255,.6);fill:none;stroke-width:2;"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>{post['read']}</span>
      <span style="display:flex;align-items:center;gap:5px;"><svg viewBox="0 0 24 24" width="13" height="13" style="stroke:rgba(255,255,255,.6);fill:none;stroke-width:2;"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg>Prime Appliance Repair</span>
    </div>
    <img class="post-hero-img" src="{post['img']}" alt="{post['title']}">
  </div>
</section>

<div class="post-layout">
  <article class="post-content">
    {body_html}
  </article>
  <aside class="post-sidebar">
    <div class="sidebar-cta">
      <h4>Need a Repair?</h4>
      <p>Our certified technicians are ready to help — same-day service available.</p>
      <a href="/Prime-Clovis/book-an-appointment/" class="sidebar-btn-primary">Book Appointment</a>
      <a href="tel:{PHONE_RAW}" class="sidebar-btn-secondary">&#x260E; {PHONE}</a>
    </div>
    <div class="sidebar-links">
      <h5>Our Services</h5>
      <ul>
        <li><a href="/Prime-Clovis/refrigerator-repair-clovis-ca/">Refrigerator Repair</a></li>
        <li><a href="/Prime-Clovis/washer-repair-clovis-ca/">Washer Repair</a></li>
        <li><a href="/Prime-Clovis/dryer-repair-clovis-ca/">Dryer Repair</a></li>
        <li><a href="/Prime-Clovis/dishwasher-repair-clovis-ca/">Dishwasher Repair</a></li>
        <li><a href="/Prime-Clovis/oven-repair-clovis-ca/">Oven &amp; Range Repair</a></li>
        <li><a href="/Prime-Clovis/microwave-repair-clovis-ca/">Microwave Repair</a></li>
      </ul>
    </div>
    <div class="sidebar-links">
      <h5>Related Articles</h5>
      <ul>"""
    for op in other_posts:
        content += f'<li><a href="/Prime-Clovis/{op["slug"]}/">{op["title"]}</a></li>'
    content += f"""
      </ul>
    </div>
  </aside>
</div>"""
    content += cta_banner()
    content += booking_section()
    content += footer()
    write_page(f"{BASE}/{post['slug']}/index.html", content)


def build_blog_posts():
    # ── Post 1: Fridge ──
    build_blog_post_shell(BLOG_POSTS[0], """
<p>It looks fine. The light turns on. It makes noise. It's cold… kind of. So you don't think about it much — until you do. Maybe it's that yogurt that went bad two days early, or the fact that your electric bill crept up without explanation. Your refrigerator might be quietly failing, and it's doing a surprisingly good job of hiding it.</p>
<h2>The Subtle Signs Your Fridge Is Lying</h2>
<p>Refrigerators rarely die suddenly. More often, they decline slowly — and the warning signs are easy to dismiss until they're not.</p>
<h3>Your Food Isn't Lasting as Long as It Should</h3>
<p>This is one of the most overlooked signs. If produce is wilting faster, leftovers are going bad sooner, or your milk expires before the date on the carton, your fridge may not be holding temperature properly. The interior might read 38°F on a thermometer, but temperature swings — especially near the door — can cause accelerated spoilage without ever triggering the low-temp alarm.</p>
<h3>The Motor Runs Constantly</h3>
<p>Your fridge should cycle on and off. If it seems like the compressor never stops running, that's a red flag. It might mean the door seal is letting in warm air, the condenser coils are coated in dust, or the refrigerant level is low. The unit is working overtime to maintain temperature — and that shows up on your energy bill.</p>
<div class="callout"><p>💡 A refrigerator that runs constantly can add $10–$30/month to your electricity bill without you noticing.</p></div>
<h3>There's Condensation or Ice in the Wrong Places</h3>
<p>Moisture on the outside of the fridge, especially around the door, often means the door gasket is worn out. Frost buildup inside the freezer compartment when it should be frost-free points to a defrost system issue. Water pooling on the bottom of the fridge interior usually means a clogged defrost drain.</p>
<h3>You Hear Sounds You Haven't Heard Before</h3>
<p>Clicking, buzzing, hissing, or knocking are all sounds worth paying attention to. Some noise is normal — the compressor cycling, water lines filling the ice maker — but new or loud noises usually mean a component is under stress or failing.</p>
<h2>What to Do Next</h2>
<p>If any of these describe your fridge right now, don't wait until the food is ruined and you're scrambling. Call or book online and we'll diagnose the issue the same day. Most refrigerator problems — door seals, defrost systems, condenser cleaning — are straightforward fixes that cost far less than a new appliance.</p>
<p>The longer you wait with refrigerator issues, the more it costs — in food waste, energy, and eventual repairs. Your fridge may look fine right now. But if it's lying to you, we'll find out.</p>
""")

    # ── Post 2: Cost Guide ──
    build_blog_post_shell(BLOG_POSTS[1], """
<p>One of the first questions people ask when an appliance breaks is: "How much does appliance repair cost?" It's a fair question, and it deserves an honest answer — not a runaround.</p>
<p>The truth is that repair costs vary quite a bit depending on the appliance, the specific issue, the parts needed, and who does the work. But there are realistic ranges you can use to set expectations.</p>
<h2>Typical Appliance Repair Costs in 2026</h2>
<table>
  <thead><tr><th>Appliance</th><th>Common Repair</th><th>Typical Range</th></tr></thead>
  <tbody>
    <tr><td>Refrigerator</td><td>Door seal, defrost system, fan</td><td>$100–$350</td></tr>
    <tr><td>Washer</td><td>Pump, belt, lid switch, control board</td><td>$120–$380</td></tr>
    <tr><td>Dryer</td><td>Heating element, thermostat, drum belt</td><td>$100–$300</td></tr>
    <tr><td>Dishwasher</td><td>Pump, door latch, control board</td><td>$100–$300</td></tr>
    <tr><td>Oven / Range</td><td>Igniter, bake element, thermostat</td><td>$120–$350</td></tr>
    <tr><td>Microwave</td><td>Magnetron, door switch, fuse</td><td>$80–$250</td></tr>
  </tbody>
</table>
<p>These ranges include parts and labor for typical repairs. Complex issues like compressor replacement on a refrigerator or control board failure can run higher.</p>
<h2>What Affects the Final Price?</h2>
<ul>
  <li><strong>Parts availability:</strong> Common brand parts (Whirlpool, GE, LG) are usually cheaper and faster to source than specialty or European brands.</li>
  <li><strong>Appliance age:</strong> Older appliances may require parts that need to be ordered, adding time and cost.</li>
  <li><strong>Complexity:</strong> Some repairs require significant disassembly or take multiple hours — others are done in 20 minutes.</li>
  <li><strong>Brand:</strong> High-end brands like Sub-Zero, Viking, or Miele typically cost more to repair.</li>
</ul>
<h2>When Does Repair Make Sense vs. Replace?</h2>
<p>A common rule of thumb: if the repair costs more than 50% of the replacement cost, and the appliance is more than halfway through its expected lifespan, replacement is often the smarter move. But for appliances under 8–10 years old, repair almost always wins financially.</p>
<div class="callout"><p>💡 We always give you an upfront quote before any work begins. You never pay unless you approve the repair.</p></div>
<h2>Our Approach to Pricing</h2>
<p>We waive the service call fee when you choose to move forward with the repair. Our technician diagnoses your appliance, gives you a clear upfront quote, and if you approve the work, there's no separate visit charge on top of it. You pay for the repair — not the trip out.</p>
""")

    # ── Post 3: Still Works ──
    build_blog_post_shell(BLOG_POSTS[2], """
<p>There's a moment every homeowner hits. The appliance is technically still running — it powers on, it makes the right sounds, it sort of does what it's supposed to do. But something's clearly off. And you're not sure whether to call someone or just keep hoping it sorts itself out.</p>
<p>It usually doesn't sort itself out.</p>
<h2>The "It Still Works" Problem</h2>
<p>Appliances are designed to keep functioning even as their components degrade. Your dryer will still tumble clothes even after the heating element weakens. Your refrigerator will still run even as the door seal slowly fails. Your washer will still complete cycles even as the bearings start to go.</p>
<p>The problem is that these "still running" appliances often cause secondary damage — higher energy bills, food spoilage, water damage, or accelerated wear on other components.</p>
<h2>Signs Something's Actually Wrong</h2>
<ul>
  <li><strong>It takes longer than it used to:</strong> Dryer cycles stretching from 45 minutes to 90. Dishwasher running extra rinse cycles. Oven taking forever to preheat. These are performance drops worth paying attention to.</li>
  <li><strong>There's a new smell:</strong> Burning plastic, burnt rubber, mildew, or a faint gas smell — none of these are normal. Ever.</li>
  <li><strong>It needs more attention to work:</strong> Jiggling the door to close it, pressing the button multiple times to start, running it on a specific setting to avoid errors — these are symptoms, not just quirks.</li>
  <li><strong>Your energy bill crept up:</strong> An inefficient appliance is often an invisible one. If your bill has quietly risen without an obvious reason, your appliances might be working harder than they should.</li>
  <li><strong>It made a sound once — and you ignored it:</strong> A loud thump, a grinding noise, a pop. If you heard it and thought "that was weird" and moved on, we'd encourage you to move back and investigate.</li>
</ul>
<h2>Why "Wait and See" Costs More</h2>
<p>Small problems become big problems. A worn drum bearing becomes a broken drum. A slow water leak becomes a flooded floor. A weak heating element becomes a completely dead dryer — usually mid-cycle on laundry day.</p>
<div class="callout"><p>💡 Most repairs are significantly cheaper when caught early. Calling at the first sign of trouble almost always saves money.</p></div>
<h2>The Bottom Line</h2>
<p>If your gut says something's wrong with your appliance, your gut is probably right. Give us a call or book online — we'll come out, diagnose it honestly, and let you know whether it's a quick fix or something bigger. Either way, you'll know where you stand.</p>
""")

    # ── Post 4: Dryer ──
    build_blog_post_shell(BLOG_POSTS[3], """
<p>If your dryer is running full cycles but clothes still come out damp — or damp and hot, which is a special kind of frustrating — something isn't working right. Here's how to figure out what's actually going on.</p>
<h2>The Most Common Reasons</h2>
<h3>Clogged Lint Trap or Exhaust Vent</h3>
<p>This is the most common cause by far. The lint trap catches most of the debris, but lint also builds up in the vent duct that runs from your dryer to the outside of your home. A partially blocked vent restricts airflow — which means heat builds up, the dryer shuts off early via thermal protection, and clothes come out damp.</p>
<p>Check: Pull the dryer away from the wall, disconnect the duct, and look inside. If it's packed with lint, that's your answer. A professional duct cleaning every 1–2 years is strongly recommended.</p>
<h3>Weak or Failed Heating Element</h3>
<p>Electric dryers use a heating element that can burn out over time — often partially. A partially failed element still produces some heat, so the dryer runs warm but doesn't fully dry. Gas dryers use a gas valve and igniter, either of which can fail or weaken.</p>
<div class="callout"><p>💡 If your dryer runs but produces no heat at all, a failed heating element or igniter is the most likely cause.</p></div>
<h3>Faulty Thermostat or Thermal Fuse</h3>
<p>Your dryer uses thermostats to regulate temperature and a thermal fuse as a safety shutoff. If the cycling thermostat fails, the dryer may not heat consistently. If the thermal fuse has blown (often due to a previous vent blockage), the dryer may produce no heat at all.</p>
<h3>Overloaded Drum</h3>
<p>This one's simple: too many clothes. Overloading prevents clothes from tumbling freely, which means they don't dry evenly. Try a smaller load and see if the issue resolves itself.</p>
<h3>Worn or Broken Belt</h3>
<p>If the drum doesn't turn, clothes don't dry — even if the dryer heats. A broken drum belt is a common failure on older machines and is a relatively straightforward fix.</p>
<h2>When to Call a Technician</h2>
<p>If cleaning the lint trap and vent doesn't solve the problem, it's time to call. Thermostat and heating element replacement are standard repairs that usually take under an hour and cost far less than a new dryer. We service all major brands throughout Fresno and Clovis.</p>
""")

    # ── Post 5: Washer Maintenance ──
    build_blog_post_shell(BLOG_POSTS[4], """
<p>Most people don't think about maintaining their washer until something goes wrong. And by then, they've usually been ignoring small signs for months. These tips are simple, take almost no time, and can genuinely extend the life of your machine by years.</p>
<h2>1. Clean the Drum Monthly</h2>
<p>Detergent residue, fabric softener buildup, and hard water minerals accumulate inside the drum over time. This creates the perfect environment for mold and mildew — which is why some washers develop a persistent musty smell even after running a clean cycle.</p>
<p>Fix it: Run a hot water cycle with two cups of white vinegar (no clothes, no detergent) once a month. For front-loaders, follow up with a baking soda cycle. It takes ten minutes of your time and costs almost nothing.</p>
<h2>2. Leave the Door Open After Each Load</h2>
<p>This one's especially important for front-loading washers. When you close the door immediately after a wash, moisture gets trapped inside the drum and around the rubber gasket — and mold loves it there. Leaving the door open for even 30–60 minutes after a cycle makes a significant difference.</p>
<div class="callout"><p>💡 Mold in the door gasket of a front-load washer is one of the most common — and preventable — repair issues we see.</p></div>
<h2>3. Clean the Detergent Drawer</h2>
<p>Pull it out completely and rinse it under hot water. Detergent and fabric softener cake up in the drawer compartments over time, blocking the flow and affecting wash quality. Most drawers come out with a simple pull or button press.</p>
<h2>4. Don't Overload — Seriously</h2>
<p>Overloading puts stress on the drum bearings, the motor, and the suspension system. These are expensive components to replace. A good rule: if you can't easily fit your hand on top of the load, it's too full.</p>
<h2>5. Check the Fill Hoses Every Year</h2>
<p>The rubber hoses that connect your washer to the water supply can crack, bulge, or develop slow leaks over time. Look behind the machine once a year and check for any sign of moisture, staining, or deformation near the connections. Replacing hoses every 5–7 years is cheap insurance against a burst hose — which can cause serious water damage.</p>
<h2>6. Level the Machine</h2>
<p>An unlevel washer shakes excessively during the spin cycle, which wears out the drum bearings faster and is annoying enough that neighbors will mention it. Use a level and adjust the feet at the base of the machine until it sits flat.</p>
<h2>When Maintenance Isn't Enough</h2>
<p>If your washer is already showing signs of trouble — loud noises, poor drainage, leaks, or error codes — maintenance won't fix the underlying problem. Call us and we'll diagnose it honestly. Most washer repairs are straightforward and much cheaper than replacement.</p>
""")

    # ── Post 6: Repair vs Replace ──
    build_blog_post_shell(BLOG_POSTS[5], """
<p>Should you repair your broken appliance or just replace it? It's one of the most common questions homeowners face — and there's no single right answer. But there are some clear frameworks that make the decision easier.</p>
<h2>The 50% Rule</h2>
<p>The most commonly used rule is simple: if the cost of the repair exceeds 50% of the cost of a new replacement appliance, lean toward replacement. The logic is that you're investing significantly into a machine that has already partially aged out, and may need another repair soon.</p>
<p>But the 50% rule isn't the full picture. You also need to factor in the age of the appliance.</p>
<h2>Age Matters More Than People Think</h2>
<table>
  <thead><tr><th>Appliance</th><th>Expected Lifespan</th><th>When to Lean Toward Replace</th></tr></thead>
  <tbody>
    <tr><td>Refrigerator</td><td>13–17 years</td><td>After year 10 with major failure</td></tr>
    <tr><td>Washer</td><td>10–14 years</td><td>After year 8 with costly repair</td></tr>
    <tr><td>Dryer</td><td>13–17 years</td><td>After year 10 with major failure</td></tr>
    <tr><td>Dishwasher</td><td>9–13 years</td><td>After year 7 with significant repair</td></tr>
    <tr><td>Oven / Range</td><td>13–17 years</td><td>After year 10–12</td></tr>
    <tr><td>Microwave</td><td>7–10 years</td><td>After year 6–7 if costly</td></tr>
  </tbody>
</table>
<p>A $250 repair on a 3-year-old washer is almost always worth it. The same $250 repair on an 11-year-old washer that's already had two repairs? That's a closer call.</p>
<h2>Things That Almost Always Favor Repair</h2>
<ul>
  <li>The appliance is less than 6–7 years old</li>
  <li>The repair cost is under 30% of replacement cost</li>
  <li>The issue is a known, common part (heating element, belt, door seal, pump)</li>
  <li>The appliance is a high-end brand that would cost significantly more to replace</li>
</ul>
<h2>Things That Favor Replacement</h2>
<ul>
  <li>The appliance is near or past its expected lifespan</li>
  <li>This is the second or third significant repair in the past 2 years</li>
  <li>Parts are discontinued or back-ordered</li>
  <li>Energy efficiency has improved significantly — new model could reduce operating costs</li>
</ul>
<div class="callout"><p>💡 We'll always give you an honest assessment. If we think replacement makes more sense than repair, we'll tell you that — even if it means we don't do the work.</p></div>
<h2>Our Honest Take</h2>
<p>In most cases, for appliances under 10 years old with a single component failure, repair is the right choice. It's faster, cheaper, and more sustainable. Call us and we'll diagnose the issue, give you a clear quote, and help you make the right call for your situation.</p>
""")


# ── SERVICE PAGE TEMPLATE ────────────────────────────────────────
def build_service_page(slug, title, meta_title, meta_desc, h1, hero_p, badge,
                       problems, intro_p, process_p, canonical):
    content = head(meta_title, meta_desc, canonical)
    content += navbar("services")
    content += inner_hero(badge, h1, hero_p, hero_btns())
    content += breadcrumb([("Home","/Prime-Clovis/"),("Services","/Prime-Clovis/services/"),(title,"")])
    content += f"""
<div class="section-outer">
<div class="section-box">
  <div class="content-wrap">
    <div class="prose">
      <h2>Common {title} Problems We Fix</h2>
      <div class="problems-grid">"""
    for p in problems:
        content += f"""
        <div class="problem-item">
          <svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
          <span>{p}</span>
        </div>"""
    content += f"""
      </div>
      <h2>How We Work</h2>
      <p>{intro_p}</p>
      <h2>Our Repair Process</h2>
      <p>{process_p}</p>
      <div class="callout"><p>💡 We provide a clear, upfront quote before starting any work. You only pay if you approve the repair.</p></div>
      <h2>Brands We Service</h2>
      <p>We repair all major appliance brands including Whirlpool, GE, Samsung, LG, Maytag, Bosch, KitchenAid, Frigidaire, Sub-Zero, Viking, Electrolux, Kenmore, Amana, and more. If you don't see your brand listed, call us — chances are we service it.</p>
      <h2>Service Area</h2>
      <p>We provide fast, reliable {title.lower()} throughout <a href="/Prime-Clovis/fresno-appliance-repair/">Fresno</a>, <a href="/Prime-Clovis/clovis-appliance-repair/">Clovis</a>, <a href="/Prime-Clovis/madera-appliance-repair/">Madera</a>, <a href="/Prime-Clovis/sanger-appliance-repair/">Sanger</a>, <a href="/Prime-Clovis/fowler-appliance-repair/">Fowler</a>, and all surrounding areas in the Central Valley.</p>
    </div>
    {sidebar_services()}
  </div>
</div>
</div>"""
    content += cta_banner()
    content += booking_section()
    content += footer()
    write_page(f"{BASE}/{slug}/index.html", content)


def build_all_service_pages():
    pages = [
        ("refrigerator-repair-clovis-ca",
         "Refrigerator Repair",
         "Refrigerator Repair Clovis, CA | Prime Appliance Repair",
         "Professional refrigerator repair in Clovis, CA. Fast, reliable service with warranty on parts and labor. Call (559) 765-0303.",
         "Refrigerator Repair in <span class='hi'>Clovis, CA</span>",
         "A refrigerator that isn't cooling properly can quickly become a bigger problem. We provide professional refrigerator repair in Clovis — same-day service available.",
         "Refrigerator Repair",
         ["Refrigerator not cooling or too warm","Freezer working but fridge is warm","Fridge running constantly","Water leaking inside or under the unit","Ice maker not working","Water dispenser not dispensing","Frost buildup in freezer","Strange noises or vibrations","Compressor problems","Temperature fluctuating"],
         "Every refrigerator service starts with a full inspection to find the exact cause of the issue. Once we identify the problem, we explain the solution clearly and proceed using quality parts.",
         "We diagnose first, quote second, repair third. You know the full cost before we start. Our goal is to fix the issue correctly the first time so your refrigerator works reliably again.",
         "https://appliancerepairclovis.com/refrigerator-repair-clovis-ca/"),
        ("washer-repair-clovis-ca",
         "Washer Repair",
         "Washer Repair Clovis, CA | Prime Appliance Repair",
         "Professional washer repair in Clovis, CA. Fast service, warranty included. We fix all brands. Call (559) 765-0303.",
         "Washer Repair in <span class='hi'>Clovis, CA</span>",
         "A broken washer disrupts your entire household. We provide fast, professional washer repair in Clovis — most repairs completed same-day.",
         "Washer Repair",
         ["Won't spin or agitate","Water not draining properly","Leaking water on the floor","Won't start or power on","Loud banging or grinding noise","Not filling with water","Shaking excessively during spin","Door won't lock or unlock","Error codes on display","Cycle not completing"],
         "We service all types of washers — top-load, front-load, high-efficiency, and traditional. Our technicians are experienced with all major brands and bring common parts to every appointment.",
         "After a thorough diagnosis, we provide a clear quote and complete the repair with quality OEM parts. Warranty included on all repairs.",
         "https://appliancerepairclovis.com/washer-repair-clovis-ca/"),
        ("dryer-repair-clovis-ca",
         "Dryer Repair",
         "Dryer Repair Clovis, CA | Prime Appliance Repair",
         "Professional dryer repair in Clovis, CA. Gas and electric dryers. Same-day service available. Call (559) 765-0303.",
         "Dryer Repair in <span class='hi'>Clovis, CA</span>",
         "Not drying? Takes too long? We provide fast, professional dryer repair in Clovis for both gas and electric models — same-day service available.",
         "Dryer Repair",
         ["Not heating or drying clothes","Takes too long to dry","Won't start or turn on","Squeaking or thumping sounds","Drum not turning","Burning smell during use","Door won't close properly","No heat — gas or electric","Overheating or shutting off early","Error codes or control issues"],
         "We repair both gas and electric dryers from all major brands. Whether it's a failed heating element, a broken belt, a bad thermostat, or a clogged exhaust system, we have the parts and expertise to fix it.",
         "Same-day diagnosis and repair on most dryer issues. We quote before we start and stand behind every repair with a warranty.",
         "https://appliancerepairclovis.com/dryer-repair-clovis-ca/"),
        ("dishwasher-repair-clovis-ca",
         "Dishwasher Repair",
         "Dishwasher Repair Clovis, CA | Prime Appliance Repair",
         "Expert dishwasher repair in Clovis, CA. Fast, affordable service for all brands. Warranty included. Call (559) 765-0303.",
         "Dishwasher Repair in <span class='hi'>Clovis, CA</span>",
         "Dirty dishes after a full cycle? Pooling water? Leaks? We provide expert dishwasher repair in Clovis — same-day service, all brands.",
         "Dishwasher Repair",
         ["Not cleaning dishes properly","Water not draining after cycle","Leaking water underneath","Won't fill with water","Dishes not drying","Strange noises during wash","Door latch broken","Control panel unresponsive","White film left on dishes","Error codes displayed"],
         "Dishwashers are complex appliances with several systems that can fail — pumps, spray arms, door latches, control boards, and heating elements. We diagnose all of them accurately.",
         "We bring the right parts for the most common dishwasher failures. Most repairs are completed in a single visit with same-day scheduling available.",
         "https://appliancerepairclovis.com/dishwasher-repair-clovis-ca/"),
        ("oven-repair-clovis-ca",
         "Oven & Range Repair",
         "Oven Repair Clovis, CA | Prime Appliance Repair",
         "Professional oven and range repair in Clovis, CA. Gas and electric. Same-day service. Call (559) 765-0303.",
         "Oven &amp; Range Repair in <span class='hi'>Clovis, CA</span>",
         "Not heating evenly? Burners won't light? We repair gas and electric ovens, ranges, and cooktops throughout Clovis — same-day service available.",
         "Oven Repair",
         ["Oven not heating or heating unevenly","Gas burners not igniting","Oven door won't close properly","Temperature inaccurate","Self-cleaning cycle not working","Bake or broil element failed","Control panel errors","Gas smell near the unit","Igniter clicking constantly","Clock or timer not working"],
         "We repair all types of ovens and ranges — freestanding, slide-in, built-in, gas, and electric. Safety is our priority, especially with gas appliances.",
         "Gas appliances require careful handling. Our technicians are trained to safely diagnose and repair all gas and electric oven issues, and we always test thoroughly before leaving.",
         "https://appliancerepairclovis.com/oven-repair-clovis-ca/"),
        ("stove-repair-clovis-ca",
         "Stove Repair",
         "Stove Repair Clovis, CA | Prime Appliance Repair",
         "Professional stove repair in Clovis, CA. Gas and electric cooktops. Same-day service. Call (559) 765-0303.",
         "Stove Repair in <span class='hi'>Clovis, CA</span>",
         "Burner won't heat? Igniter keeps clicking? We repair gas and electric stoves and cooktops throughout Clovis — fast, same-day service.",
         "Stove Repair",
         ["Burners won't heat or ignite","Uneven heat distribution","Gas smell near burners","Igniter clicking but not lighting","Electric coil not glowing","Surface element failure","Control knob broken","Spark module issues","Burner cap problems","Electronic controls not responding"],
         "Stove problems range from simple igniter replacements to more complex control board issues. We diagnose accurately and provide a clear quote before any repair begins.",
         "We stock common parts for the most popular stove brands, allowing us to complete most repairs in a single visit. Safety tested and warranty included.",
         "https://appliancerepairclovis.com/stove-repair-clovis-ca/"),
        ("microwave-repair-clovis-ca",
         "Microwave Repair",
         "Microwave Repair Clovis, CA | Prime Appliance Repair",
         "Professional microwave repair in Clovis, CA. Fast, safe service for all brands. Call (559) 765-0303.",
         "Microwave Repair in <span class='hi'>Clovis, CA</span>",
         "Not heating? Sparking? Control panel dead? We provide safe, professional microwave repair in Clovis for countertop and over-the-range models.",
         "Microwave Repair",
         ["Not heating food at all","Turntable not spinning","Sparking or arcing inside","Door not closing properly","Control panel unresponsive","Loud humming noise","Display not working","Light bulb out","Fan not running","Burning smell during use"],
         "Microwave repairs involve high-voltage components that require specialized knowledge. Our technicians are trained to safely diagnose and repair all microwave types.",
         "We repair countertop, over-the-range, and built-in microwaves from all major brands. Safety is our priority — every repair is tested before we leave.",
         "https://appliancerepairclovis.com/microwave-repair-clovis-ca/"),
        ("freezer-repair-clovis-ca",
         "Freezer Repair",
         "Freezer Repair Clovis, CA | Prime Appliance Repair",
         "Expert freezer repair in Clovis, CA. Fast service, warranty on parts and labor. Call (559) 765-0303.",
         "Freezer Repair in <span class='hi'>Clovis, CA</span>",
         "Food thawing? Excessive frost? Strange noises? We provide reliable freezer repair in Clovis — chest freezers, upright freezers, and built-ins.",
         "Freezer Repair",
         ["Not freezing properly","Excessive frost or ice buildup","Temperature fluctuating","Food thawing unexpectedly","Strange noises or vibrations","Door seal issues","Compressor problems","Water leaking inside","Not starting or running","Ice buildup on back wall"],
         "We service all types of freezers — chest freezers, upright models, built-in units, and freezer compartments within refrigerators. Our technicians carry common parts for fast same-day repairs.",
         "Freezer problems can escalate quickly — food spoilage is expensive. We prioritize fast diagnosis and same-day repair scheduling to minimize your loss.",
         "https://appliancerepairclovis.com/freezer-repair-clovis-ca/"),
        ("wine-cooler-repair-clovis-ca",
         "Wine Cooler Repair",
         "Wine Cooler Repair Clovis, CA | Prime Appliance Repair",
         "Expert wine cooler repair in Clovis, CA. Protect your collection with professional service. Call (559) 765-0303.",
         "Wine Cooler Repair in <span class='hi'>Clovis, CA</span>",
         "Wine cooler not cooling? Temperature off? We repair all brands and types of wine coolers throughout Clovis and Fresno.",
         "Wine Cooler Repair",
         ["Not cooling to target temperature","Temperature inconsistent or fluctuating","Compressor not running","Condensation inside the unit","Door seal worn or damaged","Control panel not responding","Fan not working","Excessive vibration or noise","Light not working","Thermoelectric system issues"],
         "Wine coolers — whether compressor-based or thermoelectric — require precise temperature control. Our technicians are experienced with both types and all major brands.",
         "We diagnose wine cooler issues accurately and provide a clear quote before beginning work. Protect your investment with professional repair.",
         "https://appliancerepairclovis.com/wine-cooler-repair-clovis-ca/"),
        ("ice-maker-repair-clovis-ca",
         "Ice Maker Repair",
         "Ice Maker Repair Clovis, CA | Prime Appliance Repair",
         "Professional ice maker repair in Clovis, CA. Fast service for all brands. Call (559) 765-0303.",
         "Ice Maker Repair in <span class='hi'>Clovis, CA</span>",
         "Ice maker not producing ice? Leaking? We repair built-in and freestanding ice makers throughout Clovis and Fresno — same-day service available.",
         "Ice Maker Repair",
         ["Not making ice at all","Ice cubes too small or misshapen","Water leaking from unit","Dispenser not dispensing ice","Strange taste or odor in ice","Ice maker jammed or stuck","Electrical issues","Water inlet valve failure","Ice maker frozen over","Low ice production"],
         "Ice maker issues range from simple clogs to failed water inlet valves, control boards, and refrigerant problems. We diagnose the root cause — not just the symptom.",
         "We service built-in ice makers within refrigerators as well as standalone undercounter and countertop units. Same-day service available throughout Clovis and Fresno.",
         "https://appliancerepairclovis.com/ice-maker-repair-clovis-ca/"),
        ("garbage-disposal-repair-clovis-ca",
         "Garbage Disposal Repair",
         "Garbage Disposal Repair Clovis, CA | Prime Appliance Repair",
         "Fast garbage disposal repair in Clovis, CA. Jammed, leaking, or not starting? Call (559) 765-0303.",
         "Garbage Disposal Repair in <span class='hi'>Clovis, CA</span>",
         "Jammed? Humming but not spinning? Leaking underneath? We fix garbage disposals fast throughout Clovis and Fresno.",
         "Disposal Repair",
         ["Not turning on at all","Humming but not spinning (jammed)","Leaking water underneath sink","Loud grinding noises","Not draining properly","Reset button keeps tripping","Foul odors that won't go away","Slow draining","Making clunking sounds","Unit vibrating excessively"],
         "Garbage disposals are simple but important kitchen appliances. Most issues — jams, leaks, and electrical failures — can be diagnosed and repaired quickly.",
         "We carry parts for the most common disposal brands and models. Most repairs are completed in under an hour. If the unit is beyond repair, we can install a new one same-day.",
         "https://appliancerepairclovis.com/garbage-disposal-repair-clovis-ca/"),
    ]
    for args in pages:
        build_service_page(*args)


# ── LOCATION PAGE TEMPLATE ──────────────────────────────────────
def build_location_page(slug, city, meta_title, meta_desc, h1, hero_p, canonical, extra_section=""):
    content = head(meta_title, meta_desc, canonical)
    content += navbar("areas")
    content += inner_hero(
        f"Serving {city}",
        h1,
        hero_p,
        hero_btns()
    )
    content += breadcrumb([("Home","/Prime-Clovis/"),("Service Areas","#"),(city,"")])
    content += f"""
<div class="section-outer">
<div class="section-box">
  <div class="content-wrap">
    <div class="prose">
      <h2>Appliance Repair Services in {city}</h2>
      <p>Finding trustworthy appliance repair in {city} shouldn't be complicated. Our goal is to make the process simple — from the first call to the completed repair. We work directly at your home, arrive with the tools and parts needed for most common issues, and focus on identifying the real cause of the problem.</p>
      <h2>Appliances We Repair</h2>
      <div class="problems-grid">
        <div class="problem-item"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg><span>Refrigerators &amp; Freezers</span></div>
        <div class="problem-item"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg><span>Washers &amp; Dryers</span></div>
        <div class="problem-item"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg><span>Ovens, Ranges &amp; Stoves</span></div>
        <div class="problem-item"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg><span>Dishwashers</span></div>
        <div class="problem-item"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg><span>Microwaves</span></div>
        <div class="problem-item"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg><span>Wine Coolers &amp; Ice Makers</span></div>
        <div class="problem-item"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg><span>Garbage Disposals</span></div>
        <div class="problem-item"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg><span>All Major Brands</span></div>
      </div>
      <h2>Why Choose Us in {city}</h2>
      <ul>
        <li><strong>Experienced technicians</strong> — trained on all major appliance brands and models</li>
        <li><strong>Honest diagnostics</strong> — no unnecessary repairs, no pressure tactics</li>
        <li><strong>Warranty on parts and labor</strong> — every repair is backed</li>
        <li><strong>Fast scheduling</strong> — same-day or next-day service available</li>
        <li><strong>Service at your home</strong> — we come to you, no need to haul your appliance anywhere</li>
      </ul>
      {extra_section}
      <h2>Schedule Your Service in {city}</h2>
      <p>Call today or book online for fast, reliable appliance repair in {city}. Same-day or next-day appointments available throughout the area.</p>
    </div>
    {sidebar_services()}
  </div>
</div>
</div>"""
    content += """
<div class="section-outer">
<div class="section-box">
  <div style="text-align:center;margin-bottom:36px;">
    <div class="section-badge"><svg viewBox="0 0 24 24"><path d="M9 12l2 2 4-4"/><path d="M21 12c0 4.97-4.03 9-9 9s-9-4.03-9-9 4.03-9 9-9 9 4.03 9 9z"/></svg>Brands We Service</div>
    <h2 class="section-title">All Major Appliance Brands</h2>
    <p class="section-sub">We service every major brand. If you don't see yours listed, call us — chances are we fix it.</p>
  </div>
  <div class="brands-grid-5">"""
    brands = ["Whirlpool","Samsung","LG","GE","Maytag","Bosch","KitchenAid","Frigidaire","Sub-Zero","Viking","Thermador","Electrolux","Kenmore","Amana","Miele"]
    for b in brands:
        content += f'<div class="brand-tile">{b}</div>'
    content += """
  </div>
</div>
</div>"""
    content += cta_banner()
    content += booking_section()
    content += footer()
    write_page(f"{BASE}/{slug}/index.html", content)


def build_all_location_pages():
    locs = [
        ("fresno-appliance-repair","Fresno",
         "Appliance Repair Fresno CA | Prime Appliance Repair",
         "Fast, reliable appliance repair in Fresno. Licensed technicians, same-day or next-day service. Call (559) 765-0303.",
         "Appliance Repair in <span class='hi'>Fresno, CA</span>",
         "Fast, reliable appliance repair throughout Fresno. Licensed technicians, same-day or next-day service available.",
         "https://appliancerepairclovis.com/fresno-appliance-repair/"),
        ("clovis-appliance-repair","Clovis",
         "Appliance Repair Clovis CA | Prime Appliance Repair",
         "Professional appliance repair in Clovis, CA. Same-day service, warranty included. Call (559) 765-0303.",
         "Appliance Repair in <span class='hi'>Clovis, CA</span>",
         "Your local appliance repair experts in Clovis. Same-day service, all brands, warranty on every repair.",
         "https://appliancerepairclovis.com/clovis-appliance-repair/"),
        ("madera-appliance-repair","Madera",
         "Appliance Repair Madera CA | Prime Appliance Repair",
         "Appliance repair in Madera, CA. Fast, reliable service for all major appliances. Call (559) 765-0303.",
         "Appliance Repair in <span class='hi'>Madera, CA</span>",
         "Serving Madera with fast, professional appliance repair. All major brands and appliances — same-day scheduling available.",
         "https://appliancerepairclovis.com/madera-appliance-repair/"),
        ("sanger-appliance-repair","Sanger",
         "Appliance Repair Sanger CA | Prime Appliance Repair",
         "Appliance repair in Sanger, CA. Fast, reliable service for all major appliances. Call (559) 765-0303.",
         "Appliance Repair in <span class='hi'>Sanger, CA</span>",
         "Reliable appliance repair in Sanger — same-day or next-day service available for all major appliances and brands.",
         "https://appliancerepairclovis.com/sanger-appliance-repair/"),
        ("fowler-appliance-repair","Fowler",
         "Appliance Repair Fowler CA | Prime Appliance Repair",
         "Appliance repair in Fowler, CA. Certified technicians. Warranty included. Call (559) 765-0303.",
         "Appliance Repair in <span class='hi'>Fowler, CA</span>",
         "Professional appliance repair in Fowler — certified technicians, upfront pricing, and warranty on every repair.",
         "https://appliancerepairclovis.com/fowler-appliance-repair/"),
        ("fraint-appliance-repair","Friant",
         "Appliance Repair Friant CA | Prime Appliance Repair",
         "Appliance repair in Friant, CA. Fast, reliable service for all appliances. Call (559) 765-0303.",
         "Appliance Repair in <span class='hi'>Friant, CA</span>",
         "Serving Friant with honest, reliable appliance repair. Same-day service available for most appliance issues.",
         "https://appliancerepairclovis.com/fraint-appliance-repair/"),
        ("fresno-ca-appliance-repair","Fresno",
         "Appliance Repair Fresno CA | Prime Appliance Repair Services",
         "Expert appliance repair in Fresno CA. All brands, all appliances. Same-day scheduling. Call (559) 765-0303.",
         "Appliance Repair <span class='hi'>Fresno CA</span>",
         "Certified appliance repair technicians serving Fresno, CA. All major brands, same-day scheduling, warranty on every repair.",
         "https://appliancerepairclovis.com/fresno-ca-appliance-repair/"),
        ("home-appliance-repair-fresno-ca","Fresno",
         "Home Appliance Repair Fresno CA | Prime Appliance Repair",
         "Home appliance repair in Fresno, CA. Refrigerators, washers, dryers, ovens and more. Call (559) 765-0303.",
         "Home Appliance Repair <span class='hi'>Fresno, CA</span>",
         "Complete home appliance repair service in Fresno. We fix refrigerators, washers, dryers, ovens, dishwashers, and more.",
         "https://appliancerepairclovis.com/home-appliance-repair-fresno-ca/"),
        ("appliance-repair-near-me","Your Area",
         "Appliance Repair Near Me | Prime Appliance Repair Clovis",
         "Looking for appliance repair near you? Prime Appliance Repair serves Fresno, Clovis, and the Central Valley. Call (559) 765-0303.",
         "Appliance Repair <span class='hi'>Near You</span>",
         "Serving Fresno, Clovis, Madera, Sanger, Fowler, and all surrounding Central Valley communities.",
         "https://appliancerepairclovis.com/appliance-repair-near-me/"),
        ("appliance-repair-near-fresno-ca-usa","Fresno Area",
         "Appliance Repair Near Fresno CA | Prime Appliance Repair",
         "Appliance repair near Fresno, CA. Fast, certified technicians serving the entire Central Valley. Call (559) 765-0303.",
         "Appliance Repair Near <span class='hi'>Fresno, CA</span>",
         "Professional appliance repair near Fresno — serving all communities in and around the Central Valley with same-day scheduling.",
         "https://appliancerepairclovis.com/appliance-repair-near-fresno-ca-usa/"),
    ]
    for args in locs:
        build_location_page(*args)

    # Specialty location-appliance combos
    build_location_page(
        "refrigerator-repair-fresno-ca","Fresno",
        "Refrigerator Repair Fresno CA | Prime Appliance Repair",
        "Professional refrigerator repair in Fresno, CA. Same-day service, all brands. Call (559) 765-0303.",
        "Refrigerator Repair in <span class='hi'>Fresno, CA</span>",
        "Fast, professional refrigerator repair throughout Fresno. Certified technicians, same-day scheduling, warranty on every repair.",
        "https://appliancerepairclovis.com/refrigerator-repair-fresno-ca/",
        "<h2>Signs Your Fresno Refrigerator Needs Repair</h2><ul><li>Not cooling to proper temperature</li><li>Ice maker stopped working</li><li>Water pooling inside or under the unit</li><li>Motor running constantly</li><li>Food spoiling faster than normal</li></ul>"
    )
    build_location_page(
        "dryer-repair-fresno-ca","Fresno",
        "Dryer Repair Fresno CA | Prime Appliance Repair",
        "Dryer repair in Fresno, CA. Gas and electric dryers. Fast service, warranty included. Call (559) 765-0303.",
        "Dryer Repair in <span class='hi'>Fresno, CA</span>",
        "Not heating? Takes too long? We provide professional gas and electric dryer repair throughout Fresno — same-day service available.",
        "https://appliancerepairclovis.com/dryer-repair-fresno-ca/"
    )
    build_location_page(
        "refrigerator-repair-madera-ca","Madera",
        "Refrigerator Repair Madera CA | Prime Appliance Repair",
        "Professional refrigerator repair in Madera, CA. Same-day service, all brands. Call (559) 765-0303.",
        "Refrigerator Repair in <span class='hi'>Madera, CA</span>",
        "Fast refrigerator repair throughout Madera. All brands serviced — same-day and next-day scheduling available.",
        "https://appliancerepairclovis.com/refrigerator-repair-madera-ca/"
    )
    build_location_page(
        "madera-refrigerator-repair","Madera",
        "Madera Refrigerator Repair | Prime Appliance Repair",
        "Refrigerator repair in Madera CA. Certified technicians, warranty included. Call (559) 765-0303.",
        "Madera <span class='hi'>Refrigerator Repair</span>",
        "Expert refrigerator repair in Madera — fast response, honest pricing, warranty on all repairs.",
        "https://appliancerepairclovis.com/madera-refrigerator-repair/"
    )


# ── BRAND PAGES ─────────────────────────────────────────────────
def build_brand_page(slug, brand, meta_title, meta_desc, h1, hero_p, canonical, specifics_html):
    content = head(meta_title, meta_desc, canonical)
    content += navbar("services")
    content += inner_hero(f"{brand} Repair", h1, hero_p, hero_btns())
    content += breadcrumb([("Home","/Prime-Clovis/"),("Services","/Prime-Clovis/services/"),(f"{brand} Repair","")])
    content += f"""
<div class="section-outer">
<div class="section-box">
  <div class="content-wrap">
    <div class="prose">
      {specifics_html}
      <h2>Why Choose Our Service</h2>
      <ul>
        <li><strong>Experienced technicians</strong> — trained on all major brands including {brand}</li>
        <li><strong>Honest diagnostics</strong> — no unnecessary repairs</li>
        <li><strong>Warranty on parts and labor</strong></li>
        <li><strong>Fast scheduling</strong> — same-day or next-day</li>
      </ul>
      <h2>Service Area</h2>
      <p>We proudly service Fresno, Clovis, Madera, Friant, and surrounding areas. We keep everything clear, straightforward, and hassle-free.</p>
    </div>
    {sidebar_services()}
  </div>
</div>
</div>"""
    content += cta_banner()
    content += booking_section()
    content += footer()
    write_page(f"{BASE}/{slug}/index.html", content)


def build_all_brand_pages():
    brands = [
        ("bosch-appliance-repair-fresno","Bosch",
         "Bosch Appliance Repair Fresno | Prime Appliance Repair",
         "Expert Bosch appliance repair in Fresno. Dishwashers, ovens, and more. Warranty included. Call (559) 765-0303.",
         "Bosch Appliance Repair <span class='hi'>Fresno</span>",
         "Expert repair for Bosch appliances in Fresno, Clovis, Madera, and surrounding areas.",
         "https://appliancerepairclovis.com/bosch-appliance-repair-fresno/",
         "<h2>About Bosch Appliances</h2><p>Bosch appliances are known for their quiet performance, efficiency, and sleek European design. Because of that precision engineering, even small issues can require a careful and knowledgeable approach.</p><h2>Common Bosch Issues We Fix</h2><ul><li>Dishwashers not draining</li><li>Error codes on control panel</li><li>Heating issues in ovens</li><li>Units not starting</li><li>Control board problems</li></ul>"),
        ("samsung-appliance-repair-fresno","Samsung",
         "Samsung Appliance Repair Fresno | Prime Appliance Repair",
         "Samsung appliance repair in Fresno. Refrigerators, washers, ovens and more. Warranty included. Call (559) 765-0303.",
         "Samsung Appliance Repair <span class='hi'>Fresno</span>",
         "Expert repair for Samsung appliances in Fresno, Clovis, and surrounding Central Valley areas.",
         "https://appliancerepairclovis.com/samsung-appliance-repair-fresno/",
         "<h2>About Samsung Appliances</h2><p>Samsung makes a wide range of home appliances — from refrigerators with smart features to front-load washers. Their technology-forward design means repairs often require brand-specific knowledge.</p><h2>Common Samsung Issues We Fix</h2><ul><li>Refrigerator ice maker failures</li><li>SE error codes on ovens</li><li>Washer 4E, 5E error codes</li><li>Dryer heating issues</li><li>Display panel problems</li></ul>"),
        ("subzero-appliance-repair-fresno","Sub-Zero",
         "Sub-Zero Appliance Repair Fresno | Prime Appliance Repair",
         "Sub-Zero refrigerator and appliance repair in Fresno. Expert service, warranty included. Call (559) 765-0303.",
         "Sub-Zero Appliance Repair <span class='hi'>Fresno</span>",
         "Specialized repair for Sub-Zero refrigerators and appliances in Fresno and the Central Valley.",
         "https://appliancerepairclovis.com/subzero-appliance-repair-fresno/",
         "<h2>About Sub-Zero</h2><p>Sub-Zero appliances are premium, built-in refrigeration systems that require specialized knowledge to service properly. We have the experience to handle Sub-Zero repairs correctly.</p><h2>Common Sub-Zero Issues We Fix</h2><ul><li>Not cooling properly</li><li>Condenser issues</li><li>Ice maker failures</li><li>Error codes and alarms</li><li>Compressor problems</li></ul>"),
        ("viking-appliance-repair-fresno","Viking",
         "Viking Appliance Repair Fresno | Prime Appliance Repair",
         "Viking appliance repair in Fresno. Ranges, refrigerators, and more. Expert service. Call (559) 765-0303.",
         "Viking Appliance Repair <span class='hi'>Fresno</span>",
         "Expert Viking range, refrigerator, and appliance repair throughout Fresno and the Central Valley.",
         "https://appliancerepairclovis.com/viking-appliance-repair-fresno/",
         "<h2>About Viking</h2><p>Viking is a premium appliance brand known for professional-grade ranges and refrigerators. Their heavy-duty construction is impressive, but when something does go wrong, it requires experienced hands.</p><h2>Common Viking Issues We Fix</h2><ul><li>Range burner ignition problems</li><li>Oven heating inconsistencies</li><li>Refrigerator cooling issues</li><li>Control panel failures</li><li>Gas valve problems</li></ul>"),
    ]
    for args in brands:
        build_brand_page(*args)


# ── PRIVACY POLICY ──────────────────────────────────────────────
def build_privacy():
    content = head("Privacy Policy | Prime Appliance Repair",
                   "Privacy Policy for Prime Appliance Repair Services.",
                   "https://appliancerepairclovis.com/privacy-policy/")
    content += navbar()
    content += inner_hero("Legal", "Privacy <span class='hi'>Policy</span>",
                          "How we collect, use, and protect your information.", trust=False)
    content += breadcrumb([("Home","/Prime-Clovis/"),("Privacy Policy","")])
    content += f"""
<div class="section-outer">
<div class="section-box">
  <div style="max-width:800px;">
    <p style="font-size:13px;color:#9ca3af;margin-bottom:32px;">Last updated: January 1, 2026</p>
    <h2 style="font-size:24px;font-weight:800;color:#2b3340;margin:32px 0 14px;">Information We Collect</h2>
    <p style="font-size:15px;color:#5a6472;line-height:1.8;">We collect information you provide directly to us, such as your name, phone number, email address, and service address when you book an appointment or contact us.</p>
    <h2 style="font-size:24px;font-weight:800;color:#2b3340;margin:32px 0 14px;">How We Use Your Information</h2>
    <p style="font-size:15px;color:#5a6472;line-height:1.8;">We use the information we collect to schedule and provide appliance repair services, communicate with you about your appointment, and improve our services.</p>
    <h2 style="font-size:24px;font-weight:800;color:#2b3340;margin:32px 0 14px;">Information Sharing</h2>
    <p style="font-size:15px;color:#5a6472;line-height:1.8;">We do not sell, trade, or otherwise transfer your personal information to third parties without your consent, except as required by law.</p>
    <h2 style="font-size:24px;font-weight:800;color:#2b3340;margin:32px 0 14px;">Cookies</h2>
    <p style="font-size:15px;color:#5a6472;line-height:1.8;">Our website may use cookies to enhance your browsing experience. You can choose to disable cookies in your browser settings, though this may affect some functionality.</p>
    <h2 style="font-size:24px;font-weight:800;color:#2b3340;margin:32px 0 14px;">Contact Us</h2>
    <p style="font-size:15px;color:#5a6472;line-height:1.8;">If you have questions about this Privacy Policy, please contact us at <a href="tel:{PHONE_RAW}" style="color:#445162;font-weight:700;">{PHONE}</a> or <a href="mailto:{EMAIL}" style="color:#445162;font-weight:700;">{EMAIL}</a>.</p>
  </div>
</div>
</div>"""
    content += footer()
    write_page(f"{BASE}/privacy-policy/index.html", content)


# ── 404 PAGE ────────────────────────────────────────────────────
def build_404():
    content = head("Page Not Found | Prime Appliance Repair",
                   "The page you're looking for doesn't exist. Return to Prime Appliance Repair Services.",
                   "https://appliancerepairclovis.com/404/")
    content += navbar()
    content += f"""
<div style="min-height:80vh;display:flex;align-items:center;justify-content:center;padding:120px 32px 60px;background:linear-gradient(135deg,#1e2432 0%,#2b3340 100%);">
  <div style="text-align:center;max-width:560px;">
    <div style="font-size:100px;font-weight:900;color:#d4f000;line-height:1;margin-bottom:16px;">404</div>
    <h1 style="font-size:32px;font-weight:900;color:#fff;margin:0 0 16px;">Page Not Found</h1>
    <p style="font-size:16px;color:rgba(255,255,255,.70);line-height:1.7;margin:0 0 36px;">The page you're looking for doesn't exist or may have moved. Let's get you back on track.</p>
    <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;">
      <a href="/Prime-Clovis/" style="display:inline-flex;align-items:center;gap:8px;background:#d4f000;color:#1e2432;font-size:15px;font-weight:800;padding:14px 26px;border-radius:9px;text-decoration:none;">Go Home</a>
      <a href="/Prime-Clovis/services/" style="display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,.12);color:#fff;font-size:15px;font-weight:700;padding:14px 26px;border-radius:9px;text-decoration:none;border:1.5px solid rgba(255,255,255,.3);">Our Services</a>
      <a href="/Prime-Clovis/book-an-appointment/" style="display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,.12);color:#fff;font-size:15px;font-weight:700;padding:14px 26px;border-radius:9px;text-decoration:none;border:1.5px solid rgba(255,255,255,.3);">Book Repair</a>
    </div>
    <p style="margin-top:32px;font-size:14px;color:rgba(255,255,255,.5);">Need help? Call us at <a href="tel:{PHONE_RAW}" style="color:#d4f000;font-weight:700;">{PHONE}</a></p>
  </div>
</div>"""
    content += footer()
    write_page(f"{BASE}/404.html", content)


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n🔨 Rebuilding all pages...\n")

    print("📄 Main pages...")
    build_about()
    build_services()
    build_contact()
    build_book()
    build_blog()
    build_privacy()
    build_404()

    print("\n📄 Category pages...")
    build_categories()

    print("\n📄 Blog posts...")
    build_blog_posts()

    print("\n📄 Service pages...")
    build_all_service_pages()

    print("\n📄 Location pages...")
    build_all_location_pages()

    print("\n📄 Brand pages...")
    build_all_brand_pages()

    print(f"\n✅ Done! All pages rebuilt in {BASE}/")
