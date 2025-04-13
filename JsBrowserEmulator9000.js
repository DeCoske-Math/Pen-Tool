const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('URL u want');
  const content = await page.content();
  console.log(content);
  await browser.close();
})();
