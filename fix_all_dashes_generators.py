with open('/Users/amirbahalwan/.gemini/antigravity/scratch/auto-advantage-website/update_toolbars.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace SVG horizontal line minus
text = text.replace(
    '<line x1="5" y1="12" x2="19" y2="12"></line>',
    '<polyline points="6 9 12 15 18 9"></polyline>'
)

# Replace &rarr;
text = text.replace('&rarr;', '&#8250;')

with open('/Users/amirbahalwan/.gemini/antigravity/scratch/auto-advantage-website/update_toolbars.py', 'w', encoding='utf-8') as f:
    f.write(text)

with open('/Users/amirbahalwan/.gemini/antigravity/scratch/auto-advantage-website/update_embed.py', 'r', encoding='utf-8') as f:
    text2 = f.read()

text2 = text2.replace('&rarr;', '&#8250;')

with open('/Users/amirbahalwan/.gemini/antigravity/scratch/auto-advantage-website/update_embed.py', 'w', encoding='utf-8') as f:
    f.write(text2)

print("Updated generators!")
