import asyncio


"""
python -m a002_book.b31_parallel.c4_asyncio.d1_sleep
"""


async def f(n):
    print(f'SLEEP for {n} seconds')
    await asyncio.sleep(n)
    print(f'back after {n} seconds')
    return n


async def consecutive():
    print('consecutive:')
    await f(2.5)
    await f(2)


async def consecutive2():
    print('consecutive2:')
    await asyncio.create_task(f(2.5))
    await asyncio.create_task(f(2))


async def parallel():
    print('parallel:')
    a = asyncio.create_task(f(2.5))
    b = asyncio.create_task(f(2))
    await a
    await b  # not needed


asyncio.run(consecutive())
print('----------------------')
asyncio.run(consecutive2())
print('----------------------')
asyncio.run(parallel())



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
