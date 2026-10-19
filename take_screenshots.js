const { spawn } = require('child_process');
const fs = require('fs');

async function main() {
  const chrome = spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', [
    '--headless',
    '--disable-gpu',
    '--remote-debugging-port=9222',
    '--window-size=1280,1000'
  ]);

  // wait for chrome to start
  await new Promise(r => setTimeout(r, 1500));

  try {
    const listRes = await fetch('http://127.0.0.1:9222/json/list');
    const list = await listRes.json();
    let wsUrl = list[0]?.webSocketDebuggerUrl;

    if (!wsUrl) {
      const newTabRes = await fetch('http://127.0.0.1:9222/json/new?http://localhost:3000/index.html');
      const newTab = await newTabRes.json();
      wsUrl = newTab.webSocketDebuggerUrl;
    }

    const ws = new WebSocket(wsUrl);
    await new Promise((res, rej) => {
      ws.onopen = res;
      ws.onerror = rej;
    });

    let id = 1;
    function send(method, params = {}) {
      return new Promise((resolve) => {
        const curId = id++;
        const handler = (evt) => {
          const data = JSON.parse(evt.data);
          if (data.id === curId) {
            ws.removeEventListener('message', handler);
            resolve(data.result);
          }
        };
        ws.addEventListener('message', handler);
        ws.send(JSON.stringify({ id: curId, method, params }));
      });
    }

    await send('Page.enable');
    await send('Page.navigate', { url: 'http://localhost:3000/index.html' });
    await new Promise(r => setTimeout(r, 2000));

    // Capture sections
    const sections = [
      { name: 'section_hero', selector: '.hero' },
      { name: 'section_philosophy', selector: '.philosophy-statement' },
      { name: 'section_craftsmanship', selector: '#craftsmanship' },
      { name: 'section_insurance', selector: '.insurance-section' },
      { name: 'section_financing', selector: '#financing' },
      { name: 'section_reviews', selector: '#reviews' },
      { name: 'section_booking', selector: '#book-appointment' },
      { name: 'section_instagram', selector: '.instagram-section' }
    ];

    for (const sec of sections) {
      await send('Runtime.evaluate', {
        expression: `
          const el = document.querySelector('${sec.selector}');
          if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
        `
      });
      await new Promise(r => setTimeout(r, 600));

      const shot = await send('Page.captureScreenshot', { format: 'png' });
      fs.writeFileSync(`${sec.name}.png`, Buffer.from(shot.data, 'base64'));
      console.log(`Saved ${sec.name}.png`);
    }

    ws.close();
  } catch (err) {
    console.error('Error during capture:', err);
  } finally {
    chrome.kill();
  }
}

main();
