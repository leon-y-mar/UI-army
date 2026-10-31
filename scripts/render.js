#!/usr/bin/env node
/*
 * Render de prototipos UI-Army en los viewports del producto.
 * Uso: node scripts/render.js <id> <iter> <producto> [light|light,dark]
 *   producto: ecommerce | reservas | toma-de-pedido
 * Salida: tasks/<id>/evaluations/shots/iter-0N-<v>-<ancho>-<tema>.png
 * Reporta scroll horizontal (scrollWidth > ancho del viewport) por captura.
 * Usa el Playwright/Chromium del entorno: no ejecutar "playwright install".
 */
const path = require('path');
const fs = require('fs');

let chromium;
try {
  ({ chromium } = require('playwright'));
} catch (e) {
  console.error('SIN RENDER: playwright no está disponible (' + e.message + ')');
  process.exit(2);
}

const VIEWPORTS = {
  'ecommerce': [[1440, 900], [390, 844]],
  'reservas': [[820, 1180]],
  'toma-de-pedido': [[1180, 820]],
};

const [id, iter, producto, temasArg = 'light'] = process.argv.slice(2);
if (!id || !iter || !VIEWPORTS[producto]) {
  console.error('Uso: node scripts/render.js <id> <iter> <ecommerce|reservas|toma-de-pedido> [light|light,dark]');
  process.exit(1);
}

const root = path.resolve(__dirname, '..');
const protoDir = path.join(root, 'tasks', id, 'prototypes');
const shotsDir = path.join(root, 'tasks', id, 'evaluations', 'shots');
fs.mkdirSync(shotsDir, { recursive: true });

const n = String(iter).padStart(2, '0');
const device = producto === 'ecommerce' ? '' : '&device=tablet';
const temas = temasArg.split(',');
const versiones = ['v1', 'v2', 'v3'].filter(v => fs.existsSync(path.join(protoDir, v + '.html')));
if (!versiones.length) {
  console.error('No hay v1/v2/v3.html en ' + protoDir);
  process.exit(1);
}

(async () => {
  let browser;
  try {
    browser = await chromium.launch();
  } catch (e) {
    console.error('SIN RENDER: no se pudo abrir Chromium (' + e.message + ')');
    process.exit(2);
  }
  for (const v of versiones) {
    for (const [w, h] of VIEWPORTS[producto]) {
      for (const tema of temas) {
        const page = await browser.newPage({ viewport: { width: w, height: h } });
        const errores = [];
        page.on('pageerror', err => errores.push(err.message));
        const url = 'file://' + path.join(protoDir, v + '.html') + '?theme=' + tema + device;
        await page.goto(url, { waitUntil: 'networkidle' }).catch(() => page.goto(url));
        const scrollW = await page.evaluate(() => document.documentElement.scrollWidth);
        const file = `iter-${n}-${v}-${w}-${tema}.png`;
        await page.screenshot({ path: path.join(shotsDir, file), fullPage: true });
        const flags = [];
        if (scrollW > w) flags.push(`SCROLL-HORIZONTAL ${scrollW}px > ${w}px`);
        if (errores.length) flags.push('JS-ERROR ' + errores.join(' | '));
        console.log(`${file} ${flags.length ? '[REVISAR] ' + flags.join(' · ') : 'ok'}`);
        await page.close();
      }
    }
  }
  await browser.close();
})();
