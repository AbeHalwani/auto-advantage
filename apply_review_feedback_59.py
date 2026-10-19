import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Navigation updates (Items 4, 5, 6, 23, 24)
nav_menu_old = re.search(r'<nav class="nav-menu">[\s\S]*?</nav>', html)
if nav_menu_old:
    nav_menu_new = """<nav class="nav-menu">
          <a href="#top">Home</a>
          <a href="#services">Services</a>
          <a href="#craftsmanship">Craftsmanship</a>
          <a href="#financing">Financing</a>
          <a href="#reviews">Reviews</a>
          <a href="#book-appointment">Book Online</a>
          <a href="#faq">FAQ</a>
        </nav>"""
    html = html.replace(nav_menu_old.group(0), nav_menu_new)

# Update mobile drawer
drawer_old = re.search(r'<div class="nav-mobile-drawer" id="nav-mobile-drawer">[\s\S]*?</div>\s*</header>', html)
if drawer_old:
    drawer_new = """<div class="nav-mobile-drawer" id="nav-mobile-drawer">
      <a href="#top" class="nmd-link">Home</a>
      <a href="#services" class="nmd-link">Services</a>
      <a href="#craftsmanship" class="nmd-link">Craftsmanship</a>
      <a href="#financing" class="nmd-link">Financing</a>
      <a href="#reviews" class="nmd-link">Reviews</a>
      <a href="#book-appointment" class="nmd-link">Book Online</a>
      <a href="#faq" class="nmd-link">FAQ</a>
    </div>
  </header>"""
    html = html.replace(drawer_old.group(0), drawer_new)

# 2. Hero Section updates (Items 13, 25, 26, 35, 36)
# Headline
html = re.sub(
    r'<h1 class="hero-headline">[\s\S]*?</h1>',
    '<h1 class="hero-headline">\n          The Best Auto Repair Shop in <br><span class="accent">Lincoln Park, MI.</span>\n        </h1>',
    html
)

# Lead paragraph
html = re.sub(
    r'<p class="hero-lead-text">[\s\S]*?</p>',
    '<p class="hero-lead-text">\n          Certified Mechanics that specialize in Collision repair. <strong>Computerized laser unibody realignment</strong>, climate controlled downdraft spray booths, and direct insurance claims management with all major carriers.\n        </p>',
    html,
    count=1
)

# Remove Chief Laser Datum card from hero-ribbon-grid (Item 13)
ribbon_old = re.search(r'<div class="hero-ribbon-grid">[\s\S]*?</div>\s*</div>\s*</div>', html)
if ribbon_old:
    ribbon_new = """<div class="hero-ribbon-grid">
          <div class="hr-item">
            <strong>Facility Location</strong>
            <span>1486 Southfield Rd, Lincoln Park, MI</span>
          </div>
          <div class="hr-item">
            <strong>Paint Science</strong>
            <span>Heated Downdraft Booth & Optical Match</span>
          </div>
          <div class="hr-item">
            <strong>Warranty Coverage</strong>
            <span>Written Lifetime Finish & Labor Warranty</span>
          </div>
        </div>
      </div>
    </div>"""
    html = html.replace(ribbon_old.group(0), ribbon_new)

# 3. Philosophy / Statement Section (Items 27, 28)
statement_old = re.search(r'<section class="statement-section">[\s\S]*?</section>', html)
if statement_old:
    statement_new = """<section class="statement-section">
    <div class="container">
      <div class="statement-grid">
        <div class="statement-quote">
          When an accident damages your vehicle, <span class="red">we make sure it is safe, solid, and looks brand new again.</span>
        </div>
        <div class="statement-bullets">
          <div class="sb-item">
            <span class="sb-check">✓</span>
            <div class="sb-text">
              <strong>Straight Frame Alignment</strong>
              We measure and pull bent frames back to factory millimeter specs so your car drives straight and protects your family.
            </div>
          </div>
          <div class="sb-item">
            <span class="sb-check">✓</span>
            <div class="sb-text">
              <strong>Exact Factory Color Match</strong>
              We match your vehicle original paint in our heated spray booth so the finish is seamless and guaranteed for life.
            </div>
          </div>
          <div class="sb-item">
            <span class="sb-check">✓</span>
            <div class="sb-text">
              <strong>Safety Sensors & Airbag Reset</strong>
              We test and calibrate all cameras, airbags, and radar collision sensors so they work the moment you drive away.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>"""
    html = html.replace(statement_old.group(0), statement_new)

# 4. Service Card 7: Dent Repair pill
html = html.replace('<div class="service-card-pill">Paintless PDR</div>', '<div class="service-card-pill">Paintless Dent Repair</div>')

# 5. Section 46 Format like uploaded image (Items 46, 47, 48, 57, 58)
spec_grid_old = re.search(r'<div class="craft-spec-grid">[\s\S]*?</div>\s*</div>\s*</section>', html)
if spec_grid_old:
    spec_grid_new = """<!-- Premium 4-Stage Precision Restoration Process (Inspired by High-End Engineering) -->
      <div class="craft-flow-wrap">
        <div class="craft-flow-header">
          <div class="cfh-eyebrow">CLINICAL CRAFTSMANSHIP &bull; 4-STAGE RESTORATION</div>
          <h3 class="cfh-title">MEASURED. REALIGNED. <span class="accent">NEVER</span> COMPROMISED.</h3>
        </div>

        <div class="craft-flow-grid">
          <!-- Step 01 -->
          <div class="cfg-card">
            <div class="cfg-step">01</div>
            <h4 class="cfg-title">LASER BENCH</h4>
            <div class="cfg-tag"><span class="tag-arrow">&#9656;</span> factory datum pull</div>
            <p class="cfg-desc">Chief multipull hydraulic frame bench with laser coordinate scanners measuring down to factory millimeter specs.</p>
          </div>

          <div class="cfg-arrow">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
          </div>

          <!-- Step 02 -->
          <div class="cfg-card">
            <div class="cfg-step">02</div>
            <h4 class="cfg-title">DOWNDRAFT</h4>
            <div class="cfg-tag"><span class="tag-arrow">&#9656;</span> heated european bake</div>
            <p class="cfg-desc">Heated downdraft spray booth featuring European climate controlled bake cycles for OEM clearcoat durability.</p>
          </div>

          <div class="cfg-arrow">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
          </div>

          <!-- Step 03 -->
          <div class="cfg-card">
            <div class="cfg-step">03</div>
            <h4 class="cfg-title">COLOR SCAN</h4>
            <div class="cfg-tag"><span class="tag-arrow">&#9656;</span> computerized pearl match</div>
            <p class="cfg-desc">Digital spectrophotometer analysis accounts for paint age, sun fade, and metallic pearl flake density.</p>
          </div>

          <div class="cfg-arrow">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
          </div>

          <!-- Step 04 -->
          <div class="cfg-card">
            <div class="cfg-step">04</div>
            <h4 class="cfg-title">LIFETIME</h4>
            <div class="cfg-tag"><span class="tag-arrow">&#9656;</span> you are protected for life</div>
            <p class="cfg-desc">Written lifetime warranty backing all structural realignment, body reconstruction, and clearcoat paint finishes.</p>
          </div>
        </div>
      </div>
    </div>
  </section>"""
    html = html.replace(spec_grid_old.group(0), spec_grid_new)

# 6. Insurance Matrix title & centering (Items 14, 15, 37, 38)
html = html.replace(
    '<div class="im-title">Main Insurance Companies We Often Work with</div>',
    '<h3 class="im-title">Main Insurance Companies we often work with.</h3>'
)

# 7. Financing section: Remove generic cards, keep only Snap & Sunbit with QR codes (Items 53, 54)
financing_old = re.search(r'<div class="financing-grid">[\s\S]*?<!-- Official Financing Partners', html)
if financing_old:
    html = html.replace(financing_old.group(0), '<!-- Official Financing Partners')

# 8. Reviews rating badge 4x larger & centered (Items 17, 18, 30, 31)
# Already <h2>Reviews</h2>, let's enhance rating badge styling in CSS

# 9. Booking section updates (Items 20, 33, 44, 49, 55)
html = html.replace(
    '<div class="ecc-label">Call to make an appointment over the phone or if you have questions</div>',
    '<div class="ecc-label">Call to make an appointment over the phone or if you have questions</div>'
)
# Time slots: remove 4:30 PM (Item 44: 30 min after opening to 1 hr before closing -> 9:30 AM to 4:00 PM)
html = html.replace(
    '<option value="">Select Time (9:30 AM to 4:30 PM)</option>',
    '<option value="">Select Time (9:30 AM to 4:00 PM)</option>'
)
html = re.sub(
    r'<option value="04:30 PM">4:30 PM \(Latest Arrival\)</option>',
    '',
    html
)
html = html.replace('4:00 PM</option>', '4:00 PM (Latest Booking Slot)</option>')

# Free In-Person -> Free In Person (no dash) (Item 55)
html = html.replace('Free In-Person Estimate', 'Free In Person Estimate')
html = html.replace('100% Free In-Person Written Estimate', '100% Free In Person Written Estimate')

# 10. Instagram heading (Item 59)
html = html.replace('<h2>Follow Us on Instagram</h2>', '<h2>Follow us on Instagram</h2>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated index.html HTML content successfully.')
