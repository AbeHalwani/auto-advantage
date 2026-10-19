with open('/Users/amirbahalwan/.gemini/antigravity/scratch/auto-advantage-website/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

replacements = [
    # Compound words
    ('collision-damaged', 'collision damaged'),
    ('climate-controlled', 'climate controlled'),
    ('high-strength', 'high strength'),
    ('clean-bay', 'clean bay'),
    ('pre-accident', 'original factory'),
    ('Multi-axis', 'Multi axis'),
    ('sway-damaged', 'sway damaged'),
    ('leak-proof', 'leakproof'),
    ('multi-stage', 'multistage'),
    ('Mercedes-Benz', 'Mercedes Benz'),
    ('S-Class', 'S Class'),
    ('multi-pull', 'multipull'),
    ('Mid-Day', 'Midday'),
    ('self-pay', 'self pay'),
    ('Self-Pay', 'Self Pay'),
    ('laser-measured', 'laser measured'),
    ('factory-spec', 'factory spec'),
    ('all-wheel', 'all wheel'),
    ('state-of-the-art', 'state of the art'),
    
    # Phone numbers
    ('(313) 386-1234', '(313) 386.1234'),
    ('(313) 000-0000', '(313) 000.0000'),
    ('313-386-1234', '313.386.1234'),
    
    # Any stray dashes with spaces
    (' - ', ' '),
    (' -- ', ' '),
    ('—', ' '),
    ('–', ' '),
]

for old, new in replacements:
    count = text.count(old)
    if count > 0:
        text = text.replace(old, new)
        print(f"Replaced '{old}' with '{new}' ({count} times)")

with open('/Users/amirbahalwan/.gemini/antigravity/scratch/auto-advantage-website/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved updated index.html!")
