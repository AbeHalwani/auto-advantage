import re

with open('/Users/amirbahalwan/.gemini/antigravity/scratch/auto-advantage-website/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Logo in Nav & Remove Auto Advantage / Collision & Auto Repair Spans
old_nav_brand = """        <a href="#" class="nav-brand">
          <img src="assets/logo-light.png" alt="Auto Advantage Collision and Auto Repair" class="nav-logo-img">
          <div class="nav-brand-title">
            <span class="brand-name">Auto Advantage</span>
            <span class="brand-sub">Collision & Auto Repair</span>
          </div>
        </a>"""

new_nav_brand = """        <a href="#" class="nav-brand">
          <img src="assets/logo_master_transparent.png" alt="Auto Advantage Collision" class="nav-logo-img">
        </a>"""

if old_nav_brand in html:
    html = html.replace(old_nav_brand, new_nav_brand)
    print("Replaced nav brand successfully")
else:
    print("Warning: old_nav_brand exact match not found, using regex")
    html = re.sub(
        r'<a href="#" class="nav-brand">[\s\S]*?</a>',
        '<a href="#" class="nav-brand">\n          <img src="assets/logo_master_transparent.png" alt="Auto Advantage Collision" class="nav-logo-img">\n        </a>',
        html,
        count=1
    )

# 2. Remove Numbers from Nav
old_nav_menu = """        <nav class="nav-menu">
          <a href="#services"><span class="nav-num">01</span>Services</a>
          <a href="#craftsmanship"><span class="nav-num">02</span>Craftsmanship</a>
          <a href="#instagram"><span class="nav-num">03</span>Live Feed</a>
          <a href="#insurance"><span class="nav-num">04</span>Insurance</a>
          <a href="#reviews"><span class="nav-num">05</span>Reviews</a>
          <a href="#coordinates"><span class="nav-num">06</span>Location</a>
        </nav>"""

new_nav_menu = """        <nav class="nav-menu">
          <a href="#services">Services</a>
          <a href="#craftsmanship">Craftsmanship</a>
          <a href="#instagram">Live Feed</a>
          <a href="#insurance">Insurance</a>
          <a href="#reviews">Reviews</a>
          <a href="#coordinates">Location</a>
        </nav>"""

if old_nav_menu in html:
    html = html.replace(old_nav_menu, new_nav_menu)
    print("Replaced nav menu successfully")
else:
    print("Warning: old_nav_menu exact match not found, using regex")
    html = re.sub(r'<span class="nav-num">\d+</span>', '', html)

# 3. Remove Hero Eyebrow (Lincoln Park, MI • Automotive Collision Atelier)
old_hero_eyebrow = """      <div class="hero-eyebrow">
        <span class="hero-eyebrow-line"></span>
        <span>Lincoln Park, MI • Automotive Collision Atelier</span>
      </div>"""

if old_hero_eyebrow in html:
    html = html.replace(old_hero_eyebrow, '')
    print("Removed hero eyebrow successfully")
else:
    html = re.sub(r'<div class="hero-eyebrow">[\s\S]*?</div>', '', html, count=1)
    print("Removed hero eyebrow via regex")

# 4. Remove Scope of Work Eyebrow
html = html.replace('<div class="sec-eyebrow">Scope of Work</div>', '')
print("Removed Scope of Work eyebrow")

# 5. Remove numbers from services directory rows (<span class="dir-num">01</span>, etc.)
html = re.sub(r'<span class="dir-num">\d+</span>\s*', '', html)
print("Removed dir-num numbers")

# 6. Remove SPEC 01 - SPEC 04 from craftsmanship spec list
html = re.sub(r'<span class="csg-index">SPEC \d+</span>\s*', '', html)
print("Removed csg-index numbers")

# 7. Update Footer Logo
old_footer_brand = """          <div class="brand-badge">
            <img src="assets/logo-light.png" alt="Auto Advantage Collision and Auto Repair">
          </div>"""

new_footer_brand = """          <div class="footer-logo-wrap">
            <img src="assets/logo_master_transparent.png" alt="Auto Advantage Collision" class="footer-logo-img">
          </div>"""

html = html.replace(old_footer_brand, new_footer_brand)
print("Updated footer logo")

# 8. Update CSS for nav-phone, btn-book-appt, nav-inner, directory-row, and responsive media queries
old_btn_book_appt = """.btn-book-appt {
      background: var(--crimson);
      color: var(--white);
      font-family: var(--font-display);
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      padding: 12px 22px;
      border-radius: 4px;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.25s;
    }

    .btn-book-appt:hover {
      background: var(--crimson-hover);
      transform: translateY(-1px);
    }"""

new_btn_book_appt = """.btn-book-appt {
      background: var(--crimson);
      color: var(--white);
      font-family: var(--font-display);
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      padding: 12px 24px;
      border-radius: 9999px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      white-space: nowrap;
      flex-shrink: 0;
      border: 1px solid rgba(255, 255, 255, 0.16);
      box-shadow: 0 4px 14px rgba(220, 38, 38, 0.35);
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .btn-book-appt:hover {
      background: var(--crimson-hover);
      transform: translateY(-2px);
      box-shadow: 0 6px 22px rgba(220, 38, 38, 0.55);
      border-color: rgba(255, 255, 255, 0.3);
    }"""

html = html.replace(old_btn_book_appt, new_btn_book_appt)

# Update nav-phone and nav-logo-img
old_nav_phone = """.nav-phone {
      font-family: var(--font-display);
      font-size: 14px;
      font-weight: 700;
      letter-spacing: 0.02em;
      color: var(--white);
      display: flex;
      align-items: center;
      gap: 8px;
      transition: color 0.2s;
    }"""

new_nav_phone = """.nav-phone {
      font-family: var(--font-display);
      font-size: 14px;
      font-weight: 700;
      letter-spacing: 0.02em;
      color: var(--white);
      display: inline-flex;
      align-items: center;
      gap: 8px;
      white-space: nowrap;
      flex-shrink: 0;
      transition: color 0.2s;
    }"""

html = html.replace(old_nav_phone, new_nav_phone)

# Update nav-logo-img and nav-inner
html = html.replace(
    '.nav-logo-img {\n      height: 44px;\n      width: auto;\n      object-fit: contain;\n    }',
    '.nav-logo-img {\n      height: 48px;\n      width: auto;\n      max-width: 240px;\n      object-fit: contain;\n      display: block;\n    }'
)

# Update footer logo CSS
html = html.replace(
    '.footer-brand .brand-badge {\n      background: #FFFFFF;\n      padding: 6px 14px;\n      border-radius: 4px;\n      display: inline-flex;\n      align-items: center;\n      margin-bottom: 18px;\n    }',
    '.footer-logo-wrap {\n      display: inline-flex;\n      align-items: center;\n      margin-bottom: 20px;\n    }\n\n    .footer-logo-img {\n      height: 46px;\n      width: auto;\n      object-fit: contain;\n    }'
)

# Update directory-row grid columns now that dir-num is removed
html = html.replace(
    'grid-template-columns: 70px 1.4fr 1.6fr 180px 40px;',
    'grid-template-columns: 1.6fr 2fr 180px 40px;'
)

# Enhance responsive media queries for tablet (1024px) and mobile (768px)
old_media = """    /* Responsive adjustments */
    @media (max-width: 1024px) {
      .hero-meta-grid { grid-template-columns: 1fr; gap: 40px; }
      .statement-grid { grid-template-columns: 1fr; gap: 36px; }
      .directory-row { grid-template-columns: 50px 1fr 1fr 40px; }
      .dir-badge { display: none; }
      .craft-spec-grid { grid-template-columns: repeat(2, 1fr); }
      .ig-grid { grid-template-columns: repeat(2, 1fr); }
      .testi-grid { grid-template-columns: 1fr; gap: 32px; }
      .estimate-split { grid-template-columns: 1fr; }
      .coord-grid { grid-template-columns: 1fr; }
      .footer-top-grid { grid-template-columns: repeat(2, 1fr); }
    }

    @media (max-width: 768px) {
      .container { padding: 0 20px; }
      .nav-menu { display: none; }
      .hero { padding: 60px 0; }
      .hero-headline { font-size: 40px; }
      .directory-row { grid-template-columns: 40px 1fr 30px; gap: 14px; }
      .dir-desc { display: none; }
      .craft-spec-grid { grid-template-columns: 1fr; }
      .ig-grid { grid-template-columns: 1fr; }
      .form-row-2 { grid-template-columns: 1fr; }
      .editorial-form { padding: 24px; }
      .im-list { gap: 14px; font-size: 12px; }
      .footer-top-grid { grid-template-columns: 1fr; }
    }"""

new_media = """    /* Responsive adjustments for Tablet and Mobile */
    @media (max-width: 1024px) {
      .nav-inner { height: 76px; gap: 18px; }
      .nav-menu { gap: 18px; }
      .nav-menu a { font-size: 12.5px; }
      .nav-phone { font-size: 13px; }
      .btn-book-appt { padding: 10px 18px; font-size: 12px; }
      .hero { padding: 70px 0 60px; }
      .hero-headline { font-size: clamp(38px, 5.5vw, 64px); }
      .hero-meta-grid { grid-template-columns: 1fr; gap: 36px; }
      .statement-grid { grid-template-columns: 1fr; gap: 32px; }
      .directory-row { grid-template-columns: 1.4fr 1.6fr 40px; gap: 16px; }
      .dir-badge { display: none; }
      .craft-spec-grid { grid-template-columns: repeat(2, 1fr); gap: 28px; }
      .ig-grid { grid-template-columns: repeat(2, 1fr); gap: 24px; }
      .testi-grid { grid-template-columns: 1fr; gap: 32px; }
      .estimate-split { grid-template-columns: 1fr; gap: 40px; }
      .coord-grid { grid-template-columns: 1fr; gap: 36px; }
      .footer-top-grid { grid-template-columns: repeat(2, 1fr); gap: 36px; }
    }

    @media (max-width: 768px) {
      .container { padding: 0 20px; }
      .nav-inner {
        height: auto;
        padding: 14px 0;
        flex-wrap: wrap;
        gap: 12px;
        justify-content: space-between;
      }
      .nav-brand { flex-shrink: 0; }
      .nav-logo-img { height: 38px; max-width: 160px; }
      .nav-menu { display: none; }
      .nav-cta-cluster {
        display: flex;
        align-items: center;
        gap: 10px;
        flex-wrap: nowrap;
      }
      .nav-phone {
        font-size: 12px;
        padding: 7px 12px;
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 9999px;
      }
      .btn-book-appt {
        padding: 8px 16px;
        font-size: 11px;
      }
      .hero { padding: 48px 0 54px; }
      .hero-headline { font-size: 34px; line-height: 1.1; }
      .hero-lead-text { font-size: 15px; }
      .hero-actions {
        flex-direction: column;
        gap: 12px;
        width: 100%;
      }
      .btn-hero-primary,
      .btn-hero-secondary {
        width: 100%;
        justify-content: center;
        text-align: center;
      }
      .directory-row {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 8px;
        padding: 20px 0;
        position: relative;
      }
      .dir-title { font-size: 18px; padding-right: 32px; }
      .dir-desc {
        display: block;
        font-size: 13.5px;
        color: var(--text-light-muted);
        line-height: 1.55;
      }
      .dir-arrow {
        position: absolute;
        right: 0;
        top: 20px;
        font-size: 18px;
      }
      .craft-spec-grid { grid-template-columns: 1fr; gap: 24px; }
      .ig-grid { grid-template-columns: 1fr; gap: 20px; }
      .form-row-2 { grid-template-columns: 1fr; }
      .editorial-form { padding: 24px 18px; border-radius: 12px; }
      .im-list { gap: 14px; font-size: 12px; }
      .footer-top-grid { grid-template-columns: 1fr; gap: 32px; }
    }"""

html = html.replace(old_media, new_media)

# Strip any em/en dashes
html = html.replace('—', ' - ').replace('–', ' - ')

with open('/Users/amirbahalwan/.gemini/antigravity/scratch/auto-advantage-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Applied all user edits to index.html successfully!")
