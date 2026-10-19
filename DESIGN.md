# Design System: Auto Advantage Collision & Auto Repair

## 1. Visual Theme & Atmosphere
A high-precision, motorsport-grade automotive craft aesthetic. The atmosphere balances certified technical rigor with approachable local honesty. Clean, surgical layout structures are paired with deep metallic contrast, calibrated electric blue energy, and assertive crimson highlights drawn directly from the Auto Advantage emblem.

Atmosphere scores:
* Density: 5 (Balanced technical whitespace)
* Variance: 6 (Asymmetric splits, staggered cards)
* Motion: 5 (Subtle spring physics, tactile reveals)

## 2. Color Palette & Roles
* **Canvas White** (`#F8FAFC`) : Primary background surface for daytime clarity.
* **Pure Technical Surface** (`#FFFFFF`) : Card, container, and input backgrounds.
* **Charcoal Ink** (`#0F172A`) : High-contrast primary typography and icons.
* **Muted Steel** (`#475569`) : Secondary text, explanatory copy, and specifications.
* **Titanium Silver** (`#CBD5E1`) : Precision borders, structural dividers, and metallic sheen accents.
* **Electric Blue** (`#1D4ED8`) : Primary brand anchor, header accents, and verified badges (drawn from the emblem car silhouette).
* **Deep Marine Surface** (`#131B2E`) : Dark contrast section background for reviews and warranty guarantees.
* **Obsidian Midnight** (`#0A0F1D`) : Deepest contrasting base for the footer and night-mode elements.
* **Precision Crimson** (`#DC2626`) : High-priority call to action, urgent estimate alerts, and phone buttons (drawn from "AUTO" in the emblem).

Rules:
* No pure black (`#000000`) is permitted.
* No neon or purple glow gradients.
* Crimson is reserved exclusively for primary actions and telephone emergency access.

## 3. Typography Rules
* **Display Font:** Archivo (700 and 800 weight) with tight letter spacing (`-0.025em`) and compact line height (`1.15`). Conveys structural stability and automotive power.
* **Body Font:** Plus Jakarta Sans or Inter alternative with relaxed leading (`1.65`) and maximum reading width of 65 characters per line.
* **Monospace Accent:** JetBrains Mono for hours, telephone numbers, and VIN/vehicle specs.
* **Banned:** Generic system serifs, decorative scripts, and Comic/Papyrus style fonts.

## 4. Component Stylings
* **Navigation:** Sticky translucent bar with glassmorphism blur (`backdrop-filter: blur(14px)`), hairline titanium border (`rgba(15, 23, 42, 0.08)`), embedded official logo badge, and high-contrast telephone CTA.
* **Buttons:** Tactile feedback on press (`transform: translateY(-2px)`). Radius `8px`. Solid Crimson (`#DC2626`) or Electric Blue (`#1D4ED8`) fill for primary actions. Muted ghost borders for secondary actions.
* **Cards:** Soft radius (`14px`), 1px titanium border (`#E2E8F0`), subtle neutral shadow on hover (`0 14px 30px rgba(15, 23, 42, 0.07)`). No heavy card stacking.
* **Input Fields:** Clear uppercase label above input, neutral slate fill (`#F8FAFC`), crisp border (`#CBD5E1`), and focused blue outline ring (`#1D4ED8`).
* **Lifetime Warranty Seal:** Gold-toned metallic badge (`#F59E0B`) with dark obsidian backdrop to communicate permanence and trust.

## 5. Layout Principles
* **Asymmetric Hero:** Split layout with benefit-driven headline on the left and quick-intake vehicle estimate card on the right.
* **Alternating Feature Flow:** Avoid generic three-card rows where possible. Use alternating horizontal blocks for frame machinery and paint booths.
* **Containment:** Max width container of `1200px` centered with `24px` horizontal padding.
* **Mobile Strictness:** All multi-column sections collapse to a single column below `768px` viewport width with a persistent bottom call bar.

## 6. Motion & Interaction
* **Scroll Reveals:** Staggered upward translation (`20px`) with cubic-bezier easing (`0.16, 1, 0.3, 1`) and `0.6s` duration.
* **Hover States:** Smooth `0.2s` transitions for buttons, phone badges, and service cards.

## 7. Anti-Patterns (Banned)
* No emojis in UI text (use SVG icons or clean symbols).
* No AI copywriting buzzwords ("seamless", "elevate", "unleash", "next-gen").
* No fake statistics or fabricated claim percentages.
* No em dashes in customer-facing text.
* No overlapping text elements or low-contrast text.
