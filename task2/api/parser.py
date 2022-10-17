import asyncio
import aiohttp
from playwright.async_api import async_playwright, Playwright
from pydantic import BaseModel


class WB_data(BaseModel):
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
            wb_data = WB_data(**data)
            return wb_data.dict()


# +++++++++++++++++++++++++++ Take url with card.json and wait tasks +++++++++++++++++++++++++++++++++++++
async def get_task(urls_json):
    task = await asyncio.gather(*[basket(url_json) for url_json in urls_json])
    return list(task)


# +++++++++++++++++++++++++++ Find url with card.json +++++++++++++++++++++++++++++++++++++++++++++++++++
async def find_json_url(p: Playwright, urls):
    list_finf_urls = []
    for url in urls:
        browser_type = p.chromium
        browser = await browser_type.launch()
        page = await browser.new_page()
        page.on("response", lambda response: list_finf_urls.append(response.url))
        await page.goto(url, wait_until="networkidle")
        await browser.close()
    urls_json = [i for i in list_finf_urls if 'card.json' in i]
    a = await get_task(urls_json)
    return a


# +++++++++++++++++++++++++++ Create task +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
async def main(urls):
    async with async_playwright() as p:
        results = await asyncio.create_task(find_json_url(p, urls))
        return results


def start(urls):
    a = asyncio.run(main(urls))
    return a


# +++++++++++++++++++++++++++ Take list urls +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def paresr_data(urls):
    a = start(urls)
    return a
