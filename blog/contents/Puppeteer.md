#### Puppeteer
<br><br>
>Puppeteer is a Node library which provides a high-level API to control headless Chrome or Chromium over the DevTools Protocol. It can also be configured to use full (non-headless) Chrome or Chromium.

#### What can I do
* Modern Node Library for headless Chrome/Chromium
* async/await, heavy ES7. Also supports Node 6.
* Zero config. Bundles latest Chromium
* High level APIs for common use cases
* Chrome’s reference for using the DevTools protocol
* Take screenshots & create PDF
* A/B testing & network interception
* Inject styles/script in page
* Offline testing
* Tracing & performance metrics
* Code coverage
* Running headless in the cloud
* SSR/pre-rendering
* Mobile viewport emulation
* Network emulation
* ‘Render as Google’ search check
<br><br>

#### Code Example in Javascript
##### Get Started
```commandline
npm i puppeteer
npm i puppeteer-core
```
<br>

##### Screenshot
```javascript
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com');
  await page.screenshot({path: 'example.png'});

  await browser.close();
})();
```
<br>

##### create a PDF
```javascript
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://news.ycombinator.com', {waitUntil: 'networkidle2'});
  await page.pdf({path: 'hn.pdf', format: 'A4'});

  await browser.close();
})();
```
<br>

##### evaluate script in the context of the page
```javascript
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com');

  // Get the "viewport" of the page, as reported by the page.
  const dimensions = await page.evaluate(() => {
    return {
      width: document.documentElement.clientWidth,
      height: document.documentElement.clientHeight,
      deviceScaleFactor: window.devicePixelRatio
    };
  });

  console.log('Dimensions:', dimensions);

  await browser.close();
})();
```
<br>

#### Code Example in Python
##### Get Started
```commandline
python3 -m pip install pyppeteer
```
<br>

##### open web page and take a screenshot
```python
import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://example.com')
    await page.screenshot({'path': 'example.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
```
<br>

##### evaluate script on the page.
```python
import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://example.com')
    await page.screenshot({'path': 'example.png'})

    dimensions = await page.evaluate('''() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }''')

    print(dimensions)
    # >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
```

##### Reference
* https://developers.google.com/web/tools/puppeteer/
* https://youtu.be/lhZOFUY1weo
* https://github.com/GoogleChrome/puppeteer
* https://pypi.org/project/pyppeteer/
<br><br>

> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.