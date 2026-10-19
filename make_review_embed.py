import re

with open('/Users/amirbahalwan/.gemini/antigravity/scratch/auto-advantage-website/index.html', 'r', encoding='utf-8') as f:
    site_html = f.read()

# Replace local relative asset paths with localhost:3000 paths so they always load smoothly
site_html_fixed = site_html.replace('src="assets/', 'src="http://localhost:3000/assets/')

# Extract styles from site_html
style_matches = re.findall(r'<style>([\s\S]*?)</style>', site_html_fixed)
site_css = "\n".join(style_matches)

# Extract body content from site_html
body_match = re.search(r'<body[^>]*>([\s\S]*?)</body>', site_html_fixed)
if not body_match:
    raise Exception("Could not find body in site_html")

site_body_content = body_match.group(1)

# We will scope site CSS so it only affects #site-preview-root and its descendants!
# This prevents it from bleeding into the parent Generative UI wrapper!
scoped_css = f"""
#site-preview-root {{
  color-scheme: dark;
  font-family: 'DM Sans', -apple-system, sans-serif;
  background: #080C14;
  color: #F1F5F9;
  position: relative;
  width: 100%;
}}

{site_css}

/* Extra overrides for review embed */
#site-preview-root nav {{
  position: sticky;
  top: 0;
}}

.pin-marker {{
  position: absolute;
  width: 26px;
  height: 26px;
  background: #DC2626;
  color: #FFFFFF;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 11px;
  font-family: 'Outfit', sans-serif;
  cursor: pointer;
  z-index: 1000;
  transform: translate(-50%, -50%);
  box-shadow: 0 0 0 2px #FFFFFF, 0 4px 10px rgba(0,0,0,0.6);
  animation: pinPulse 2s infinite;
  user-select: none;
}}

@keyframes pinPulse {{
  0% {{ box-shadow: 0 0 0 2px #FFFFFF, 0 0 0 0 rgba(220, 38, 38, 0.7); }}
  70% {{ box-shadow: 0 0 0 2px #FFFFFF, 0 0 0 10px rgba(220, 38, 38, 0); }}
  100% {{ box-shadow: 0 0 0 2px #FFFFFF, 0 0 0 0 rgba(220, 38, 38, 0); }}
}}

#element-hover-box {{
  position: absolute;
  pointer-events: none;
  z-index: 999;
  border: 2px dashed #DC2626;
  background: rgba(220, 38, 38, 0.08);
  border-radius: 4px;
  display: none;
}}

#element-hover-label {{
  position: absolute;
  top: -22px;
  left: 0;
  background: #DC2626;
  color: #FFFFFF;
  font-size: 10px;
  font-weight: 700;
  padding: 1px 6px;
  border-radius: 4px;
  white-space: nowrap;
}}

.cursor-pin #site-preview-root {{
  cursor: crosshair !important;
}}

.cursor-pin #site-preview-root * {{
  cursor: crosshair !important;
}}

.cursor-highlight #site-preview-root {{
  cursor: pointer !important;
}}

.cursor-highlight #site-preview-root * {{
  cursor: pointer !important;
}}
"""

template = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
  <style>
{scoped_css}
  </style>
</head>
<body class="bg-transparent text-[var(--foreground)] antialiased p-2">

  <!-- Main Review Card Container -->
  <div class="bg-[var(--card)] text-[var(--foreground)] border border-[var(--border)] rounded-2xl shadow-2xl overflow-hidden flex flex-col font-sans">
    
    <!-- Top Action & Review Bar -->
    <div class="bg-[var(--background)] border-b border-[var(--border)] px-4 py-2.5 flex flex-wrap items-center justify-between gap-3 select-none">
      
      <!-- Brand & Status -->
      <div class="flex items-center gap-2.5">
        <span class="flex h-2.5 w-2.5 relative">
          <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-red-400 opacity-75"></span>
          <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-red-600"></span>
        </span>
        <span class="font-bold text-xs tracking-wider uppercase text-[var(--foreground)]">Auto Advantage Studio</span>
        <span class="text-[11px] px-2 py-0.5 rounded-full bg-blue-500/10 text-blue-400 font-medium border border-blue-500/20">Live Review</span>
      </div>

      <!-- Mode Selector -->
      <div class="flex items-center bg-[var(--card)] border border-[var(--border)] rounded-full p-1 gap-1">
        <button id="mode-browse" class="px-3 py-1 rounded-full text-xs font-semibold bg-red-600 text-white transition-all shadow-sm">
          Browse
        </button>
        <button id="mode-pin" class="px-3 py-1 rounded-full text-xs font-medium text-[var(--muted-foreground)] hover:text-[var(--foreground)] transition-all">
          Add Pin
        </button>
        <button id="mode-highlight" class="px-3 py-1 rounded-full text-xs font-medium text-[var(--muted-foreground)] hover:text-[var(--foreground)] transition-all">
          Highlight Element
        </button>
      </div>

      <!-- Viewport Selector -->
      <div class="flex items-center bg-[var(--card)] border border-[var(--border)] rounded-full p-1 gap-1">
        <button id="view-desktop" class="px-2.5 py-1 rounded-full text-xs font-semibold bg-[var(--foreground)] text-[var(--background)] transition-all">
          Desktop
        </button>
        <button id="view-mobile" class="px-2.5 py-1 rounded-full text-xs font-medium text-[var(--muted-foreground)] hover:text-[var(--foreground)] transition-all">
          Mobile (375px)
        </button>
      </div>

      <!-- Notes Counter & Copy Actions -->
      <div class="flex items-center gap-2">
        <button id="btn-toggle-notes" class="flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-white border border-slate-700 transition-all">
          <span>Notes</span>
          <span id="notes-badge" class="bg-red-600 text-white text-[10px] px-1.5 py-0.2 rounded-full font-bold">0</span>
        </button>
        <button id="btn-copy-feedback" class="flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-blue-600 hover:bg-blue-500 text-white transition-all shadow-sm">
          <span>Copy Feedback</span>
        </button>
      </div>

    </div>

    <!-- Mode Helper Instruction Banner -->
    <div id="mode-helper" class="bg-blue-950/40 border-b border-blue-900/30 px-4 py-1.5 text-xs text-blue-300 flex items-center justify-between">
      <span id="mode-helper-text">Browse Mode: Click buttons, explore before and after photo, and inspect the booking flow.</span>
      <span class="text-[11px] text-blue-400 font-mono">Tip: Switch to "Add Pin" or "Highlight Element" to leave edits</span>
    </div>

    <!-- Scrollable Preview Window -->
    <div id="preview-window" class="relative overflow-y-auto max-h-[500px] bg-[#080C14]">
      
      <!-- Responsive Frame Container -->
      <div id="viewport-frame" class="w-full transition-all duration-300">
        
        <!-- Element Highlighter Box -->
        <div id="element-hover-box">
          <span id="element-hover-label">Element</span>
        </div>

        <!-- The actual Website Content -->
        <div id="site-preview-root">
{site_body_content}
        </div>

      </div>

    </div>

    <!-- Notes Tray / Drawer -->
    <div id="notes-tray" class="border-t border-[var(--border)] bg-[var(--background)] p-3 hidden flex-col gap-2 max-h-[200px] overflow-y-auto">
      <div class="flex items-center justify-between pb-1 border-b border-[var(--border)]">
        <h4 class="text-xs font-bold uppercase tracking-wider text-[var(--foreground)]">Feedback Checklist (<span id="notes-tray-count">0</span> notes)</h4>
        <button id="btn-clear-notes" class="text-[11px] text-red-400 hover:text-red-300 underline">Clear All</button>
      </div>
      <div id="notes-list-items" class="flex flex-col gap-2 pt-1 text-xs text-[var(--muted-foreground)]">
        <!-- Dynamically rendered notes -->
      </div>
    </div>

    <!-- Pop-up Comment Modal -->
    <div id="comment-modal" class="fixed inset-0 bg-black/60 backdrop-blur-sm z-[9999] hidden items-center justify-center p-4">
      <div class="bg-slate-900 border border-slate-700 rounded-xl p-5 w-full max-w-md shadow-2xl text-white font-sans">
        <h3 id="modal-title" class="font-bold text-base text-white mb-1">Add Feedback</h3>
        <p id="modal-target-desc" class="text-xs text-slate-400 mb-3 font-mono"></p>
        <textarea id="modal-textarea" rows="3" class="w-full bg-slate-950 border border-slate-700 rounded-lg p-2.5 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-red-500 mb-4" placeholder="Type what you want changed here..."></textarea>
        <div class="flex items-center justify-end gap-2">
          <button id="modal-btn-cancel" class="px-3 py-1.5 rounded-lg text-xs font-medium text-slate-400 hover:text-white bg-slate-800">Cancel</button>
          <button id="modal-btn-save" class="px-4 py-1.5 rounded-lg text-xs font-semibold text-white bg-red-600 hover:bg-red-500">Save Note</button>
        </div>
      </div>
    </div>

    <!-- Copied Toast -->
    <div id="feedback-toast" class="fixed bottom-4 left-1/2 -translate-x-1/2 bg-slate-900 border border-green-500/50 text-white px-4 py-2 rounded-full text-xs font-semibold shadow-2xl flex items-center gap-2 opacity-0 pointer-events-none transition-all duration-200 z-[10000]">
      <span class="w-2 h-2 rounded-full bg-green-400"></span>
      <span id="toast-text">Feedback copied to clipboard!</span>
    </div>

  </div>

  <script>
  (function() {{
    let currentMode = 'browse'; // 'browse', 'pin', 'highlight'
    let currentViewport = 'desktop';
    let notes = JSON.parse(localStorage.getItem('auto_adv_embed_notes') || '[]');
    let pendingNote = null;
    let hoveredEl = null;

    const root = document.getElementById('site-preview-root');
    const previewWindow = document.getElementById('preview-window');
    const viewportFrame = document.getElementById('viewport-frame');
    const hoverBox = document.getElementById('element-hover-box');
    const hoverLabel = document.getElementById('element-hover-label');
    const modal = document.getElementById('comment-modal');
    const modalTitle = document.getElementById('modal-title');
    const modalDesc = document.getElementById('modal-target-desc');
    const modalText = document.getElementById('modal-textarea');
    const toast = document.getElementById('feedback-toast');
    const notesBadge = document.getElementById('notes-badge');
    const notesTrayCount = document.getElementById('notes-tray-count');
    const notesTray = document.getElementById('notes-tray');
    const notesList = document.getElementById('notes-list-items');
    const helperText = document.getElementById('mode-helper-text');

    const btnBrowse = document.getElementById('mode-browse');
    const btnPin = document.getElementById('mode-pin');
    const btnHighlight = document.getElementById('mode-highlight');
    const btnDesktop = document.getElementById('view-desktop');
    const btnMobile = document.getElementById('view-mobile');
    const btnToggleNotes = document.getElementById('btn-toggle-notes');
    const btnCopyFeedback = document.getElementById('btn-copy-feedback');
    const btnClearNotes = document.getElementById('btn-clear-notes');
    const btnModalSave = document.getElementById('modal-btn-save');
    const btnModalCancel = document.getElementById('modal-btn-cancel');

    function setMode(mode) {{
      currentMode = mode;
      document.body.classList.remove('cursor-pin', 'cursor-highlight');

      btnBrowse.className = 'px-3 py-1 rounded-full text-xs font-medium text-[var(--muted-foreground)] hover:text-[var(--foreground)] transition-all';
      btnPin.className = 'px-3 py-1 rounded-full text-xs font-medium text-[var(--muted-foreground)] hover:text-[var(--foreground)] transition-all';
      btnHighlight.className = 'px-3 py-1 rounded-full text-xs font-medium text-[var(--muted-foreground)] hover:text-[var(--foreground)] transition-all';

      if (mode === 'browse') {{
        btnBrowse.className = 'px-3 py-1 rounded-full text-xs font-semibold bg-red-600 text-white transition-all shadow-sm';
        helperText.textContent = 'Browse Mode: Explore links, before/after photo, and the consultation booking form.';
      }} else if (mode === 'pin') {{
        btnPin.className = 'px-3 py-1 rounded-full text-xs font-semibold bg-red-600 text-white transition-all shadow-sm';
        document.body.classList.add('cursor-pin');
        helperText.textContent = 'Add Pin Mode: Click anywhere on the webpage to place a numbered feedback marker.';
      }} else if (mode === 'highlight') {{
        btnHighlight.className = 'px-3 py-1 rounded-full text-xs font-semibold bg-red-600 text-white transition-all shadow-sm';
        document.body.classList.add('cursor-highlight');
        helperText.textContent = 'Highlight Mode: Hover over any card, text, or button and click to attach feedback to that component.';
      }}
      hoverBox.style.display = 'none';
    }}

    btnBrowse.addEventListener('click', () => setMode('browse'));
    btnPin.addEventListener('click', () => setMode('pin'));
    btnHighlight.addEventListener('click', () => setMode('highlight'));

    function setViewport(vp) {{
      currentViewport = vp;
      if (vp === 'desktop') {{
        viewportFrame.className = 'w-full transition-all duration-300';
        btnDesktop.className = 'px-2.5 py-1 rounded-full text-xs font-semibold bg-[var(--foreground)] text-[var(--background)] transition-all';
        btnMobile.className = 'px-2.5 py-1 rounded-full text-xs font-medium text-[var(--muted-foreground)] hover:text-[var(--foreground)] transition-all';
      }} else {{
        viewportFrame.className = 'max-w-[375px] mx-auto border-4 border-slate-700 rounded-3xl shadow-2xl overflow-hidden my-4 transition-all duration-300';
        btnMobile.className = 'px-2.5 py-1 rounded-full text-xs font-semibold bg-[var(--foreground)] text-[var(--background)] transition-all';
        btnDesktop.className = 'px-2.5 py-1 rounded-full text-xs font-medium text-[var(--muted-foreground)] hover:text-[var(--foreground)] transition-all';
      }}
      renderPins();
    }}

    btnDesktop.addEventListener('click', () => setViewport('desktop'));
    btnMobile.addEventListener('click', () => setViewport('mobile'));

    function showToast(msg) {{
      document.getElementById('toast-text').textContent = msg;
      toast.classList.remove('opacity-0', 'pointer-events-none');
      setTimeout(() => toast.classList.add('opacity-0', 'pointer-events-none'), 2500);
    }}

    function saveNotes() {{
      localStorage.setItem('auto_adv_embed_notes', JSON.stringify(notes));
      updateUI();
    }}

    function updateUI() {{
      notesBadge.textContent = notes.length;
      notesTrayCount.textContent = notes.length;
      renderPins();
      renderTray();
    }}

    function renderPins() {{
      document.querySelectorAll('.pin-marker').forEach(p => p.remove());
      const rRect = root.getBoundingClientRect();
      const pRect = previewWindow.getBoundingClientRect();

      notes.forEach((note, idx) => {{
        const pin = document.createElement('div');
        pin.className = 'pin-marker';
        pin.setAttribute('data-id', note.id);
        pin.innerHTML = `<span>${{idx + 1}}</span>`;
        pin.style.left = note.x + 'px';
        pin.style.top = note.y + 'px';

        pin.addEventListener('click', (e) => {{
          e.stopPropagation();
          notesTray.classList.remove('hidden');
          const card = document.getElementById('tray-note-' + note.id);
          if (card) {{
            card.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
            card.classList.add('border-red-500');
            setTimeout(() => card.classList.remove('border-red-500'), 1500);
          }}
        }});

        root.appendChild(pin);
      }});
    }}

    function renderTray() {{
      if (notes.length === 0) {{
        notesList.innerHTML = '<p class="py-2 text-center text-slate-500 italic">No notes yet. Click "Add Pin" or "Highlight Element" to add feedback.</p>';
        return;
      }}
      notesList.innerHTML = notes.map((note, idx) => `
        <div id="tray-note-${{note.id}}" class="p-2.5 rounded-lg bg-[var(--card)] border border-[var(--border)] flex items-start justify-between gap-2 transition-all">
          <div class="flex items-start gap-2">
            <span class="w-5 h-5 rounded-full bg-red-600 text-white flex items-center justify-center font-bold text-[10px] shrink-0 mt-0.5">${{idx + 1}}</span>
            <div>
              <p class="font-semibold text-slate-200 text-xs">${{escapeHtml(note.targetLabel)}}</p>
              <p class="text-slate-300 text-xs mt-0.5">${{escapeHtml(note.text)}}</p>
              <p class="text-[10px] text-slate-500 mt-1 font-mono">${{note.timestamp}}</p>
            </div>
          </div>
          <button onclick="window.removeEmbedNote('${{note.id}}')" class="text-slate-500 hover:text-red-400 text-sm px-1 font-bold">&times;</button>
        </div>
      `).join('');
    }}

    function escapeHtml(s) {{
      return (s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }}

    window.removeEmbedNote = function(id) {{
      notes = notes.filter(n => n.id !== id);
      saveNotes();
    }};

    // Hover Highlight
    root.addEventListener('mousemove', (e) => {{
      if (currentMode !== 'highlight') {{
        hoverBox.style.display = 'none';
        return;
      }}
      const target = e.target.closest('h1, h2, h3, p, a, button, img, section, .hero-content, .card, .service-row, .gallery-item');
      if (!target || target.classList.contains('pin-marker') || target.id === 'element-hover-box') {{
        hoverBox.style.display = 'none';
        return;
      }}

      const rRect = root.getBoundingClientRect();
      const rect = target.getBoundingClientRect();

      hoverBox.style.display = 'block';
      hoverBox.style.left = (rect.left - rRect.left) + 'px';
      hoverBox.style.top = (rect.top - rRect.top) + 'px';
      hoverBox.style.width = rect.width + 'px';
      hoverBox.style.height = rect.height + 'px';

      const tag = target.tagName.toLowerCase();
      const text = (target.textContent || '').trim().slice(0, 24);
      hoverLabel.textContent = `<${{tag}}> ${{text ? '"' + text + '..."' : ''}}`;
      hoveredEl = target;
    }});

    // Click handler for Pin and Highlight
    root.addEventListener('click', (e) => {{
      if (currentMode === 'browse') return;

      e.preventDefault();
      e.stopPropagation();

      const rRect = root.getBoundingClientRect();
      const x = Math.round(e.clientX - rRect.left);
      const y = Math.round(e.clientY - rRect.top);

      let label = 'Canvas Spot';
      if (currentMode === 'highlight' && hoveredEl) {{
        const tag = hoveredEl.tagName.toUpperCase();
        const snippet = (hoveredEl.textContent || '').trim().slice(0, 24);
        label = `${{tag}}: ${{snippet ? snippet : 'Element'}}`;
      }} else {{
        const el = document.elementFromPoint(e.clientX, e.clientY);
        if (el) {{
          const tag = el.tagName.toUpperCase();
          const snippet = (el.textContent || '').trim().slice(0, 20);
          label = `${{tag}}: ${{snippet ? snippet : 'Section'}}`;
        }}
      }}

      pendingNote = {{
        id: 'note_' + Date.now(),
        x: x,
        y: y,
        targetLabel: label,
        timestamp: new Date().toLocaleTimeString([], {{ hour: '2-digit', minute: '2-digit' }})
      }};

      modalTitle.textContent = `Feedback for: ${{label}}`;
      modalDesc.textContent = `Location: x: ${{x}}px, y: ${{y}}px`;
      modalText.value = '';
      modal.classList.remove('hidden');
      modal.classList.add('flex');
      modalText.focus();
    }});

    btnModalCancel.addEventListener('click', () => {{
      modal.classList.add('hidden');
      modal.classList.remove('flex');
      pendingNote = null;
    }});

    btnModalSave.addEventListener('click', () => {{
      const val = modalText.value.trim();
      if (!val) return;
      if (pendingNote) {{
        pendingNote.text = val;
        notes.push(pendingNote);
        saveNotes();
        pendingNote = null;
        modal.classList.add('hidden');
        modal.classList.remove('flex');
        showToast('Feedback note saved! Click "Copy Feedback" when ready');
      }}
    }});

    btnToggleNotes.addEventListener('click', () => {{
      notesTray.classList.toggle('hidden');
    }});

    btnCopyFeedback.addEventListener('click', () => {{
      if (notes.length === 0) {{
        showToast('No notes yet to copy');
        return;
      }}
      let md = '### Visual Review Notes for Auto Advantage Website\\n\\n';
      notes.forEach((n, i) => {{
        md += `${{i + 1}}. **[${{n.targetLabel}}]**: ${{n.text}}\\n`;
      }});
      md += '\\nPlease apply these requested changes to the website.';

      navigator.clipboard.writeText(md).then(() => {{
        showToast('Feedback copied! Paste it in the chat');
      }}).catch(() => {{
        showToast('Feedback copied! Paste it in the chat');
      }});
    }});

    btnClearNotes.addEventListener('click', () => {{
      if (confirm('Clear all review notes?')) {{
        notes = [];
        saveNotes();
        showToast('All notes cleared');
      }}
    }});

    updateUI();
  }})();
  </script>

</body>
</html>
"""

# Strip any em/en dashes
template = template.replace('—', ' - ').replace('–', ' - ')

out_path = '/Users/amirbahalwan/.gemini/antigravity/scratch/auto-advantage-website/review_embed.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(template)

print("Created review_embed.html! Length:", len(template))
