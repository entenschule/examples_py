import random

import asyncio
import aiohttp
import aiofiles

from ..shared import article_names_1, article_names_2, tock, make_download_folder


"""
python -m a002_book.b31_parallel.c4_asyncio.d2_crawler.e3_aiofiles
"""


download_path = make_download_folder(__file__)


queue_maxsize = 3
number_of_consumers = 5


async def find_articles_1(queue):
    for article_name in article_names_1:
        await queue.put(article_name)
        await asyncio.sleep(random.random())


async def find_articles_2(queue):
    for article_name in article_names_2:
        await queue.put(article_name)
        await asyncio.sleep(random.random())


async def download(session, i, queue):
    while True:
        article_name = await queue.get()
        url = f"https://en.wikipedia.org/wiki/{article_name}"
        async with session.get(url) as response:
            async with aiofiles.open(f"{download_path}/{article_name}.html", "w") as f:
                await f.write(await response.text())
                print(f"Consumer {i} has downloaded {article_name}.")
        queue.task_done()


async def crawl():
    queue = asyncio.Queue(maxsize=queue_maxsize)
    producers = [
        asyncio.create_task(find_articles_1(queue)),
        asyncio.create_task(find_articles_2(queue))
    ]
    async with aiohttp.ClientSession() as session:
        consumers = [asyncio.create_task(download(session, i, queue)) for i in range(number_of_consumers)]
        await asyncio.gather(*producers)
        await queue.join()
    for c in consumers:
        c.cancel()


asyncio.run(crawl())
