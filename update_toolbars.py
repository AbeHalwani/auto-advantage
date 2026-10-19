import re

# 1. Update preview.html generator
with open('/Users/amirbahalwan/.gemini/antigravity/scratch/auto-advantage-website/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# CSS for preview.html with bottom-docked, collapsible toolbar
preview_css = """
/* ============================================================
   BOTTOM-DOCKED, COLLAPSIBLE REVIEW TOOLBAR
   ============================================================ */
#review-toolbar {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 9999999;
  background: rgba(10, 16, 28, 0.95);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  border: 1px solid rgba(255, 255, 255, 0.16);
  box-shadow: 0 20px 45px rgba(0, 0, 0, 0.7), 0 0 0 1px rgba(0,0,0,0.8);
  border-radius: 9999px;
  padding: 6px 10px;
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: 'DM Sans', -apple-system, sans-serif;
  color: #F8FAFC;
  font-size: 13px;
  user-select: none;
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.2s ease;
}

#review-toolbar.minimized {
  transform: translateX(-50%) translateY(120px);
  opacity: 0;
  pointer-events: none;
}

/* Floating Reopen Button (when minimized) */
#review-floating-trigger {
  position: fixed;
  bottom: 20px;
  right: 24px;
  z-index: 9999998;
  background: #DC2626;
  color: #FFFFFF;
  border: 2px solid rgba(255, 255, 255, 0.9);
  box-shadow: 0 10px 30px rgba(220, 38, 38, 0.5), 0 4px 12px rgba(0, 0, 0, 0.5);
  padding: 10px 18px;
  border-radius: 9999px;
  font-size: 13px;
  font-weight: 700;
  font-family: 'DM Sans', sans-serif;
  cursor: pointer;
  display: none;
  align-items: center;
  gap: 8px;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  user-select: none;
}

#review-floating-trigger.show {
  display: flex;
  animation: triggerBounce 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

#review-floating-trigger:hover {
  transform: scale(1.05);
  box-shadow: 0 14px 35px rgba(220, 38, 38, 0.7);
}

@keyframes triggerBounce {
  0% { transform: scale(0.6) translateY(20px); opacity: 0; }
  100% { transform: scale(1) translateY(0); opacity: 1; }
}

.review-brand {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 4px 10px 4px 6px;
  font-weight: 700;
  letter-spacing: 0.04em;
  font-size: 12px;
  color: #F1F5F9;
  border-right: 1px solid rgba(255, 255, 255, 0.12);
  text-transform: uppercase;
}

.review-brand-dot {
  width: 8px;
  height: 8px;
  background: #DC2626;
  border-radius: 50%;
  box-shadow: 0 0 8px #DC2626;
}

.review-btn-group {
  display: flex;
  align-items: center;
  background: rgba(255, 255, 255, 0.06);
  border-radius: 9999px;
  padding: 2px;
  gap: 2px;
}

.review-btn {
  background: transparent;
  border: none;
  color: #94A3B8;
  padding: 6px 12px;
  border-radius: 9999px;
  font-size: 12px;
  font-weight: 500;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.15s ease;
  font-family: inherit;
}

.review-btn:hover {
  color: #FFFFFF;
  background: rgba(255, 255, 255, 0.08);
}

.review-btn.active {
  background: #DC2626;
  color: #FFFFFF;
  font-weight: 600;
  box-shadow: 0 2px 8px rgba(220, 38, 38, 0.4);
}

.review-btn.btn-secondary {
  background: rgba(37, 99, 235, 0.2);
  color: #60A5FA;
  border: 1px solid rgba(37, 99, 235, 0.4);
}

.review-btn.btn-secondary:hover {
  background: rgba(37, 99, 235, 0.35);
  color: #FFFFFF;
}

.review-btn.btn-minimize {
  background: rgba(255, 255, 255, 0.06);
  color: #94A3B8;
  padding: 6px 10px;
}

.review-btn.btn-minimize:hover {
  background: rgba(255, 255, 255, 0.15);
  color: #FFFFFF;
}

.review-badge {
  background: #DC2626;
  color: #FFFFFF;
  font-size: 10px;
  font-weight: 700;
  padding: 1px 6px;
  border-radius: 999px;
  margin-left: 2px;
}

/* Canvas & Viewport Wrapper */
#review-viewport-container {
  width: 100%;
  min-height: 100vh;
  background: #06090F;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  position: relative;
  overflow-x: hidden;
  padding-bottom: 90px; /* Leave space so bottom docked bar never covers content */
}

#review-viewport-container.viewport-tablet {
  max-width: 768px;
  margin: 20px auto 100px auto;
  min-height: 1024px;
  border: 8px solid #1E293B;
  border-radius: 28px;
  box-shadow: 0 30px 80px rgba(0, 0, 0, 0.8);
  overflow: hidden;
}

#review-viewport-container.viewport-mobile {
  max-width: 390px;
  margin: 20px auto 100px auto;
  min-height: 844px;
  border: 10px solid #1E293B;
  border-radius: 36px;
  box-shadow: 0 30px 80px rgba(0, 0, 0, 0.8);
  overflow: hidden;
}

/* Pin element */
.review-pin {
  position: absolute;
  width: 28px;
  height: 28px;
  background: #DC2626;
  color: #FFFFFF;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 12px;
  font-family: 'Outfit', sans-serif;
  cursor: pointer;
  z-index: 999990;
  transform: translate(-50%, -50%);
  box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.9), 0 8px 16px rgba(0, 0, 0, 0.5);
  animation: pinPulse 2s infinite;
  transition: transform 0.2s ease;
}

.review-pin:hover {
  transform: translate(-50%, -50%) scale(1.15);
}

@keyframes pinPulse {
  0% { box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.9), 0 0 0 0 rgba(220, 38, 38, 0.6); }
  70% { box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.9), 0 0 0 12px rgba(220, 38, 38, 0); }
  100% { box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.9), 0 0 0 0 rgba(220, 38, 38, 0); }
}

/* Highlight Box */
#review-highlighter-box {
  position: absolute;
  pointer-events: none;
  z-index: 999980;
  border: 2px dashed #DC2626;
  background: rgba(220, 38, 38, 0.08);
  border-radius: 6px;
  display: none;
  transition: all 0.08s ease-out;
}

#review-highlighter-tag {
  position: absolute;
  top: -24px;
  left: 0;
  background: #DC2626;
  color: #FFFFFF;
  font-size: 11px;
  font-family: 'DM Sans', sans-serif;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 4px;
  white-space: nowrap;
}

/* Modal Popup for Adding Note */
#review-modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(6px);
  z-index: 9999998;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.review-dialog {
  background: #0F172A;
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 18px;
  width: 100%;
  max-width: 480px;
  padding: 24px;
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.7);
  color: #F8FAFC;
  font-family: 'DM Sans', sans-serif;
}

.review-dialog h3 {
  font-family: 'Outfit', sans-serif;
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.review-dialog p {
  color: #94A3B8;
  font-size: 13px;
  margin-bottom: 16px;
}

.review-dialog textarea {
  width: 100%;
  min-height: 110px;
  background: #090E17;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 10px;
  padding: 12px;
  color: #F1F5F9;
  font-family: inherit;
  font-size: 14px;
  resize: vertical;
  margin-bottom: 16px;
  outline: none;
}

.review-dialog textarea:focus {
  border-color: #DC2626;
  box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.2);
}

.review-dialog-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

/* Comments Drawer */
#review-drawer {
  position: fixed;
  top: 0;
  right: -420px;
  width: 400px;
  height: 100vh;
  background: #0B111E;
  border-left: 1px solid rgba(255, 255, 255, 0.12);
  z-index: 9999995;
  box-shadow: -15px 0 40px rgba(0, 0, 0, 0.6);
  display: flex;
  flex-direction: column;
  transition: right 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  font-family: 'DM Sans', sans-serif;
  color: #F8FAFC;
}

#review-drawer.open {
  right: 0;
}

.review-drawer-header {
  padding: 20px 24px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.review-drawer-title {
  font-family: 'Outfit', sans-serif;
  font-size: 18px;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 10px;
}

.review-drawer-close {
  background: transparent;
  border: none;
  color: #94A3B8;
  font-size: 20px;
  cursor: pointer;
  padding: 4px;
  border-radius: 6px;
}

.review-drawer-close:hover {
  color: #FFFFFF;
}

.review-drawer-content {
  flex: 1;
  overflow-y: auto;
  padding: 20px 24px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.review-note-card {
  background: #111927;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  padding: 14px 16px;
  transition: border-color 0.15s ease;
}

.review-note-card:hover {
  border-color: rgba(220, 38, 38, 0.4);
}

.review-note-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 8px;
}

.review-note-tag {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  font-weight: 700;
  color: #DC2626;
  text-transform: uppercase;
  letter-spacing: 0.03em;
}

.review-note-num {
  background: #DC2626;
  color: #FFFFFF;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
}

.review-note-delete {
  background: transparent;
  border: none;
  color: #64748B;
  cursor: pointer;
  font-size: 14px;
  transition: color 0.15s;
}

.review-note-delete:hover {
  color: #EF4444;
}

.review-note-body {
  font-size: 14px;
  line-height: 1.5;
  color: #F1F5F9;
  margin-bottom: 10px;
  white-space: pre-wrap;
}

.review-note-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 11px;
  color: #64748B;
}

.review-note-jump {
  color: #38BDF8;
  cursor: pointer;
  text-decoration: underline;
}

.review-drawer-footer {
  padding: 18px 24px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  background: #090E17;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

/* Toast */
#review-toast {
  position: fixed;
  bottom: 90px;
  left: 50%;
  transform: translateX(-50%) translateY(100px);
  background: #0F172A;
  color: #FFFFFF;
  border: 1px solid rgba(34, 197, 94, 0.4);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
  padding: 12px 24px;
  border-radius: 9999px;
  font-size: 13px;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 10px;
  z-index: 99999999;
  opacity: 0;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  pointer-events: none;
  font-family: 'DM Sans', sans-serif;
}

#review-toast.show {
  transform: translateX(-50%) translateY(0);
  opacity: 1;
}

/* Mode cursors */
body.mode-pin #review-viewport-container {
  cursor: crosshair;
}

body.mode-highlight #review-viewport-container {
  cursor: pointer;
}
"""

preview_markup = """
<!-- ============================================================
     BOTTOM-DOCKED, COLLAPSIBLE REVIEW STUDIO TOOLBAR
     ============================================================ -->
<div id="review-toolbar">
  <div class="review-brand">
    <span class="review-brand-dot"></span>
    Review Studio
  </div>

  <div class="review-btn-group">
    <button class="review-btn active" id="btn-mode-browse" title="Interact normally with the page">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
      Browse
    </button>
    <button class="review-btn" id="btn-mode-pin" title="Click anywhere on the layout to place a comment pin">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
      Add Pin
    </button>
    <button class="review-btn" id="btn-mode-highlight" title="Hover over elements and click to highlight and leave feedback">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line></svg>
      Highlight
    </button>
  </div>

  <div class="review-btn-group">
    <button class="review-btn active" id="btn-view-desktop" title="Full Desktop View">
      Desktop
    </button>
    <button class="review-btn" id="btn-view-tablet" title="iPad / Tablet View (768px)">
      Tablet
    </button>
    <button class="review-btn" id="btn-view-mobile" title="Mobile iPhone View (390px)">
      Mobile
    </button>
  </div>

  <button class="review-btn btn-secondary" id="btn-toggle-drawer">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
    Notes <span class="review-badge" id="notes-count-badge">0</span>
  </button>

  <button class="review-btn btn-secondary" id="btn-copy-all-notes" title="Copy all feedback to clipboard to paste to Agent">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
    Copy Feedback
  </button>

  <!-- Minimize Button -->
  <button class="review-btn btn-minimize" id="btn-minimize-toolbar" title="Hide toolbar so it doesn't block the screen (or press H)">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
    Hide
  </button>
</div>

<!-- Floating Pill Trigger (shown when toolbar is minimized) -->
<button id="review-floating-trigger" title="Click to reopen review tools">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg>
  <span>Review Tools</span>
  <span class="review-badge" id="floating-badge">0</span>
</button>

<!-- Highlight Box -->
<div id="review-highlighter-box">
  <span id="review-highlighter-tag">Element</span>
</div>

<!-- Modal for Adding Note -->
<div id="review-modal-overlay">
  <div class="review-dialog">
    <h3 id="modal-heading">Add Review Note</h3>
    <p id="modal-subtext">Click save to anchor this note to the design.</p>
    <textarea id="modal-input" placeholder="Type what you want changed here (e.g., make this headline bolder, swap photo, change button text)..."></textarea>
    <div class="review-dialog-actions">
      <button class="review-btn" id="btn-modal-cancel" style="background: rgba(255,255,255,0.08); color: #94A3B8;">Cancel</button>
      <button class="review-btn" id="btn-modal-save" style="background: #DC2626; color: #FFFFFF; font-weight: 600;">Save Note</button>
    </div>
  </div>
</div>

<!-- Notes Drawer -->
<div id="review-drawer">
  <div class="review-drawer-header">
    <div class="review-drawer-title">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
      Review Notes (<span id="drawer-count">0</span>)
    </div>
    <button class="review-drawer-close" id="btn-close-drawer">&times;</button>
  </div>
  <div class="review-drawer-content" id="drawer-notes-list">
    <div style="text-align: center; color: #64748B; padding: 40px 10px; font-size: 13px;">
      No review notes yet.<br>Click "Add Pin" or "Highlight" to drop feedback directly on the design.
    </div>
  </div>
  <div class="review-drawer-footer">
    <button class="review-btn" id="btn-drawer-copy-feedback" style="background: #2563EB; color: #FFFFFF; width: 100%; justify-content: center; padding: 10px; font-weight: 600;">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
      Copy Feedback for Agent
    </button>
    <button class="review-btn" id="btn-drawer-clear-all" style="background: transparent; color: #64748B; width: 100%; justify-content: center; font-size: 11px;">
      Clear All Notes
    </button>
  </div>
</div>

<!-- Toast Notification -->
<div id="review-toast">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#22C55E" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
  <span id="toast-message">Feedback copied to clipboard!</span>
</div>
"""

preview_js = """
<script>
(function() {
  let currentMode = 'browse'; // 'browse', 'pin', 'highlight'
  let currentViewport = 'desktop'; // 'desktop', 'tablet', 'mobile'
  let isMinimized = false;
  let notes = JSON.parse(localStorage.getItem('auto_advantage_review_notes') || '[]');
  let pendingNoteTarget = null;
  let hoveredElement = null;

  const toolbar = document.getElementById('review-toolbar');
  const triggerBtn = document.getElementById('review-floating-trigger');
  const floatingBadge = document.getElementById('floating-badge');
  const container = document.getElementById('review-viewport-container');
  const highlighterBox = document.getElementById('review-highlighter-box');
  const highlighterTag = document.getElementById('review-highlighter-tag');
  const modalOverlay = document.getElementById('review-modal-overlay');
  const modalHeading = document.getElementById('modal-heading');
  const modalSubtext = document.getElementById('modal-subtext');
  const modalInput = document.getElementById('modal-input');
  const drawer = document.getElementById('review-drawer');
  const drawerNotesList = document.getElementById('drawer-notes-list');
  const countBadge = document.getElementById('notes-count-badge');
  const drawerCount = document.getElementById('drawer-count');
  const toast = document.getElementById('review-toast');

  // Buttons
  const btnBrowse = document.getElementById('btn-mode-browse');
  const btnPin = document.getElementById('btn-mode-pin');
  const btnHighlight = document.getElementById('btn-mode-highlight');
  const btnDesktop = document.getElementById('btn-view-desktop');
  const btnTablet = document.getElementById('btn-view-tablet');
  const btnMobile = document.getElementById('btn-view-mobile');
  const btnToggleDrawer = document.getElementById('btn-toggle-drawer');
  const btnCloseDrawer = document.getElementById('btn-close-drawer');
  const btnCopyAllNotes = document.getElementById('btn-copy-all-notes');
  const btnDrawerCopy = document.getElementById('btn-drawer-copy-feedback');
  const btnClearAll = document.getElementById('btn-drawer-clear-all');
  const btnMinimize = document.getElementById('btn-minimize-toolbar');
  const btnModalSave = document.getElementById('btn-modal-save');
  const btnModalCancel = document.getElementById('btn-modal-cancel');

  // Minimize / Expand functionality
  function minimizeToolbar() {
    isMinimized = true;
    toolbar.classList.add('minimized');
    triggerBtn.classList.add('show');
  }

  function expandToolbar() {
    isMinimized = false;
    toolbar.classList.remove('minimized');
    triggerBtn.classList.remove('show');
  }

  btnMinimize.addEventListener('click', minimizeToolbar);
  triggerBtn.addEventListener('click', expandToolbar);

  // Keyboard shortcut: H toggles toolbar, Esc closes modals or cancels pin mode
  window.addEventListener('keydown', (e) => {
    if (e.key === 'h' || e.key === 'H') {
      if (document.activeElement.tagName !== 'TEXTAREA' && document.activeElement.tagName !== 'INPUT') {
        if (isMinimized) expandToolbar();
        else minimizeToolbar();
      }
    } else if (e.key === 'Escape') {
      if (modalOverlay.style.display === 'flex') {
        modalOverlay.style.display = 'none';
        pendingNoteTarget = null;
      } else if (drawer.classList.contains('open')) {
        closeDrawer();
      } else if (currentMode !== 'browse') {
        setMode('browse');
      }
    }
  });

  function setMode(mode) {
    currentMode = mode;
    document.body.classList.remove('mode-pin', 'mode-highlight');
    btnBrowse.classList.toggle('active', mode === 'browse');
    btnPin.classList.toggle('active', mode === 'pin');
    btnHighlight.classList.toggle('active', mode === 'highlight');

    if (mode === 'pin') {
      document.body.classList.add('mode-pin');
      showToast('Click anywhere on the layout to place a comment pin');
    } else if (mode === 'highlight') {
      document.body.classList.add('mode-highlight');
      showToast('Hover and click any element to highlight and edit');
    }
    highlighterBox.style.display = 'none';
  }

  btnBrowse.addEventListener('click', () => setMode('browse'));
  btnPin.addEventListener('click', () => setMode('pin'));
  btnHighlight.addEventListener('click', () => setMode('highlight'));

  function setViewport(vp) {
    currentViewport = vp;
    container.classList.remove('viewport-tablet', 'viewport-mobile');
    btnDesktop.classList.toggle('active', vp === 'desktop');
    btnTablet.classList.toggle('active', vp === 'tablet');
    btnMobile.classList.toggle('active', vp === 'mobile');

    if (vp === 'tablet') container.classList.add('viewport-tablet');
    if (vp === 'mobile') container.classList.add('viewport-mobile');
    renderPins();
  }

  btnDesktop.addEventListener('click', () => setViewport('desktop'));
  btnTablet.addEventListener('click', () => setViewport('tablet'));
  btnMobile.addEventListener('click', () => setViewport('mobile'));

  function showToast(msg) {
    document.getElementById('toast-message').textContent = msg;
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 2400);
  }

  function saveNotes() {
    localStorage.setItem('auto_advantage_review_notes', JSON.stringify(notes));
    updateUI();
  }

  function updateUI() {
    countBadge.textContent = notes.length;
    floatingBadge.textContent = notes.length;
    drawerCount.textContent = notes.length;
    renderPins();
    renderDrawer();
  }

  function renderPins() {
    document.querySelectorAll('.review-pin').forEach(el => el.remove());
    notes.forEach((note, index) => {
      const pin = document.createElement('div');
      pin.className = 'review-pin';
      pin.setAttribute('data-id', note.id);
      pin.innerHTML = `<span>${index + 1}</span>`;
      pin.style.left = note.x + 'px';
      pin.style.top = note.y + 'px';

      pin.addEventListener('click', (e) => {
        e.stopPropagation();
        openDrawer();
        const noteCard = document.getElementById('note-card-' + note.id);
        if (noteCard) {
          noteCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
          noteCard.style.borderColor = '#DC2626';
          setTimeout(() => noteCard.style.borderColor = '', 1500);
        }
      });

      container.appendChild(pin);
    });
  }

  function renderDrawer() {
    if (notes.length === 0) {
      drawerNotesList.innerHTML = `
        <div style="text-align: center; color: #64748B; padding: 40px 10px; font-size: 13px;">
          No review notes yet.<br>Click "Add Pin" or "Highlight" to drop feedback directly on the design.
        </div>`;
      return;
    }

    drawerNotesList.innerHTML = notes.map((note, idx) => `
      <div class="review-note-card" id="note-card-${note.id}">
        <div class="review-note-header">
          <div class="review-note-tag">
            <span class="review-note-num">${idx + 1}</span>
            <span>${escapeHtml(note.targetLabel || 'Custom Pin')}</span>
          </div>
          <button class="review-note-delete" onclick="window.deleteReviewNote('${note.id}')" title="Delete note">&times;</button>
        </div>
        <div class="review-note-body">${escapeHtml(note.text)}</div>
        <div class="review-note-footer">
          <span>${note.timestamp}</span>
          <span class="review-note-jump" onclick="window.jumpToReviewNote('${note.id}')">Scroll to pin &#8250;</span>
        </div>
      </div>
    `).join('');
  }

  function escapeHtml(str) {
    if (!str) return '';
    return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  window.deleteReviewNote = function(id) {
    notes = notes.filter(n => n.id !== id);
    saveNotes();
  };

  window.jumpToReviewNote = function(id) {
    const note = notes.find(n => n.id === id);
    if (!note) return;
    const pin = document.querySelector(`.review-pin[data-id="${id}"]`);
    if (pin) {
      pin.scrollIntoView({ behavior: 'smooth', block: 'center' });
      pin.style.transform = 'translate(-50%, -50%) scale(1.6)';
      setTimeout(() => pin.style.transform = '', 1000);
    }
  };

  container.addEventListener('mousemove', (e) => {
    if (currentMode !== 'highlight') {
      highlighterBox.style.display = 'none';
      return;
    }

    let target = e.target;
    if (!target || target.closest('#review-toolbar') || target.closest('#review-drawer') || target.closest('#review-modal-overlay') || target.closest('#review-floating-trigger') || target.classList.contains('review-pin')) {
      highlighterBox.style.display = 'none';
      return;
    }

    const rect = target.getBoundingClientRect();
    const cRect = container.getBoundingClientRect();

    highlighterBox.style.display = 'block';
    highlighterBox.style.top = (rect.top - cRect.top) + 'px';
    highlighterBox.style.left = (rect.left - cRect.left) + 'px';
    highlighterBox.style.width = rect.width + 'px';
    highlighterBox.style.height = rect.height + 'px';

    const tagName = target.tagName.toLowerCase();
    const textSnippet = (target.textContent || '').trim().slice(0, 24);
    highlighterTag.textContent = `<${tagName}> ${textSnippet ? '"' + textSnippet + '..."' : ''}`;
    hoveredElement = target;
  });

  container.addEventListener('click', (e) => {
    if (currentMode === 'browse') return;

    if (e.target.closest('#review-toolbar') || e.target.closest('#review-drawer') || e.target.closest('#review-modal-overlay') || e.target.closest('#review-floating-trigger') || e.target.classList.contains('review-pin')) {
      return;
    }

    e.preventDefault();
    e.stopPropagation();

    const cRect = container.getBoundingClientRect();
    const x = e.clientX - cRect.left;
    const y = e.clientY - cRect.top + container.scrollTop;

    let targetLabel = 'Custom Position';
    if (currentMode === 'highlight' && hoveredElement) {
      const tag = hoveredElement.tagName.toLowerCase();
      const txt = (hoveredElement.textContent || '').trim().slice(0, 28);
      targetLabel = `${tag.toUpperCase()}: ${txt ? txt : 'Section'}`;
    } else {
      const el = document.elementFromPoint(e.clientX, e.clientY);
      if (el) {
        const tag = el.tagName.toLowerCase();
        const txt = (el.textContent || '').trim().slice(0, 28);
        targetLabel = `${tag.toUpperCase()}: ${txt ? txt : 'Layout'}`;
      }
    }

    pendingNoteTarget = {
      id: 'note_' + Date.now(),
      x: Math.round(x),
      y: Math.round(y),
      targetLabel: targetLabel,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    };

    modalHeading.textContent = `Feedback on: ${targetLabel}`;
    modalSubtext.textContent = 'Enter your exact comment or requested edit below:';
    modalInput.value = '';
    modalOverlay.style.display = 'flex';
    modalInput.focus();
  });

  btnModalCancel.addEventListener('click', () => {
    modalOverlay.style.display = 'none';
    pendingNoteTarget = null;
  });

  btnModalSave.addEventListener('click', () => {
    const val = modalInput.value.trim();
    if (!val) return;
    if (pendingNoteTarget) {
      pendingNoteTarget.text = val;
      notes.push(pendingNoteTarget);
      saveNotes();
      pendingNoteTarget = null;
      modalOverlay.style.display = 'none';
      showToast('Note added! Click "Copy Feedback" when ready');
    }
  });

  function openDrawer() { drawer.classList.add('open'); }
  function closeDrawer() { drawer.classList.remove('open'); }
  btnToggleDrawer.addEventListener('click', () => drawer.classList.toggle('open'));
  btnCloseDrawer.addEventListener('click', closeDrawer);

  function copyAllNotes() {
    if (notes.length === 0) {
      showToast('No notes yet to copy');
      return;
    }

    let summary = '### Visual Review Feedback for Auto Advantage Website\\n\\n';
    notes.forEach((note, idx) => {
      summary += `${idx + 1}. **[${note.targetLabel}]**: ${note.text}\\n`;
    });
    summary += '\\nPlease apply these requested edits to the site.';

    navigator.clipboard.writeText(summary).then(() => {
      showToast('Feedback copied! Paste it in the chat');
    }).catch(() => {
      showToast('Feedback copied! Paste it in the chat');
    });
  }

  btnCopyAllNotes.addEventListener('click', copyAllNotes);
  btnDrawerCopy.addEventListener('click', copyAllNotes);

  btnClearAll.addEventListener('click', () => {
    if (confirm('Are you sure you want to clear all review notes?')) {
      notes = [];
      saveNotes();
      showToast('All review notes cleared');
    }
  });

  updateUI();
})();
</script>
"""

# Assemble preview.html
head_close = html.rfind('</head>')
html_with_css = html[:head_close] + f"<style>{preview_css}</style>\n" + html[head_close:]

body_match = re.search(r'<body[^>]*>', html_with_css)
body_tag_end = body_match.end()
body_close = html_with_css.rfind('</body>')

final_preview = (
    html_with_css[:body_tag_end] +
    "\n" + preview_markup +
    "\n<div id=\"review-viewport-container\">\n" +
    html_with_css[body_tag_end:body_close] +
    "\n</div><!-- end review-viewport-container -->\n" +
    preview_js +
    "\n</body>\n</html>"
)

final_preview = final_preview.replace('—', ' ').replace('–', ' ')

with open('/Users/amirbahalwan/.gemini/antigravity/scratch/auto-advantage-website/preview.html', 'w', encoding='utf-8') as f:
    f.write(final_preview)

with open('/Users/amirbahalwan/.gemini/antigravity/brain/b789549c-086c-4f12-b831-4ab3ed9bd659/preview.html', 'w', encoding='utf-8') as f:
    f.write(final_preview)

print("Updated preview.html with bottom-docked collapsible toolbar!")
