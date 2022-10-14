import asyncio
import aiohttp
from playwright.async_api import async_playwright, Playwright
from pydantic import BaseModel


class Person(BaseModel):
    article: str
    brand: str
    title: str


# +++++++++++++++++++++++++++ Find by links *json and create data with pydantic +++++++++++++++++++++++++++++++
async def basket(url_json):
    async with aiohttp.ClientSession() as session:
        async with session.get(url_json) as resp:
            a = await resp.json()
            title = a['imt_name'].replace('"', '*')
            data = {"article": a['nm_id'], "brand": a['selling']['brand_name'], "title": title}
            person = Person(**data)
            return person.dict()


# +++++++++++++++++++++++++++ Take url with card.json and wait tasks +++++++++++++++++++++++++++++++++++++
async def get_task(ur):
    task = await asyncio.gather(*[basket(url_json) for url_json in ur])
    return list(task)


# +++++++++++++++++++++++++++ Find url with card.json +++++++++++++++++++++++++++++++++++++++++++++++++++
async def run(p: Playwright, urls):
    f = []
    for url in urls:
        browser_type = p.chromium
        browser = await browser_type.launch()
        page = await browser.new_page()
        page.on("response", lambda response: f.append(response.url))
        await page.goto(url, wait_until="networkidle")
        await browser.close()
    d = [i for i in f if 'card.json' in i]
    a = await get_task(d)
    return a


# +++++++++++++++++++++++++++ Create task +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
async def main(urls):
    async with async_playwright() as p:
        results = await asyncio.create_task(run(p, urls))
        return results


def start(urls):
    a = asyncio.run(main(urls))
    return a


# +++++++++++++++++++++++++++ Take list urls +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def tr(list_json):
    a = start(list_json)
    return a
