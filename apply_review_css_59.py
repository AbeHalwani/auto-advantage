with open('index.html', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update Hero styles: reduce padding and move car video up
css = css.replace(
    """    .hero {
      position: relative;
      min-height: 84vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding: 44px 0 0 0;
      background: #000000;
      border-bottom: 1px solid var(--hairline-dark);
      overflow: hidden;
    }""",
    """    .hero {
      position: relative;
      min-height: 80vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding: 16px 0 0 0;
      background: #000000;
      border-bottom: 1px solid var(--hairline-dark);
      overflow: hidden;
    }"""
)

css = css.replace(
    """    .hero-video-element {
      position: absolute;
      top: 41%;
      left: 75%;
      width: 145%;
      height: 100%;
      min-width: 145%;
      min-height: 100%;
      object-fit: cover;
      transform: translate(-50%, -50%);
      opacity: 0.98;
      filter: contrast(1.15) brightness(1.0);
    }""",
    """    .hero-video-element {
      position: absolute;
      top: 35%;
      left: 75%;
      width: 145%;
      height: 100%;
      min-width: 145%;
      min-height: 100%;
      object-fit: cover;
      transform: translate(-50%, -50%);
      opacity: 0.98;
      filter: contrast(1.15) brightness(1.0);
    }"""
)

# 2. Update hero-ribbon-grid to 3 columns (since Chief Laser card was removed)
css = css.replace(
    """    .hero-ribbon-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
    }""",
    """    .hero-ribbon-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }"""
)

# 3. Update Before & After labels: double size & centered
css = css.replace(
    """    .ba-label {
      position: absolute;
      top: 24px;
      padding: 14px 32px;
      font-family: var(--font-display);
      font-size: 24px;
      font-weight: 800;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      background: rgba(8, 12, 20, 0.92);
      border: 1px solid rgba(255, 255, 255, 0.18);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-radius: 8px;
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.6);
      text-align: center;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      z-index: 10;
    }""",
    """    .ba-label {
      position: absolute;
      top: 24px;
      padding: 16px 40px;
      font-family: var(--font-display);
      font-size: 28px;
      font-weight: 900;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      background: rgba(8, 12, 20, 0.94);
      border: 1px solid rgba(255, 255, 255, 0.22);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-radius: 10px;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.75);
      text-align: center;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      z-index: 10;
    }"""
)

# 4. Reviews 4x larger rating display
css = css.replace(
    """    .testi-score-badge-centered .stars {
      color: #F59E0B;
      letter-spacing: 6px;
      font-size: clamp(40px, 4.8vw, 54px);
      line-height: 1;
    }

    .testi-score-badge-centered .score-text {
      font-size: clamp(20px, 2.4vw, 26px);
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: var(--text-light);
    }""",
    """    .testi-score-badge-centered .stars {
      color: #F59E0B;
      letter-spacing: 10px;
      font-size: clamp(60px, 6.5vw, 76px);
      line-height: 1;
      text-shadow: 0 4px 28px rgba(245, 158, 11, 0.45);
      margin-bottom: 4px;
    }

    .testi-score-badge-centered .score-text {
      font-size: clamp(26px, 3vw, 34px);
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: #FFFFFF;
    }"""
)

# 5. Insurance Matrix: centered, larger, evenly spaced
css = css.replace(
    """    .im-title {
      font-family: var(--font-display);
      font-size: 14.5px;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: none;
      color: var(--crimson);
      text-align: center;
      line-height: 1.4;
    }

    .im-grid {
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 14px 18px;
      width: 100%;
    }

    .im-card {
      background: rgba(255, 255, 255, 0.025);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 8px;
      padding: 16px 18px;
      font-family: var(--font-display);
      font-size: 15px;
      font-weight: 800;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      color: #F1F5F9;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      min-height: 52px;
      transition: all 0.25s;
    }""",
    """    .im-title {
      font-family: var(--font-display);
      font-size: 22px;
      font-weight: 800;
      letter-spacing: -0.01em;
      text-transform: none;
      color: #FFFFFF;
      text-align: center;
      line-height: 1.3;
      margin-bottom: 4px;
    }

    .im-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px 20px;
      width: 100%;
      max-width: 960px;
      margin: 0 auto;
    }

    .im-card {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 10px;
      padding: 18px 20px;
      font-family: var(--font-display);
      font-size: 16.5px;
      font-weight: 800;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      min-height: 60px;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.3);
      transition: all 0.25s;
    }
    .im-card:hover {
      border-color: var(--crimson);
      background: rgba(220, 38, 38, 0.08);
      transform: translateY(-2px);
    }"""
)

# 6. Instagram feed: 1:1 aspect ratio square crops
css = css.replace(
    """    .ig-card {
      position: relative;
      background: var(--dark);
      overflow: hidden;
      aspect-ratio: 4 / 3;
    }""",
    """    .ig-card {
      position: relative;
      background: var(--dark);
      overflow: hidden;
      aspect-ratio: 1 / 1;
      border-radius: 12px;
      border: 1px solid rgba(255, 255, 255, 0.08);
    }"""
)

# 7. Add Section 46 High-End Process Flow CSS (matching media_1792442811353.png)
section_46_css = """
    /* ============================================================
       SECTION 46: 4-STAGE PRECISION FLOW (Inspired by Auditor Specimen)
       ============================================================ */
    .craft-flow-wrap {
      margin-top: 48px;
      padding-top: 40px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
    }

    .craft-flow-header {
      text-align: center;
      margin-bottom: 36px;
    }

    .cfh-eyebrow {
      font-family: var(--font-display);
      font-size: 13px;
      font-weight: 800;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--crimson);
      margin-bottom: 10px;
    }

    .cfh-title {
      font-family: var(--font-display);
      font-size: clamp(30px, 4vw, 48px);
      font-weight: 900;
      letter-spacing: -0.02em;
      color: #FFFFFF;
      text-transform: uppercase;
      line-height: 1.1;
    }

    .craft-flow-grid {
      display: flex;
      align-items: stretch;
      justify-content: space-between;
      gap: 12px;
      width: 100%;
    }

    .cfg-card {
      flex: 1;
      background: #0B0E14;
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      padding: 26px 20px;
      display: flex;
      flex-direction: column;
      position: relative;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .cfg-card:hover {
      border-color: var(--crimson);
      transform: translateY(-4px);
      box-shadow: 0 16px 36px rgba(220, 38, 38, 0.22);
      background: #0F121A;
    }

    .cfg-step {
      font-family: var(--font-display);
      font-size: 13.5px;
      font-weight: 800;
      color: #64748B;
      letter-spacing: 0.06em;
      margin-bottom: 14px;
    }

    .cfg-title {
      font-family: var(--font-display);
      font-size: clamp(19px, 1.8vw, 23px);
      font-weight: 900;
      letter-spacing: -0.01em;
      text-transform: uppercase;
      color: #FFFFFF;
      margin-bottom: 10px;
      line-height: 1.15;
    }

    .cfg-tag {
      font-family: var(--font-display);
      font-size: 12.5px;
      font-weight: 700;
      color: var(--crimson);
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .cfg-tag .tag-arrow {
      font-size: 11px;
    }

    .cfg-desc {
      font-family: 'DM Sans', sans-serif;
      font-size: 13.5px;
      line-height: 1.6;
      color: #94A3B8;
      margin-top: auto;
    }

    .cfg-arrow {
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--crimson);
      opacity: 0.85;
      padding: 0 2px;
      flex-shrink: 0;
    }

    @media (max-width: 900px) {
      .craft-flow-grid {
        flex-direction: column;
        gap: 16px;
      }
      .cfg-arrow {
        transform: rotate(90deg);
        padding: 6px 0;
      }
    }
"""

# Insert Section 46 CSS before the responsive section
css = css.replace('/* ============================================================\n       RESPONSIVE DESIGN SYSTEM', section_46_css + '\n    /* ============================================================\n       RESPONSIVE DESIGN SYSTEM')

# 8. Service Requested pre-select banner and select border: remove redundant red outline
css = css.replace(
    """    .selected-service-banner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      background: rgba(229, 35, 32, 0.08);
      border: 1px solid rgba(229, 35, 32, 0.35);
      border-left: 4px solid var(--crimson);
      border-radius: 8px;
      padding: 10px 14px;
      margin-bottom: 4px;
    }""",
    """    .selected-service-banner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-left: 4px solid #64748B;
      border-radius: 8px;
      padding: 10px 14px;
      margin-bottom: 4px;
    }"""
)

# 9. Booking section compact styling so full form shows without scrolling
css = css.replace(
    """    .estimate-section {
      padding: 72px 0;
      background: var(--dark-surface);
      border-top: 1px solid var(--hairline-dark);
      border-bottom: 1px solid var(--hairline-dark);
      position: relative;
    }""",
    """    .estimate-section {
      padding: 40px 0;
      background: var(--dark-surface);
      border-top: 1px solid var(--hairline-dark);
      border-bottom: 1px solid var(--hairline-dark);
      position: relative;
    }"""
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated index.html CSS successfully.')
