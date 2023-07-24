import os
import asyncio
import aiohttp
from ..shared import article_names, tock


"""
python -m a002_book.b31_parallel.c4_asyncio.d2_crawler.e2_queue
"""


parent_path = os.path.dirname(__file__)
download_path = parent_path + '/DOWNLOADS'
try:
    os.mkdir(download_path)
except FileExistsError:
    pass


def find_articles(queue):
    for article_name in article_names:
        n = article_names.index(article_name)
        print(f'  {n}   {tock()}')
        queue.put_nowait(article_name)


async def download(session, i, queue, html_dict):
    while True:
        article_name = await queue.get()
        n = article_names.index(article_name)
        url = f'https://en.wikipedia.org/wiki/{article_name}'
        async with session.get(url) as response:
            print(f'▽ {n}   {tock()}')
            html_dict[article_name] = await response.text()
            print(f'▼ {n}c{i} {tock()}')  # `i` is the index of the consumer
        queue.task_done()


async def crawl():
    print(f'CRAWL {tock()}')
    queue = asyncio.Queue()
    find_articles(queue)
    html_dict = {}
    async with aiohttp.ClientSession() as s:
        consumers = [asyncio.create_task(download(s, i, queue, html_dict)) for i in range(3)]
        await queue.join()
    for c in consumers:
        c.cancel()
    return html_dict


html_dict = asyncio.run(crawl())
for article_name, content in html_dict.items():
    n = article_names.index(article_name)
    print(f'○ {n}   {tock()}')
    with open(f'{download_path}/{article_name}.html', 'w') as f_html:
        f_html.write(content)


"""
CRAWL 0.001
  0   0.001
  1   0.001
  2   0.001
  3   0.001
  4   0.001
  5   0.002
  6   0.002
  7   0.002
  8   0.002
  9   0.002
▽ 0   0.253
▽ 1   0.255
▽ 2   0.263
▼ 0c0 0.61
▼ 2c2 0.629
▼ 1c1 0.638
▽ 3   0.719
▽ 4   0.752
▽ 5   0.797
▼ 3c0 0.899
▼ 4c2 0.975
▼ 5c1 0.992
▽ 6   1.016
▽ 7   1.123
▼ 6c0 1.134
▽ 8   1.175
▼ 7c2 1.254
▽ 9   1.285
▼ 9c0 1.369
▼ 8c1 1.371
○ 0   1.372
○ 2   1.388
○ 1   1.392
○ 3   1.412
○ 4   1.415
○ 5   1.428
○ 6   1.431
○ 7   1.434
○ 9   1.436
○ 8   1.439
"""
