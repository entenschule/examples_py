import os
import asyncio
import aiohttp
from ..shared import article_names, tock


"""
python -m a002_book.b31_parallel.c4_asyncio.d2_crawler.e1_simple
"""


parent_path = os.path.dirname(__file__)
download_path = parent_path + '/DOWNLOADS'
try:
    os.mkdir(download_path)
except FileExistsError:
    pass


async def download(session, article_name):
    n = article_names.index(article_name)
    print(f'  {n}   {tock()}')
    url = f'https://en.wikipedia.org/wiki/{article_name}'
    async with session.get(url) as response:
        print(f'▽ {n}   {tock()}')
        html = await response.text()
        print(f'▼ {n}   {tock()}')
        return html


async def crawl(article_names):
    print(f'CRAWL {tock()}')
    async with aiohttp.ClientSession() as session:
        coroutines = [download(session, _) for _ in article_names]
        return await asyncio.gather(*coroutines)


crawled_articles = asyncio.run(crawl(article_names))

article_zip = zip(article_names, crawled_articles)


for article_name, content in article_zip:
    n = article_names.index(article_name)
    print(f'○ {n}   {tock()}')
    filename = f'{download_path}/{article_name}.html'
    with open(filename, 'w') as file:
        file.write(content)


"""
CRAWL 0.0
  0   0.001
  1   0.002
  2   0.002
  3   0.003
  4   0.003
  5   0.003
  6   0.003
  7   0.004
  8   0.004
  9   0.004
▽ 1   0.219
▽ 4   0.264
▽ 2   0.265
▽ 3   0.269
▽ 0   0.284
▽ 5   0.337
▽ 6   0.344
▽ 7   0.346
▽ 8   0.35
▽ 9   0.514
▼ 1   1.007
▼ 9   1.013
▼ 4   1.032
▼ 8   1.056
▼ 3   1.067
▼ 7   1.147
▼ 2   1.302
▼ 5   1.376
▼ 6   1.38
▼ 0   1.489
○ 0   1.493
○ 1   1.509
○ 2   1.523
○ 3   1.536
○ 4   1.541
○ 5   1.544
○ 6   1.547
○ 7   1.551
○ 8   1.554
○ 9   1.556
"""
