import asyncio
import httpx
import feedparser
import time
from constants import *
from models import *

async def make_request(url: str, keywords: list[str]) -> Site_Data:
    start = time.perf_counter()
    title_data = []

    try:
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.get(url)
            feed = feedparser.parse(response.content)

            for entry in feed.entries:
                included_keywords = [word for word in keywords if word in entry.title]
                if included_keywords:
                    title_data.append(Title_Data(str(entry.title), included_keywords, {}))

    except Exception as e:
        print(f"An error occurred when fetching {url}:" + str(e))

    duration = time.perf_counter() - start

    return Site_Data(url, title_data, duration)

async def fetch_titles(keywords: list[str]) -> list[Site_Data]:
    site_datas = await asyncio.gather(*(make_request(url, keywords) for url in feeds))
    site_datas = [site_data for site_data in site_datas if site_data.title_datas]

    useful_results = [ site_data for site_data in site_datas if site_data.titles ]

    return useful_results

def main(debug: bool, keywords: list[str] = [], ignore_words: list[str] = []) -> list[Site_Data]:
    results = asyncio.run(fetch_titles(keywords))
    
    if(debug):
        # Sort feeds by duration descending
        sorted_feeds = sorted(results, key=lambda d: d.response_time, reverse=True)

        print("Responsive feeds sorted by response time (slowest first):")
        for feed in sorted_feeds:
            print(f"{feed.response_time:.2f} sec - {feed.url}")
    
    return results
