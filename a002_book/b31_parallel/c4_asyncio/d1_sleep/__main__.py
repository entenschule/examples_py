import asyncio


"""
python -m a002_book.b31_parallel.c4_asyncio.d1_sleep
"""


async def sleep_print(n):
    print(f'SLEEP for {n} seconds')
    await asyncio.sleep(n)
    print(f'back after {n} seconds')


async def consecutive():
    print('consecutive:')
    await sleep_print(2.5)
    await sleep_print(2)


async def parallel():
    print('parallel:')
    a = asyncio.create_task(sleep_print(2.5))
    b = asyncio.create_task(sleep_print(2))
    await a
    await b


async def parallel_fail():
    print('parallel fail:')
    await asyncio.create_task(sleep_print(2.5))
    await asyncio.create_task(sleep_print(2))


asyncio.run(consecutive())
print('----------------------')
asyncio.run(parallel())
print('----------------------')
asyncio.run(parallel_fail())


"""
consecutive:
SLEEP for 2.5 seconds
back after 2.5 seconds
SLEEP for 2 seconds
back after 2 seconds
----------------------
parallel:
SLEEP for 2.5 seconds
SLEEP for 2 seconds
back after 2 seconds
back after 2.5 seconds
----------------------
parallel fail:
SLEEP for 2.5 seconds
back after 2.5 seconds
SLEEP for 2 seconds
back after 2 seconds
"""
